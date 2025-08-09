import google.generativeai as genai

def generate_latex_resume(latex_template, resume_text, gemini_api_key):
    prompt = f"""
You are a LaTeX expert and resume formatter.
Given the following LaTeX resume template and resume data, fill the template with the resume data.
Instructions:
- Ensure the final resume is concise and fits within one page.
- Avoid long sentences and unnecessary details; keep each section brief and impactful.
- If any section is missing or lacks content, generate attractive and relevant text to fill the gap.
- Return only the complete LaTeX code, with no explanation, no extra text, and do not include any markdown formatting such as ```latex or ``` at the start or end. Only output the raw LaTeX code.
LATEX TEMPLATE:
{latex_template}

RESUME DATA:
{resume_text}
"""
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    # Robust error handling
    try:
        latex_code = response.text.strip()
        if not latex_code:
            raise ValueError("Empty LaTeX code returned.")
        return latex_code
    except Exception as e:
        print("Gemini did not return valid LaTeX code. Try reducing the template or resume size.")
        print("Error details:", e)
        return ""