import os
import uuid
from ats_general import analyze_resume
from ats_job_des import get_ats_score_from_gemini
from ats_resume_improve import improve_resume_with_gemini
from ats_resume_rebuild import rebuild_resume_with_gemini
from latex_resume_gen import generate_latex_resume

def main():
    print("Select an option:")
    print("1. ATS score without job description")
    print("2. ATS score with job description (and improve if needed)")
    print("3. Directly enhance resume by rewriting (no job description needed)")
    print("4. Directly rebuild resume according to job description")
    user_choice = input("Enter 1, 2, 3, or 4: ").strip()

    resume_path = input("Enter the path to your resume file (pdf, docx, or image): ").strip()
    gemini_api_key = "AIzaSyC7wqktrMwFSs5SoqvyepwAImuga1zVCYw"  # Replace with your Gemini API key

    if user_choice == "1":
        # ATS without job description
        result = analyze_resume(resume_path)
        print("\nGeneral ATS Score:", result["score"])
        print(result["breakdown"])
        print(result["grade"])
        print(result["suggestions"])

    elif user_choice == "2":
        # ATS with job description and improve if needed
        job_title = input("Enter the job title you are applying for: ")
        job_description = input("Paste the job description here:\n")
        ats_feedback = get_ats_score_from_gemini(resume_path, job_description, gemini_api_key)
        print("\nGemini ATS Feedback:")
        print(ats_feedback)
        import re
        match = re.search(r'ATS score\s*[:\-]?\s*(\d+)', ats_feedback, re.IGNORECASE)
        score = int(match.group(1)) if match else 0

        if score >= 70:
            print("\nYou are a good fit for this job according to your resume!")
        elif 65 < score < 70:
            print("\nYour score is close! Improving your resume...")
            improved_resume = improve_resume_with_gemini(resume_path, job_description, gemini_api_key)
            print("\nImproved Resume:\n", improved_resume)
            latex_code = generate_latex_resume(latex_template, improved_resume, gemini_api_key)
            unique_id = uuid.uuid4().hex[:8]
            latex_filename = f"improved_resume_{unique_id}.tex"
            with open(latex_filename, "w", encoding="utf-8") as f:
                f.write(latex_code)
            print(f"LaTeX code saved as {latex_filename}")
        elif score <= 60:
            print("\nYour score is low. Let's rebuild your resume for this job...")
            rebuilt_resume = rebuild_resume_with_gemini(resume_path, job_title, job_description, gemini_api_key)
            print("\nRebuilt Resume:\n", rebuilt_resume)
            latex_code = generate_latex_resume(latex_template, rebuilt_resume, gemini_api_key)
            unique_id = uuid.uuid4().hex[:8]
            latex_filename = f"rebuilt_resume_{unique_id}.tex"
            with open(latex_filename, "w", encoding="utf-8") as f:
                f.write(latex_code)
            print(f"LaTeX code saved as {latex_filename}")
        else:
            print("\nYour score is in the mid-range. Please review your resume and try again.")

    elif user_choice == "3":
        # Directly enhance resume by rewriting (no job description)
        improved_resume = improve_resume_with_gemini(resume_path, "", gemini_api_key)
        print("\nEnhanced Resume:\n", improved_resume)
        latex_code = generate_latex_resume(latex_template, improved_resume, gemini_api_key)
        unique_id = uuid.uuid4().hex[:8]
        latex_filename = f"enhanced_resume_{unique_id}.tex"
        with open(latex_filename, "w", encoding="utf-8") as f:
            f.write(latex_code)
        print(f"LaTeX code saved as {latex_filename}")

    elif user_choice == "4":
        # Directly rebuild resume according to job description
        job_title = input("Enter the job title you are applying for: ")
        job_description = input("Paste the job description here:\n")
        rebuilt_resume = rebuild_resume_with_gemini(resume_path, job_title, job_description, gemini_api_key)
        print("\nRebuilt Resume:\n", rebuilt_resume)
        latex_code = generate_latex_resume(latex_template, rebuilt_resume, gemini_api_key)
        unique_id = uuid.uuid4().hex[:8]
        latex_filename = f"rebuilt_resume_{unique_id}.tex"
        with open(latex_filename, "w", encoding="utf-8") as f:
            f.write(latex_code)
        print(f"LaTeX code saved as {latex_filename}")

    else:
        print("Invalid option. Please run the program again and select 1, 2, 3, or 4.")

