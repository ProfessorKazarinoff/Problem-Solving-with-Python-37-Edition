# TODO

## pdf

 - [x] Refactor template into different files for packages, preable, etc
 - [x] Take out empty cell at the bottom of each section when conversion to web and pdf. See [https://nbconvert.readthedocs.io/en/stable/api/preprocessors.html#nbconvert.preprocessors.RegexRemovePreprocessor](https://nbconvert.readthedocs.io/en/stable/api/preprocessors.html#nbconvert.preprocessors.RegexRemovePreprocessor) and try ```jupyter nbconvert --RegexRemovePreprocessor.patterns="['\s*\Z']" mynotebook.ipynb```
 
 ## website
 
  - [ ] Make website build a 1 or 2 step process instead of calling three different scripts
  - [ ] Convert mkdocs pages in .yml to nav in .yml
 