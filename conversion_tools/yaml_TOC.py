#!/usr/bin/env python

"""
This module contains functions and a main script to construct a TOC yaml file for MkDocs
The TOC is saved in a .yml file for use in the mkdocs.yaml file
The TOC is built from the jupyter notebooks saved in the notebooks directory.
For the following directory structure and notebooks:

notebooks
    00-Preface
        00.00-Preface.ipynb             contains # Preface ## Preface
        0.001-Motivation.ipynb          contains ## Motivation
    01-Orientation
        01.00-Introduction.ipynb        contains # Orientation ## Introduction
        01.01-Formatting.ipynb          contains ## Formatting
        01.02-Summary.ipynb             contains ## Summary

The TOC.yml file produced will be of the form:

#TOC.yml
pages:
    - Home: index.md
    - Preface:
        - Preface: 00-Preface/00.00-Preface.md
        - Motivation: 00-preface/00.01-Motivation.md
    - Chapter 1 Orientation:
        - Introduction: 01-orientation/01.00-Introduction.md
        - Why Python?: 01-orientation/01.01-Formatting.md
        - Installing Python: 01-orientation/01.02-summary.md
"""

import nbformat
import os
import re


def get_notebook_chapter_title(nb_file):
    """
    Description: This function pulls out the markdown from a notebook when a cell starts with #
    this is often the notebook title.
    :param nb_file: string with path to jupyter notebook relative to cwd, str
    :return: Text after # in markdown, str
    """
    nb = nbformat.read(nb_file, as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('# '):
            chapter_title = cell.source[1:].splitlines()[0].strip()
    return chapter_title


def get_notebook_section_title(nb_file):
    """
    Description: This function pulls out the markdown from a notebook when a cell starts with ##
    this is often the section title or notebook title.
    :param nb_file: string with path to jupyter notebook relative to cwd, str
    :return: Text after ## in markdown, str
    """
    nb = nbformat.read(nb_file, as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('## '):
            section_title = cell.source[2:].splitlines()[0].strip()
    return section_title


def modext(instr,ext):
    """
    Converts the extension at the end of a string to a new extension
    Example in: modext('file.txt','md')  --> 'file.md'
    :param instr: str, the file name with a . extension
    :param ext: str, the extension ex: 'md' or 'txt' also '.md' and '.txt' will work as well
    :return: str, the new filename with the new extension
    """
    if ext.startswith('.'):
        ext = ext[1:]
    return "".join([instr.rsplit( ".", 1 )[0], '.', ext])

def ch_title_line(ch_title):
    """
    outputs a mkdoc.yml second level TOC entry from a string
    :param ch_title: str, the chapter title ex: 'Chapter 1 Introduction'
    :return: str, ex: '    - Chapter 1 Introduction:'
    """
    TAB = '    '
    return "".join([TAB,'- ', ch_title, ':'])

def print_yaml_TOC(infile='TOC.yml'):
    with open(infile, "r") as f:
        print(f.read())


def iter_notebook_sub_dir_file_name(notebook_dir_name='notebooks'):
    """
    Returns a list, elements are 'sub_directory/notebookfile.ipynb'
    :param notebook_dir_name: str, ex: 'notebooks'
    :return: list, with entries like: ['00-Preface/00.00-Preface.ipynb']
    """
    NOTEBOOK_DIR = os.path.join(os.pardir, notebook_dir_name)
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    REG_nb_dir = re.compile((r'(\d\d)-*'))

    nb_file_name_lst = []
    for dir in os.listdir(NOTEBOOK_DIR):
        if REG_nb_dir.match(dir):
            #print(dir)
            for nb in os.listdir(os.path.join(NOTEBOOK_DIR, dir)):
                if REG_nb.match(nb):
                    #print(nb)
                    nb_file_name_lst.append("/".join([dir,nb]))
    return sorted(nb_file_name_lst)


def make_yaml_TOC(nb_file_name_list, outfile):
    """
    Constructs the Table of Contents using a list of notebook names that include a file path
    :param nb_file_name_list: lst, example: ['02-The-Python-REPL/02.01-Mathmatical-Opperations', '02-The-Python-REPL/02.02-Math-Module']
    :param outfile: str, example: 'TOC.yml'
    """
    REG_nb_chap_title = re.compile(r'(\d\d)\.(00)-(.*)\.ipynb')
    nb_sec_title_and_file_name_list = ['# Content','pages:', '    - Home: index.md']
    for nb_sub_dir_and_filename in nb_file_name_list:
        print('nb sub dir and file name: ' + nb_sub_dir_and_filename)
        nb_filename = nb_sub_dir_and_filename.split("/")[1]
        print('nb file name: ' + nb_filename)
        nb_sub_dir = nb_sub_dir_and_filename.split("/")[0]
        print('nb subdir name: ' + nb_sub_dir)
        nb_path = os.path.join(os.pardir, 'notebooks', nb_sub_dir, nb_filename)
        print('nb path: ' + nb_path)

        if REG_nb_chap_title.match(nb_filename):
            print('notebook contains chapter title: ' + nb_filename)
            ch_title = get_notebook_chapter_title(nb_path)
            print('chapter title: ' + ch_title)
            if not 'Preface' in ch_title and not 'Appendix' in ch_title:
                ch_title = "".join(['Chapter ', nb_sub_dir[:2].lstrip('0'), ' ', ch_title])
            nb_sec_title_and_file_name_list.append(ch_title_line(ch_title))

        sec_title = get_notebook_section_title(nb_path)
        print('section title: ' + sec_title)
        nb_sec_title_and_file_name_list.append(
            "".join(['        - ', sec_title, ': ', modext(nb_sub_dir_and_filename, 'md')]))

    print(nb_sec_title_and_file_name_list)

    with open(outfile, "w") as f:
        f.write("\n".join(nb_sec_title_and_file_name_list))

def main():
    nb_lst = iter_notebook_sub_dir_file_name('notebooks')
    make_yaml_TOC(nb_lst, 'TOC.yml')
    print_yaml_TOC('TOC.yml')

if __name__ == '__main__':
    main()