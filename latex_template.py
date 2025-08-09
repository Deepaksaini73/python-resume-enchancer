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


%----------FONT OPTIONS----------
% sans-serif
% \usepackage[sfdefault]{FiraSans}
% \usepackage[sfdefault]{roboto}
% \usepackage[sfdefault]{noto-sans}
% \usepackage[default]{sourcesanspro}

% serif
% \usepackage{CormorantGaramond}
% \usepackage{charter}


\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
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

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


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
        \resumeItem{Implemented Jenkins to provide a continuous integration service to automate the entire process of loading code and test files, running the tests, and generating a report of the results once per day.}
        \resumeItem{Designed solutions to visualize and deliver daily reports of test results to team members  using HTML, Javascript, and CSS.}
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
    
    \item\small \textbf{NEST} \hfill \small\textbf{December 2023} \\
    Secured all India rank 25 in National Entrance Screening Test. \hfill \href{https://drive.google.com}{Certificate}
    
    \item \small\textbf{Smart India Hackathon Finalist} \hfill \small\textbf{December 2023} \\
    Developed a distributed voting system using XX.\hfill \href{https://drive.google.com}{Certificate}
    
    \item \small\textbf{Codeforces: Specialist Title} \hfill \small\textbf{December 2023} \\
    Achieved the title of Specialist with a peak rating of 1450.\hfill \href{https://drive.google.com}{Certificate}
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