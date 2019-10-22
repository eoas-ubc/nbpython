---
title: 'Jupyter notebooks as quiz question sourcefiles'
---

## Background

In the worst case scenario, my workflow for posting a quiz on canvas used to involve four separate source documents:

1. A docx file containing quiz questions with answers/explanations. 
1. A separate docx file with the answers stripped that was posted for students to work from
   prior to enetering their answers on canvas.

1. A jupyter python notebook with the numeric answers worked out

1. A canvas quiz with the question entered via the canvas web interface

Fortunately, three of these documents are unnecessary.  My current workflow is:

1. Write a [jupyter notebook](https://jupyter.org/) with the quiz questions and answers. This is a mix of markdown cells for the narative/images, and python cells for the actual calculations.  Use
   jupyter cell metadata to tag each cell as a question or answer, along with the question number and, if
   multiple choice, the correct answer.

1. Save the notebook as a python file using [jupytext](https://github.com/mwouts/jupytext)  (This is automatic, since the jupytext plugin overrides jupyter's `content_mananger_class`).

1. Commit to git

1. Generate the student version of the quiz by filtering out the answer cells and use `jupyter nbconvert` to produce a paginated pdf with headers.

1. (to be done) Generate the canvas version of the quiz using the [r-exams](http://www.r-exams.org/)
canvas qti writer.

For classes that involve student programming, we've adopted DSCI 100's use of  [nbgrader](https://nbgrader.readthedocs.io/en/stable/), which is as you know is just a (much) more elaborate version of the workflow above.

## Example




## Approach

here is the approach and now this and this and this

and this




