# conversion_tools/README.md

## To build website:

## Create the conda environment book37-website

```text
cd conversion_tools
conda env -f environment-website.yml
conda activate book37-website
(book37-website)
```

## Convert notebooks to html that mkdocs can read, copy images and build mkdocs.yml toc

Activate the book37-website env and 

run the main script in nb2mkdocs.py

```text
conda activate book37-website

(book37-website) python nb2mkdocs.py
```

### build and serve mkdocs site

cd into the website directory and activate the ```(book37-website)``` env. Build and serve using mkdocs.

```text
$ conda activate book37-env
(book37-website)$ cd website
(book37-website)$ mkdocs build
(book37-website)$ mkdocs serve
```

### post the website to github pages

```text
(book)$ mkdocs gh-deploy
```

On windows, this didn't work initially, but the commands below to change the credential helper

```
git config --global credential.helper wincred
```

And then run with the force option seemed to work.

```
mkdocs gh-deploy --force
```

If this does not work, ensure the current working directory is website, then

```text
git push -f origin gh-pages
```
