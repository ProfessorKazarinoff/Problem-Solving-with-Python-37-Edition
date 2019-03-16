# nb2mkdocs.py
#
# a script to turn the notebook directory into
# something ready for mkdocs to build into a static site
#
# set of steps from conversion_tools/README.md
#
## To build website:

import nb2html
import copy_images_dir
import yaml_TOC
import make_mkdocs_yaml

def main():
### Convert notebooks to html that mkdocs can read

#run main script in nb2html.py

	nb2html.main()

### Copy over all of the images from the notebooks/subdir to website/subdir

#run main script in copy_images_dir.py

	copy_images_dir.main()


### Build the TOC yaml that goes at the end of the mkdocs config file

# run main script in yaml_TOC.py

	yaml_TOC.main()

### Combine the TOC.yml file created above with the mkdocs_config file

#run the main script in make_mkdocs_yaml.py

	make_mkdocs_yaml.main()

if __name__ == "__main__":
	main()