# smart_title_case_bib

I made this simple Python script for a quick fix on the common issues in latex bibtex file.


Just run
```
python bib_titlecase.py input.bib
```
it will create a processed file ```input_fixed.bib```


What this script does:

1. Change the words in paper titles and journals into smart titlecase. (i.e. capitalize all words, except for articles such as "a", "an", etc.)
2. Put curly brackets around title, so that they render correctly into PDF.
3. Remove "and others" (if appeared) from the author list.

Note: this may mess up some words, such as incorrectly changing "fMRI" into "FMRI". So you need to double check the bibtex file, and additional edits if necessary.