# Dummy LaTeX template (replace with your own)
latex_template = r"""
\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{fontawesome5}
\usepackage{multicol}
\setlength{\multicolsep}{-3.0pt}
\setlength{\columnsep}{-1pt}
\input{glyphtounicode}

\pagestyle{fancy}
\fancyhf{} 
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1.19in}
\addtolength{\topmargin}{-.7in}
\addtolength{\textheight}{1.4in}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large\bfseries
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

%-------------------------
% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\classesList}[4]{
    \item\small{
        {#1 #2 #3 #4 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & \textbf{\small #2} \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & \textbf{\small #2}\\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
\newcommand\sbullet[1][.5]{\mathbin{\vcenter{\hbox{\scalebox{#1}{\tiny$\bullet$}}}}}
\newcommand{\descript}[1]{\color{subheadings}\raggedright\hspace*{0pt}\hfill\vspace{3pt}\fontsize{11pt}{13pt}\selectfont {#1 \\} \normalfont}



\begin{document}


% \end{center}


\begin{center}
    
      {\Huge \scshape Alessandro Plasmati} \\\vspace{4pt}
       DOB: 01 Jan 2000 \quad HomeTown, District, HomeState   \\ \vspace{4pt}

    \small \raisebox{-0.1\height}\faPhone\ (+91) 1234567890 ~ \href{mailto:x@gmail.com}{\raisebox{-0.2\height}\faEnvelope\  \underline{alessandro@gmail.com}} ~ 
    \href{https://linkedin.com/in//}{\raisebox{-0.2\height}\faLinkedin\ \underline{alessandro}}  ~
    \href{https://github.com/}{\raisebox{-0.2\height}\faGithub\ \underline{alessandro}}
    %This Section Adds Additional Links like leetcode, codeforce, etc.
    \href{https://www.example.com}{\raisebox{-0.2\height}\faGlobe\ \underline{Random Link }}
    \href{https://example.com/gradecard.pdf}{\raisebox{-0.2\height}\faBook\ \underline{Gradecard}} 
    \vspace{-8pt}
\end{center}


%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {National Institute of Technology, Rourkela}{September 2021 -- Present}
      {Bachelor of Technology in Computer Science and Engineering (CGPA - 8.76)}{Rourkela, Odisha}
    \resumeSubheading
      {ODM Public School, Rourkela}{May 2021}
      {AISCCE -- CBSE, Science (PCM) (Percentage - 91\%)}{Bhubaneswar, Odisha}
    \resumeSubheading
      {Delhi Public School, Rourkela}{May 2019}
      {AISSE -- CBSE (Percentage - 95\%)}{Rourkela, Odisha}
  \resumeSubHeadingListEnd

%------RELEVANT COURSEWORK-------
\section{Relevant Coursework}

        \begin{multicols}{3}
            \begin{itemize}[itemsep=-5pt, parsep=3pt]
                \item\small Data Structures and Algorithm
                \item Database Management
                \item Object Oriented Programming
                \item Design and Analysis of Algorithms
                \item Operating System
                \item Computer Networks
                
                
                
            \end{itemize}
        \end{multicols}
        \vspace*{2.0\multicolsep}
    
    
%-----------Experience-----------%
\section{Work Experience}

  \resumeSubHeadingListStart

    \resumeSubheading
      {Electronics Company}{May 2023 -- August 2023}
      {Software Engineer Intern}{City, State}
      \resumeItemListStart
        \resumeItem{Developed a service to automatically perform a set of unit tests daily on a product in development to decrease time needed for team members to identify and fix bugs/issues.}
        \resumeItem{Incorporated scripts using Python and PowerShell to aggregate XML test results into an organized format to load code onto the hardware for daily testing.}
      \resumeItemListEnd
    \resumeSubHeadingListEnd
\vspace{-16pt}

%-----------PROJECTS-----------%

\section{Projects}
  \resumeSubHeadingListStart


    \resumeSubheading
      {The-Muscle-Studio}{May 2022 -- August 2022}
{React Js, Material UI, APIs}{\href{https://github.com/}{GitHub}}
      \resumeItemListStart
        \resumeItem{A fitness exercise web application used by over 100 users that has the functionality to choose specific categories based on muscle groups and equipments.}\\
        \resumeItem{User can browse more than 1000 exercises with practical examples and demo videos.}\\
        \resumeItem{ExerciseDB and Youtube Search API are used for fetching data from the internet.}\\
    \resumeItemListEnd
    
  \resumeSubHeadingListEnd
\vspace{-16pt}


\section{Achievements/Certifications}
\begin{itemize}[leftmargin=0.35in, itemsep=0pt, label={\tiny$\bullet$}]
    
    \item \small\textbf{Academic Excellence Award} \hfill \small\textbf{December 2023} \\
    Received Award from the Department of CSE for being in top 1 percent. \hfill \href{https://drive.google.com}{Certificate}
    
\end{itemize}
   
\vspace{-16pt}
%
%-----------PROGRAMMING SKILLS-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.35in, itemsep=0pt, label={\tiny$\bullet$}]
     \item \textbf{Languages}{: Python, C, HTML/CSS} 
     \item \textbf{Operating Systems}{: Windows, MacOS}
     \item \textbf{Developer Tools}{: VS Code, Sublime}
     \item \textbf{Technologies/Frameworks}{: React js, MongoDB, Tailwind}
    
 \end{itemize}
 \vspace{-16pt}


%-----------INVOLVEMENT---------------
\section{Extracurricular Activities}
    \resumeSubHeadingListStart
        \resumeSubheading{Fraternity}{September 2022 -- Present}{President}{University Name}
            \resumeItemListStart
                \resumeItem{Achieved a 4 star fraternity ranking by the Office of Fraternity and Sorority Affairs (highest possible ranking).}
                \resumeItem{Managed executive board of 5 members and ran weekly meetings to oversee progress in essential parts of the chapter.}
                \resumeItem{Led chapter of 30+ members to work towards goals that improve and promote community service, academics, and unity.}
            \resumeItemListEnd
        
    \resumeSubHeadingListEnd


\end{document}
"""

if __name__ == "__main__":
    main()