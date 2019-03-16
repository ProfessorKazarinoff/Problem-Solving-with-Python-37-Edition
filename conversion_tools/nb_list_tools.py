## Adapted from Jake VanDerplas
# https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/tools/generate_contents.py
# From his Python Data Science Handhook github repo: https://github.com/jakevdp/PythonDataScienceHandbook

import os
import re
import itertools
import nbformat

NOTEBOOK_DIR = os.path.join(os.path.dirname(__file__), '..', 'notebooks')

CHAPTERS = {"00": "Preface",
            "01": "IPython: Beyond Normal Python",
            "02": "NumPy",
            "03": "Pandas",
            "04": "Matplotlib",
            "05": "Machine Learning"}

REG = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')


def iter_notebook_file_names(notebook_dir_name='notebooks'):
    import os
    import re
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
                    nb_file_name_lst.append(nb)

    return sorted(nb_file_name_lst)

def iter_notebook_sub_dirs(notebook_dir_name='notebooks'):
    import os
    import re
    NOTEBOOK_DIR = os.path.join(os.pardir, notebook_dir_name)
    REG_nb_dir = re.compile((r'(\d\d)-*'))
    nb_sub_dir_name_lst = []
    for dir in os.listdir(NOTEBOOK_DIR):
        if REG_nb_dir.match(dir):
            nb_sub_dir_name_lst.append(dir)

    return sorted(nb_sub_dir_name_lst)

def iter_notebook_sub_dirs_path(notebook_dir_name='notebooks'):
    """
    function outputs a list of paths of the notebooks sub dirs inside the notebook dir
    :param notebook_dir_name: str, the main directory with the notebooks, default 'notebooks'
    :return: lst, example ['../notebooks/00-Prefence','../notebooks/01-Introduction']
    """
    NOTEBOOK_DIR = os.path.join(os.pardir, notebook_dir_name)
    REG_nb_dir = re.compile((r'(\d\d)-*'))
    nb_sub_dir_path_lst = []
    for dir in os.listdir(NOTEBOOK_DIR):
        if REG_nb_dir.match(dir):
            dir_path=os.path.join(os.pardir, notebook_dir_name, dir)
            nb_sub_dir_path_lst.append(dir_path)

    return sorted(nb_sub_dir_path_lst)

def iter_docs_sub_dirs_path(docs_dir_name='docs'):
    """
    function outputs a list of paths of the docs sub dirs inside the docs dir
    :param docs_dir_name: str, the main directory with all the sub dirs that contain markdown for the sie, default 'docs'
    :return: lst, example ['../website/docs/00-Prefence','../website/docs/01-Introduction']
    """
    DOCS_DIR = os.path.join(os.pardir, 'website', docs_dir_name)
    REG_docs_sub_dir = re.compile((r'(\d\d)-*'))
    docs_sub_dir_path_lst = []
    for dir in os.listdir(DOCS_DIR):
        if REG_docs_sub_dir.match(dir):
            dir_path=os.path.join(os.pardir, 'website', docs_dir_name, dir)
            docs_sub_dir_path_lst.append(dir_path)

    return sorted(docs_sub_dir_path_lst)

def iter_notebook_paths(notebook_dir_name='notebooks'):
    """
    function outputs a list of paths of the all notebooks inside sub dirs inside the notebook dir
    :param notebook_dir_name: str, the main directory with the notebooks, default 'notebooks'
    :return: lst, example ['../notebooks/00-Prefence/00.01-Introduction.ipynb','../notebooks/01-Introduction/01.01-The-Python-REPL.ipynb']
    """
    NOTEBOOK_DIR = os.path.join(os.pardir, notebook_dir_name)
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    nb_path_lst = []
    for sub_dir_path in iter_notebook_sub_dirs_path(notebook_dir_name):
        for file in os.listdir(sub_dir_path):
            if REG_nb.match(file):
                nb_path = os.path.join(sub_dir_path, file)
                nb_path_lst.append(nb_path)

    return sorted(nb_path_lst)


def get_notebook_title(nb_file):
    nb = nbformat.read(os.path.join(NOTEBOOK_DIR, nb_file), as_version=4)
    for cell in nb.cells:
        if cell.source.startswith('#'):
            return cell.source[1:].splitlines()[0].strip()


def gen_contents(directory=None):
    for nb in iter_notebooks():
        if directory:
            nb_url = os.path.join(directory, nb)
        else:
            nb_url = nb
        chapter, section, title = REG.match(nb).groups()
        title = get_notebook_title(nb)
        if section == '00':
            if chapter in ['00', '06']:
                yield '\n### [{0}]({1})'.format(title, nb_url)
            else:
                yield '\n### [{0}. {1}]({2})'.format(int(chapter),
                                                     title, nb_url)
        else:
            yield "- [{0}]({1})".format(title, nb_url)


def print_contents(directory=None):
    print('\n'.join(gen_contents(directory)))

def main():
    lst = iter_notebook_sub_dirs_path()
    for i in lst:
        print(i)
    nb_path_lst = iter_notebook_paths()
    for nb in nb_path_lst:
        print(nb)


if __name__ == "__main__":
    main()