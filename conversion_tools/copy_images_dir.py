
# coding: utf-8

# ### A notebook to figure out how to copy over the images directory from notebooks to website docs

# In[1]:


import os
import shutil
from os.path import join
import re


# In[2]:


def copy_figures_dir(nb_dir_name='notebooks',docs_dir_name='docs'):
    nb_dir = join(os.pardir,nb_dir_name)
    docs_dir = join(os.pardir,'website', docs_dir_name)
    scr = join(nb_dir,'figures')
    dst = join(docs_dir,'figures')
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(scr,dst)


# In[3]:


def copy_image_dirs(notebook_dir_name='notebooks', docs_dir_name='docs'):
    """
    a function to copy the image directory and images from notebooks directory to website/docs directory
    website/docs/subdir/images must not exhist for the copy to work
    """
    nb_dir = os.path.join(os.pardir, notebook_dir_name)
    docs_dir = os.path.join(os.pardir,'website',docs_dir_name)
    REG_nb_dir = re.compile((r'(\d\d)-*'))
    
    for dir in os.listdir(nb_dir):
        if REG_nb_dir.match(dir):
            if os.path.exists(join(nb_dir, dir, 'images')):
                scr = join(nb_dir, dir, 'images')
                dst = join(docs_dir, dir, 'images')
                if os.path.exists(dst):
                    shutil.rmtree(dst)
                try:
                    shutil.copytree(scr,dst)
                    print("coppied the directory: {}".format(str(scr)))
                except:
                    print("can't copy the directory: {}".format(str(scr)))
            else:
                print("no images folder in directory: {}".format(str(dir)))


def main():
    copy_figures_dir()
    copy_image_dirs()

if __name__ == "__main__":
    main()
