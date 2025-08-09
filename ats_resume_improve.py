import google.generativeai as genai
from ats_job_des import extract_text_from_file, split_sections, format_resume_for_gemini

def improve_resume_with_gemini(resume_path, job_description, gemini_api_key):
    raw_text = extract_text_from_file(resume_path)
    sections = split_sections(raw_text)
    formatted_resume = format_resume_for_gemini(sections)

    prompt = f"""
You are an expert resume writer and ATS optimizer.
Given the following RESUME and JOB DESCRIPTION, suggest improvements and rewrite the resume to achieve an ATS score of 70+.

Instructions:
1. Do not use *, #, or bullet points in your response.
2. For suggestions, use numbered lines, each with a short, clear detail (one line per suggestion, not too much detail).
3. Only improve the text and structure, do not add or remove entire sections.
4. Add quantifiable metrics, strong action verbs, and relevant keywords where appropriate.
5. Correct passive voice and grammar.
6. Ensure the improved resume fits on one page and is concise and impactful.
7. Return the improved resume in the same sectioned format as provided.

RESUME:
{formatted_resume}

JOB DESCRIPTION:
{job_description}

First, list suggestions for improvement as numbered lines (one line each, concise).
Then, provide the improved resume in the same sectioned format.
"""

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text.strip()