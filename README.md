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

## Installation

```
pip install git+https://github.com/suss-vli/labguide.git
```

### Setup after Installation

After you have `pip install` the labguide package, run the command below for the initial setup:
```
labguide setup
```

The setup will create a `labs/` folder in your current working directory, and include `lab0/` for you to try out.

### Setup for Courses

**<span style="color:red">IMPT!</span> You will be required to have permission and be authenticated before having access to the LabGuide of the courses.**

1. To get the labs of the course and set up the LabGuide environment, you can use the command:
```
labguide get <course>
```
For example:
```
labguide get ict133
```
This will `git clone` the course's labs into `labs/<course>` folder.

2. Run the `setup` command:
```
labguide setup <course>
```
3. Your labs are now ready for you!


### Credits

A special shoutout to our amazing interns who have played a part in making LabGuide work:

- Bryan Chew @bchewzy
- Joey Tan @jeezusplays
