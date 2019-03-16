#!/usr/bin/env python

"""
This module contains functions and a main script to construct a mkdocs.yml file
Two files are combined to make this file:
1. TOC.yml in the conversion_tools/ directory
2. mkdocs_config.yml in the webiste/ directory TOC yaml file for MkDocs
The combined file is named:
mkdocs.yml in the website/ directory

book/
    conversion_tools/
        TOC.yml
    website/
        mkdocs_config.yml
        mkdocs.yml

"""

import nbformat
import os
import re


def combine_yaml(infile1=os.path.join(os.pardir, 'website', 'mkdocs_config.yml'),
                 infile2=os.path.join(os.pardir, 'conversion_tools', 'TOC.yml'),
                 outfile_name=os.path.join(os.pardir, 'website', 'mkdocs.yml')):
    # combine the files
    filenames = [infile2, infile1]
    with open(outfile_name, "w") as outfile:
        for fname in filenames:
            with open(fname, "r") as infile:
                outfile.write(infile.read())


def main():
    config_file = os.path.join(os.pardir, 'conversion_tools', 'TOC.yml')
    TOC_file = os.path.join(os.pardir, 'website', 'mkdocs_config.yml')
    mkdocs_yaml_file = os.path.join(os.pardir, 'website', 'mkdocs.yml')
    combine_yaml(config_file, TOC_file, mkdocs_yaml_file)


if __name__ == "__main__":
    main()
