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

### Initial Setup

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


## Implementing Custom LabGuide Plugins

Customize your labs to suit your teaching style and students' learning better! Create your own `labguide` plugin using Python and enable it just for your class.


### Implementation

Create a Python script for your plugin. The script should be in the `.plugins` folder.

Refer to `/.plugins/hello.py` for a sample plugin.


### Configuration

Navigate to the specific course folder, and locate the `.config.yml` file.

For example, the `lab0/` folder contains:

- **.config.yml (Open this file)**
- .encrypted_lab0_solution
- requirements.txt
- lab0.ipynb

### Edit .config.yml

Add this section to the end of the .config.yml file.

```
### Code above not shown ###

plugins:
  - hello.py
  - another_plugin.py
  - ...
```
**Note: Take note of the indentation, ensure that it is consistent throughout.**

Comment the line to turn off a specific plugin.
```
### Code above not shown ###

plugins:
  - hello.py
  - another_plugin.py
  # - turnoff_plugin.py
```

## Credits

A special shoutout to our amazing interns who have played a part in making LabGuide work:

- Bryan Chew @bchewzy
- Joey Tan @jeezusplays
