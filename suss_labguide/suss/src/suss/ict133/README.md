# ICT 133 Interactive Guide

## Features

1. Interactive learning tools via Kaggle's `learntools`
2. Batch autograding via `pytest` and `testbook` for students and instructors
3. [WIP] Ship test code and solution via packages. Hide the solution behind packaging.
4. Integrate on Jupyter Notebook
5. Integrate with Git and Github classroom
6. [WIP] Integrate with videos of panopto.com/
7. [WIP] Automate generation of autograding.py or __init__.py
8. Support Latex in jupyter notebook

---

src:https://github.com/Kaggle/learntools/tree/master/learntools

`learntools.core` contains the basic elements of exercise checking, shared across all Learn micro-courses and exercises.

The course-specific directories subclass ProblemViews from `learntools.core`. Examples of types of ProblemViews are `CodingProblem`, `EqualityCheckProblem` and `ThoughtExperiment`.

The `ProblemView` provides an interface that wraps a `learntools.core.Problem`. The interface it provides generally includes `hint()`, `check()` and `solution()` methods. The behavior of these is determined by the values for `var`, `_hint` and `_solution` in the checking code written by the course author.



---
# Some thoughts about autograding and autotesting

Autograding is the act of automating grading in order to achieve graded work. These graded work comprises of grades, graded assignnment or exam, feedback.

Autotesting is a way for 
instructors to run batch testing code to do autograding. 

The learning tools by kaggle are hint(), check(), solution()

There should be a way to automatically generate these learning tools from the tests that the instructors write.
    