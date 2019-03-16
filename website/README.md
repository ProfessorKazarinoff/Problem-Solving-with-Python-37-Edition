# README.md

## To build website:

cd into the conversion_tools directory

```text
$ cd conversion_tools
```

### Convert notebooks to html that mkdocs can read

run main script in nb2html.py

```text
$ python nb2html.py
```

### Copy over all of the images from the notebooks/subdir to website/subdir

run main script in copy_images_dir.py

```text
$ python copy_images_dir.py
```

### Build the TOC yaml that goes at the end of the mkdocs config file

run main script in yaml_TOC.py

```text
$ python yaml_TOC.py
```

### Combine the TOC.yml file created above with the mkdocs_config file

run the main script in make_mkdocs_yaml.py

```text
$ python make_mkdocs_yaml.py
```

### build and serve mkdocs site

cd into the website directory and activate the ```(book)``` env. Build and serve using mkdocs

```text
$ conda activate book
(book)$ cd website
(book)$ mkdocs build
(book)$ mkdocs serve
```

### post the website to github pages

```text
(book)$ mkdocs gh-deploy
```

If this does not work, ensure the current working directory is website, then

```text
git push -f origin gh-pages
```
