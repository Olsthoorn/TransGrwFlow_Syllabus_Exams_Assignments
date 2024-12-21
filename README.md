# How to generate the documentation of the full transient groundwater course on READTHEDOCS?

First see the directory `SyllabusUptoDate` in the current folder. It has the file `TransientGroundwater.lyx`, which constains the entire Lyx syllabus.

From within Lyx, export the `TransientGroundwater.text` file as a basis for generating the rst files required bt Sphinx / readthedocs.

Also, the the directory `SyllabusUptoDate` holds the other lyx files required for the final documentation on `Readthedocs`:

`examsfrom2006.lyx',
`exams from 2006+answers.lyx`,
`old_assingments.lyx`,


Also, from whithin lyx expert their tex files.

These tex files are not yet suitable for `sphinx` and need some corrections, like replacing figure nubmers to prevent duplicated figure numbers in cases where the lyx file has more than one figure in a single float.

There are three python files to make the conversion to rst.
To make the conversion change folger from to `SyllabusUptoDate` to `SyllabusUptoDate/../docs/source` to find three
python files to make the conversion from `tex` to `rst`, while also making the corrections to the tex files:

`old_exams_tex_to_rst.py`
`old_assignments_tex_to_rst.py`,
`old_exams_tex_to_rst.py`

The conversions are done with the program `pandoc` within these `.py' files.
The resulting `.rst` files are placed in this directory.

The assignments together with the file `Techniques.ipynb` are also given as notebooks in the `project/docs/source/notebooks` directory. These notebooks should be inserted in the documentation directly.

For an extended HowTo file see `Project/docs/HowTo.md`.

@TO 2024-12-21

