# LabGuide

## Introduction

LabGuide is an open-source, interactive self-learning and autograding lab. It uses Jupyter Notebook to hold the questions, and `learntools` and `suss` python packages to power the autograding and autotesting. 

#### Credits
Kaggle's learningtools https://github.com/Kaggle/learntools

## Lab0

Lab0 is provided in this open source LabGuide. The `lab0` contains the following files:
- .config.yml
- .encrypted_lab0_solution
- requirements.txt
- lab0.ipynb

You can try out LabGuide's autograding feature by following the instructions in `lab0.ipynb`.

## Setup

You can set up your LabGuide environment for `lab0` by running the `setup.sh` script using this command:
```
pip install git+https://github.com/suss-vli/labguide.git
```

### Setup for Courses

**<span style="color:red">IMPT!</span> You will be required to have permission and be authenticated before having access to the LabGuide of the courses.**

To get all the labs of the course and set up the LabGuide environment, you can use the `get_course.sh` command:
```
./dev/get_course.sh <course>
```
For example:
```
./dev/get_course.sh ict133
```

  