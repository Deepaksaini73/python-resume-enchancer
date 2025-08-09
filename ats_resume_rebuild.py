import google.generativeai as genai
from ats_job_des import extract_text_from_file, split_sections, format_resume_for_gemini

def find_resume_gaps_with_gemini(formatted_resume, job_title, job_description, gemini_api_key):
    prompt = f"""
You are an ATS and resume expert.
Given the RESUME and JOB TITLE/DESCRIPTION, list the top 3-5 most important missing or weak sections, projects, or skills that would improve the resume for this job.
For each, write a short question to ask the user if they have this experience or project.
Respond as a numbered list of questions only, no extra text.

RESUME:
{formatted_resume}

JOB TITLE:
{job_title}

JOB DESCRIPTION:
{job_description}
"""
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return [line.strip().split('. ', 1)[1] for line in response.text.strip().split('\n') if '. ' in line]

def get_user_or_gemini_answer(question, job_title, job_description, gemini_api_key):
    print(f"\n{question}\nType 'yes' to provide your own details, or 'no' to let the system add an attractive example for your resume:")
    user_has = input().strip().lower()
    if user_has == "yes":
        print("Please provide a short description/details for this (1-2 lines):")
        user_detail = input().strip()
        prompt = f"""
Rewrite the following user-provided detail as a strong, concise resume bullet or section for a {job_title} resume, matching the style of the rest of the resume. Do not use *, #, or bullet points, just a single line.
User detail: {user_detail}
Job description: {job_description}
"""
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content(prompt)
        # Robust error handling
        if hasattr(response, "text") and response.text and response.text.strip():
            return response.text.strip()
        else:
            print("Gemini did not return a response. Using your input as-is.")
            return user_detail
    else:
        prompt = f"""
Generate a strong, relevant project/skill/experience for a {job_title} resume, based on the following job description. Do not use *, #, or bullet points, just a single line.
Job description: {job_description}
"""
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel('gemini-2.5-pro')
        response = model.generate_content(prompt)
        # Robust error handling
        if hasattr(response, "text") and response.text and response.text.strip():
            return response.text.strip()
        else:
            print("Gemini did not return a response. Using a default example.")
            return f"Relevant {job_title} project or skill (details not provided)."

def rebuild_resume_with_gemini(resume_path, job_title, job_description, gemini_api_key):
    raw_text = extract_text_from_file(resume_path)
    sections = split_sections(raw_text)
    formatted_resume = format_resume_for_gemini(sections)

    # Step 1: Find gaps/questions
    questions = find_resume_gaps_with_gemini(formatted_resume, job_title, job_description, gemini_api_key)
    new_items = []

    # Step 2: For each gap, ask user or generate
    for q in questions:
        answer = get_user_or_gemini_answer(q, job_title, job_description, gemini_api_key)
        new_items.append(answer)

    # Step 3: Rebuild resume with new items
    prompt = f"""
You are an expert resume builder and ATS optimizer.
Given the following RESUME, JOB TITLE, JOB DESCRIPTION, and NEW ITEMS, rebuild the resume to be highly relevant and ATS-friendly for this job.

Instructions:
1. Remove any projects, technologies, or skills from the resume that are not suitable or relevant for the given job description.
2. Only include these sections in the final resume, in this order:
   - About section
   - Education
   - Relevant Coursework
   - Technical Skills
   - Projects (maximum 2, most relevant)
   - Awards & Achievements
   - Extracurricular Activities (maximum 1, most relevant)
3. Do not exceed one page in length. Keep all content concise and impactful. Avoid long sentences and unnecessary details.
4. If any section is missing or lacks content, generate attractive and relevant text to fill the gap, but keep it succinct.
5. Integrate the NEW ITEMS into the most appropriate sections.
6. Remove irrelevant or weak content.
7. Use only numbers for any lists, no *, #, or bullet points.
8. Return only the rebuilt resume in the same sectioned format as provided, with clear section headings. Do not include any explanation or extra text.

RESUME:
{formatted_resume}

JOB TITLE:
{job_title}

JOB DESCRIPTION:
{job_description}

NEW ITEMS TO ADD:
{chr(10).join([f"{i+1}. {item}" for i, item in enumerate(new_items)])}
"""

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text.strip()