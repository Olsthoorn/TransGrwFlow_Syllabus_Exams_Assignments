# How to geenrated the documentation??

The documenation consists of the

*. Sysllabus
*. The old exams (2006-2022)
*. The old exams + answer
*. Previous assigments
*. Previous assigments worked out
*. Techniues (useful python techniques

The project directory is as follows

``
ReadTheDocsSyllabus
    docs
        HowTo.md   # This HowTo markdown file.
        make.bat   # Generated, guess it's for Windows
        Makefile
        source
            __pycache__  # generated automatcally
            _statuc      # generated automatcally
            _templates   # generated automatcally
            .vscode      # generated automatcally when working with vscode
            notebooks    # The notebooks with the workout of the individual assignments
                         # Softlink to the original directory, ../../SyllabusUptoDate/notebooks
                AssWithAnswers.ipynb  # Intro, and top title of the workout of the old assignments
                AssJan2016.ipynb      # workout of the asisgnment of Jan 2016
                AssJan2017.ipynb      # workout of the asisgnment of Jan 2016
                AssJan2019.ipynb      # workout of the asisgnment of Jan 2017
                AssJan2020.ipynb      # workout of the asisgnment of Jan 2020
                AssJan2021.ipynb      # workout of the asisgnment of Jan 2021
                AssJan2022.ipynb      # workout of the asisgnment of Jan 2022
                Techniques.ipynb      # useful Pyhon techniques
            pictures  # softlink to the original directory ../../SyllabusUptoDate/pictures
                all the pictures, about 210 in total

            confpy                  # generated automatcally by sphinx-quickstart and edited to reflect the current project
            index.rst               # TOC tree for the current project (generated and then adapted)
            rerquirements.txt       # Required by Readthedocs

            syllabys_tex_to_rst.py          # Run this to prepare the exported tex file to the rst file in the source directory
            old_exams_tex_to_rst.py         # Run  this to prepare the exporeted two tex files to the two rst source file for the old exams (with and without answers)
            old_assignments_tex_to_rst.py   # Run this to convert the exported tex file with the old assigments to the rst file in the source directory. 

            TransientGroundwater.rst        # The rst file of the syllabus to build the html from
            exams_from_2006.rst             # The rst file of the old exams to build the html from
            exams_from_2006+answers.rst     # The rst file of the old exams with answers to build the old exams source fle from
            old_assignments.rst             # The rst file of the old assignments to build the source file from

            TransientGroundwater.bib

        build
            doctrees
                nbsphinx  # generated in the build process
                    notebooks # generated in the build process
                    # all the pictures automatically renamed.
                norebooks # generated in the build process
            html #The built html documentation. Start with clicking on index.html
                index.html # start file, click this to start the documentation in the browser.
            # more html files

    SyllabusUptoDate
        notebooks
            # The original notebooks in which the old assignments are worked out one by one.
        Other
            pictures                                  # soflink to the original pictures ../SyllabusUptoDate/pictures
            BarometerDampingDelay.lyx                 # Explains barometer effect
            Hanush_power_series.lyx                   # Explains Hantush power series
            log_normal_pdf_for_sand_sieve_curves.lyx  # Explains nog-normal distribution
        TransientGroundwater.bib

        TransientGroundwater.lyx     # Original LyX file of the Syllabus
        TransientGroundwater.tex     # Exported from LyX to pdfltex (tex)
        TransientGroundwater.pdf     # Genrated and saved pdf file of the Syllabus

        exams_from_2006+answers.lyx  # Original LyX file of the old exams with their answers
        exams_from_2006+answers.pdf  # Generated pdf fle of the old exams with answers
        exams_from_2006+answers.tex  # Exported from LyX to pdflatex (tex)

        exams_from_2006.lyx   # Original LyX file of the old exams without answers
        exams_from_2006.pdf   # Generated pdf fle of the old exams without answers
        exams_from_2006.tex   # Exported from LyX to pdflatex (tex)

        old_assignments.lyx   # Original LyX file of the old exams without workout
        old_assignments.pdf   # Generated pdf fle of the old exams without workout
        old_assignments.tex   # Exported from LyX to pdflatex (tex)
    ``


    The original documentation in the directory SyllabusUptoDate is in its .LyX files.

    After any of the LyX files has been changed save it and export from LyX to pdflatex, yielding the tex file of the same name.

    The notebooks, one as an intro, one for useful Python techniques and the others each for one assignment if a given course year
    may be updated in jupyter, Ipython or rather in vscode. No export needs to be done.

    The from the docs/source directory run each of the .py files (except conf.py) ton convert the tex files in the SyllabusUptoDate directory
    to the required restructured text source files (.rst) from which the documentation will be built.

    When done, move up to the docs directory
    and issue the commands

    make clean  # this may be omitted of one file was edited as the build process with see it. Just to make sure you get a complete new build, you may use it.
    make html  # generated the html files

    finally:
    cd to the build/html directory and click the
    index.html file to start up the documentation in the browser.


    Theo Olsthoorn
    July 4, 2022