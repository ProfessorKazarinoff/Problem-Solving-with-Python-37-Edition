# tex_modify_contents.py
"""
This file contains a function and script to modify the .tex file
outputted by the nb2latex.py script to change:

\chapter*{Preface}\label{preface}
	\addcontentsline{toc}{chapter}{Preface}

\section*{Motivation}\label{motivation}
        \addcontentsline{toc}{section}{Motivation}

\chapter*{Appendix}\label{appendix}
\addcontentsline{toc}{chapter}{Appendix}


\renewcommand{\thesection}{\Alph{section}.}
\setcounter{section}{0}
"""
import re
import os
from pathlib import Path

def is_chapter(line, ch_title):
    re_str = r"\\chapter{" +ch_title + r"\b"
    m = re.compile(re_str)
    return m.match(line)

def is_section(line, sec_title):
    re_str = r"\\section{" + sec_title + r"\b"
    m = re.compile(re_str)
    return m.match(line)

def remove_ch_number_from_toc(ch_title):
    #line='\\chapter*{Preface}\\label{preface} \n \\addcontentsline{toc}{chapter}{Preface}}'
    outline = "\\chapter*{"+ch_title+"}\\label{"+ch_title.lower()+"} \n \\addcontentsline{toc}{chapter}{"+ch_title+"}} \n \markboth{" + ch_title.upper() + "}{}"
    return outline

def remove_sec_number_from_toc(sec_title):
    if " " in sec_title:
        lower_sec_title = sec_title.replace(" ","-").lower()
    else:
        lower_sec_title = sec_title.lower() 
    #line='\\chapter*{Preface}\\label{preface} \n \\addcontentsline{toc}{chapter}{Preface}}'
    outline = "\\section*{"+sec_title+"}\\label{"+lower_sec_title+"} \n \\addcontentsline{toc}{section}{"+sec_title+"}}"
    return outline

def process_tex_file(infile,outfile,ch_list,sec_list):
    with open(infile) as f:
        lines = f.readlines()

    outf = open(outfile, "w")
    for line in lines:
        for ch in ch_list:
            if is_chapter(line, ch):
                line = remove_ch_number_from_toc(ch)
                if ch=='Appendix':
                    line=line+'\n \\renewcommand{\\thesection}{\\Alph{section}.} \n \\setcounter{section}{0} \n  \\renewcommand{\\thesection}{Appendix \\Alph{section}} \n \\dottedcontents{section}[9.3em]{}{7em}{1pc} \n'
                print(line)
        for sec in sec_list:
            if is_section(line, sec):
                line = remove_sec_number_from_toc(sec)
                print(line)
        outf.write(line)
    outf.close()

def main():
    starting_tex_Path = Path(os.pardir,'pdf','out.tex')
    ending_tex_Path = Path(os.pardir,'pdf','out_new_toc.tex')
    ch_list=['Preface','Appendix']
    sec_list=['Motivation','Acknowledgments','Supporting Materials','Formatting Conventions','Errata']
    process_tex_file(starting_tex_Path,ending_tex_Path,ch_list,sec_list)
    print(f"processed file {starting_tex_Path}")
    print(f"output file: {ending_tex_Path}")

if __name__ == "__main__":
    main()
