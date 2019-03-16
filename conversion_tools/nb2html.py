
"""
This module provides functions and a script to turn a directory full of
jupyter notebooks into a directory full of .md files that can be read by mkdocs.
This script should be run after the make TOC script is run. After the make TOC script is run,
the mkdocs.yml file appended and this script run, mkdocs can be run to build the site.
"""
import nbformat
from nbconvert import HTMLExporter
from nbconvert.writers import FilesWriter
import os
import re
import shutil
from nb_list_tools import iter_notebook_sub_dirs_path, iter_docs_sub_dirs_path


def clean_docs_dir(docs_dir='docs'):
    """
    This function cleans out the docs dir of all sub dirs that contain regular .md files. The figures, index and
    stylesheets directories will stay.
    This function erases the subdirectories and all files inside of subdirectories inside the docs dir
    :param docs_dir: str, directory where docs subdirs are located. docs subdirs contain .md files to build site
    :return:
    """
    docs_subdir_path_lst = iter_docs_sub_dirs_path(docs_dir)
    print(docs_subdir_path_lst)
    for docs_subdir_path in docs_subdir_path_lst:
        try:
            shutil.rmtree(docs_subdir_path)
            print('Erased: {}'.format(docs_subdir_path))
        except:
            print('{} does not exist'.format(docs_subdir_path))
    print('Complete')
    docs_subdir_path_lst = iter_docs_sub_dirs_path(docs_dir)
    print('Remaining doc subdirs are {}'.format(docs_subdir_path_lst))

def convertNotebooktoHTML(notebookPath, outfilePath='nb_out', template='md_not_converted'):
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    notebook_basename = os.path.basename(notebookPath)
    if REG_nb.match(notebook_basename):
        with open(notebookPath) as fh:
            nbnode = nbformat.read(notebookPath, as_version=4)

        exporter = HTMLExporter()
        exporter.template_file = template  # leaves markdown not converted, converts input and output cells
        exporter.file_extension = '.md'
        body, resources = exporter.from_notebook_node(nbnode)
        writer = FilesWriter()
        writer.write(body, resources, notebook_name=outfilePath)  # will end up with .html extension


def convertNotebookDir(notebookdir='notebooks', docsdir='docs'):
    REG_nb_dir = re.compile((r'(\d\d)-*'))
    REG_nb = re.compile(r'(\d\d)\.(\d\d)-(.*)\.ipynb')
    f = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(os.pardir, notebookdir)):
        f.extend(dirnames)
        for dirname in dirnames:
            print(dirname)
            if REG_nb_dir.match(dirname):
                print(dirname)
                if not os.path.exists(os.path.join(os.pardir, 'website', docsdir, dirname)):
                    os.mkdir(os.path.join(os.pardir, 'website', docsdir, dirname))
                nbnames = os.listdir(os.path.join(os.pardir, 'notebooks', dirname))
                for nbname in nbnames:
                    print(nbname)
                    if REG_nb.match(nbname):
                        nbpath = os.path.join(os.pardir, 'notebooks', dirname, nbname)
                        root, ext = os.path.splitext(nbname)
                        extension = ''
                        mdname = os.path.join(root + extension)
                        mdpath = os.path.join(os.pardir, 'website', docsdir, dirname, mdname)
                        convertNotebooktoHTML(nbpath, mdpath)
                        print("Converted: {} to {}".format(str(nbpath),str(mdpath)))
                        #if mdpath.endswith(.html) or mdpath.endswith

def main():
    clean_docs_dir()
    convertNotebookDir('notebooks','docs')


if __name__ == "__main__":
    main()
