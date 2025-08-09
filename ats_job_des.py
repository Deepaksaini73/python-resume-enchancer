import os
import re
import spacy
import google.generativeai as genai
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
import pytesseract
from PIL import Image
import easyocr

# Load spaCy
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import subprocess
    import sys
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Canonical section names mapped to header variations
SECTION_HEADERS = {
    "Contact Information": [
        "contact", "personal info", "details"
    ],
    "Professional Summary": [
        "professional summary", "summary", "career objective", "objective", "profile", "about me"
    ],
    "Skills": [
        "skills", "core competencies", "technical skills", "key skills"
    ],
    "Work Experience": [
        "work experience", "professional experience", "employment history", "career history"
    ],
    "Education": [
        "education", "academic background", "qualifications", "educational details"
    ],
    "Projects": [
        "projects", "key projects", "academic projects", "notable projects"
    ],
    "Certifications": [
        "certifications", "licenses", "courses", "professional certifications"
    ],
    "Awards & Achievements": [
        "awards", "achievements", "honors", "recognitions", "accomplishments"
    ],
    "Extracurricular Activities": [
        "extracurricular activities", "activities", "hobbies & interests", "leadership & activities"
    ],
    "Languages": [
        "languages", "language proficiency", "spoken languages"
    ],
    "Publications": [
        "publications", "research papers", "research work", "articles", "papers"
    ],
    "Volunteer Experience": [
        "volunteer experience", "community work", "volunteering", "social work"
    ]
}

# Flatten for fast lookup
HEADER_TO_SECTION = {}
for canonical, variations in SECTION_HEADERS.items():
    for v in variations:
        HEADER_TO_SECTION[v.lower()] = canonical


# Initialize EasyOCR reader (supports multiple languages)
reader = easyocr.Reader(['en'])

def extract_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        text = extract_pdf_text(file_path)

    elif ext == ".docx":
        doc = Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])

    elif ext in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
        # OCR for image files using EasyOCR
        results = reader.readtext(file_path, detail=0)  # detail=0 returns only text
        text = "\n".join(results)

    else:
        raise ValueError("Unsupported file type. Only PDF, DOCX, and image files are supported.")

    return text


def match_section(line):
    line_clean = line.strip().lower()
    for header, canonical in HEADER_TO_SECTION.items():
        # Match header at start of line, allow for ":" or "-" after header
        if re.match(rf"^{re.escape(header)}\b[\s:\-]*$", line_clean):
            return canonical
    return None

def split_sections(text):
    lines = text.splitlines()
    sections = {}
    current_section = "Other"
    buffer = []
    for line in lines:
        matched = match_section(line)
        if matched:
            if buffer:
                sections[current_section] = "\n".join(buffer).strip()
                buffer = []
            current_section = matched
        else:
            buffer.append(line)
    if buffer:
        sections[current_section] = "\n".join(buffer).strip()
    return sections

def format_resume_for_gemini(sections):
    formatted = []
    for sec, content in sections.items():
        formatted.append(f"--- {sec.upper()} ---\n{content.strip()}\n")
    return "\n".join(formatted)

def get_ats_score_from_gemini(resume_path, job_description, gemini_api_key):
    raw_text = extract_text_from_file(resume_path)
    sections = split_sections(raw_text)
    formatted_resume = format_resume_for_gemini(sections)

    prompt = f"""
You are an ATS (Applicant Tracking System) expert.
Given the following RESUME and JOB DESCRIPTION, analyze the resume for ATS-friendliness and job match.
Return your response in this concise, WhatsApp-friendly format (no #, *, or bullet points, use only numbers and headings):

1. ATS Score: (0-100)
2. Strengths: (just the main headings, not full sentences)
3. Weaknesses: (just the main headings, not full sentences)
4. Suggestions: (just the main headings, not full sentences)
5. Missing or Mismatched Skills/Keywords: (just the main headings, not full sentences)

RESUME:
{formatted_resume}

JOB DESCRIPTION:
{job_description}

Respond in the above format, using only numbers and headings, no extra text.
"""

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-pro')
    response = model.generate_content(prompt)
    return response.text.strip()

# Example usage:
# gemini_api_key = "YOUR_GEMINI_API_KEY"
# ats_feedback = get_ats_score_from_gemini("resume.pdf", "Job description text here", gemini_api_key)
# print(ats_feedback)