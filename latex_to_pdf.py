import subprocess
import os

def latex_to_pdf(latex_code, output_pdf):
    # Save LaTeX code to a temporary .tex file
    with open("temp.tex", "w", encoding="utf-8") as f:
        f.write(latex_code)
    
    # Run pdflatex to create PDF
    subprocess.run(["pdflatex", "-interaction=nonstopmode", "temp.tex"], stdout=subprocess.PIPE)
    
    # Rename/move the generated PDF
    if os.path.exists("temp.pdf"):
        os.rename("temp.pdf", output_pdf)
        print(f"PDF created: {output_pdf}")
    else:
        print("PDF generation failed.")
        
if __name__ == "__main__":
    latex_code = r"""
\documentclass{article}
\begin{document}
Hello, \LaTeX!
\end{document}
"""
    latex_to_pdf(latex_code, "output.pdf")