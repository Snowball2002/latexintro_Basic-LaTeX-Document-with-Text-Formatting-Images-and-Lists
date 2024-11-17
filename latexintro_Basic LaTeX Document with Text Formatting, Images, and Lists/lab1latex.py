# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

latex_content = r"""
\documentclass{article}
\{graphicx} % Package to handle images
\{hyperref} % Package for hyperlinks (optional, but useful)

\title{Getting Started with LaTeX}
\author{Paolo Lauricella}
\date{\7/29/24}

\begin{document}

\

% 
Hello my name is Your Paolo I am currently learning LaTeX for my course and this is my initial document I am excited to discover the capabilities of LaTeX and improve my document creation skills

% Experimenting with various text formatting styles
This text is in \textbf{bold}. \\
This text is in \textit{italic}. \\
This text is \underline{underlined}.

% Adding and displaying an image
\begin{figure}[h!]
    \centering
    \includegraphics[width=0.5\textwidth]{example.png}
    \caption{Sample Image}
    \label{fig:sample_image}
\end{figure}

Figure \ref{fig:sample_image} 

% Creating an unordered list
\begin{itemize}
    \item Item one
    \item Item two
    \item Item three
\end{itemize}

\end{document}
"""


with open("latex_project.tex", "w") as file:
    file.write(latex_content)

print("LaTeX document has been generated as 'latex_project.tex'. Upload this file to Overleaf.")

