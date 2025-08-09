# ATS Resume Analyzer & Builder

This project provides an interactive command-line tool to:
- Analyze your resume for ATS-friendliness (with or without a job description)
- Suggest improvements or rebuild your resume for a specific job
- Enhance or rebuild your resume using Gemini AI
- Convert your resume to LaTeX format

## Features

1. **ATS Score Without Job Description**  
   Get a general ATS score and suggestions for your resume.

2. **ATS Score With Job Description**  
   Get a job-specific ATS score and, if needed, AI-powered improvements or a full rebuild.

3. **Direct Resume Enhancement**  
   Instantly enhance your resume wording and structure.

4. **Direct Resume Rebuild**  
   Rebuild your resume for a specific job, interactively filling gaps with your input or AI-generated content.

5. **LaTeX Resume Generation**  
   Generate a LaTeX version of your improved or rebuilt resume.

## Requirements

- Python 3.8+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (for image resume OCR, if using pytesseract)
- [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) (for PDF to image conversion)
- Gemini API key (for AI features)

## Installation

1. Clone this repository.
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) if you want to process image resumes.
4. Install [Poppler](https://github.com/oschwartz10612/poppler-windows/releases/) and add it to your PATH for PDF-to-image conversion.

## Usage

Run the main program:
```
python main.py
```
Follow the prompts to analyze, enhance, or rebuild your resume.

## File Structure

- `main.py` - Entry point, user interaction and workflow routing
- `ats_general.py` - General ATS scoring logic
- `ats_job_des.py` - Job-specific ATS scoring using Gemini
- `ats_resume_improve.py` - Resume enhancement logic
- `ats_resume_rebuild.py` - Interactive resume rebuilding logic
- `latex_resume_gen.py` - LaTeX resume generation using Gemini
- `latex_template.py` - LaTeX template string
- `latex_to_pdf.py` - Convert LaTeX code to PDF
- `pdf_to_image.py` - Convert PDF to image

## Notes

- Replace `"YOUR_GEMINI_API_KEY"` in `main.py` with your actual Gemini API key.
- For best results, use clear, well-formatted resumes and job descriptions.
- The LaTeX template can be customized in `latex_template.py`.

---
