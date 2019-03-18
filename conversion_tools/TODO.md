# TODO

## pdf

 - [ ] Refactor template into different files for packages, preable, etc
 - [ ] Take out empty cell at the bottom of each section when conversion to web and pdf. See [https://nbconvert.readthedocs.io/en/stable/api/preprocessors.html#nbconvert.preprocessors.RegexRemovePreprocessor](https://nbconvert.readthedocs.io/en/stable/api/preprocessors.html#nbconvert.preprocessors.RegexRemovePreprocessor) and try ```jupyter nbconvert --RegexRemovePreprocessor.patterns="['\s*\Z']" mynotebook.ipynb```
 