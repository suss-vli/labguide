# LabGuide

## Introduction

LabGuide is an open-source, interactive self-learning and autograding lab. It uses Jupyter Notebook to hold the questions, and `learntools` and `suss` python packages to power the autograding and autotesting.

**Note: You will be required to have permission and be authenticated before having access to the LabGuide of the courses.**

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

Install LabGuide package
```
pip install git+https://github.com/suss-vli/labguide.git
```

### Setup after Installation

Create a folder to store all the labs. Navigate to that folder and run the setup command.
```
cd <lab directory>
labguide setup
```
For example:
```
cd labs 
labguide setup
```

The setup will create a `lab0/` folder in your current working directory, and includes `lab0.ipynb` for you to try out.

### Setup for Courses

**<span style="color:red">IMPT!</span> You will be required to have permission and be authenticated before having access to the LabGuide of the courses.**

1. Navigate to the lab folder.

 
```
cd <lab directory>
```

2. To get the labs of the course and set up the LabGuide environment, you can use the command:

 
```
labguide get <course>
```
For example:
```
labguide get ict133
```
This command will `git clone` the course's labs into the `<course>/` folder.

3. Run the `setup` command:

 
```
labguide setup <course>
```
For example:
```
labguide setup ict133
```
This command will install all the dependencies required for the labs.

4. Your labs are now ready for you!


## Credits

A special shoutout to our amazing interns who have played a part in making LabGuide work:

- Bryan Chew @bchewzy
- Joey Tan @jeezusplays
