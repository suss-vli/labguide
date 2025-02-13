This is documentation for developers to refer when working on developing labguides.

## Table of contents
  - [Introduction](#introduction)
    - [Credits](#credits)
    - [Features](#features)
    - [Todo](#todo)
  - [Getting started in development](#getting-started-in-development)
    - [Names and Terms](#names-and-terms)
    - [Reserved phrases and keywords](#reserved-phrases-and-keywords)
    - [Import the labs and questions](#import-the-labs-and-questions)
    - [Developing `suss`](#developing-suss)
    - [Testing the answer](#testing-the-answer)
    - [Clean up for students](#clean-up-for-students)
  - [Config and scripts](#config-and-scripts)
    - [Relating to config](#relating-to-config)
    - [Scripts in `dev` folder](#scripts-in-dev-folder)
    - [CI/CD](#cicd)
      - [Auto-Encryption](#auto-encryption)
  - [Known issues](#known-issues)
    - [Type checking in learner's feedback](#type-checking-in-learners-feedback)
  - [Regarding learntools](#regarding-learntools)
    - [Multiple patches](#multiple-patches)
  - [Troubleshooting](#troubleshooting)
    - [Deployment stage issue: `token must be in bytes`](#deployment-stage-issue-token-must-be-in-bytes-for-hints-and-solutions)
    - [ImportError: cannot import name 'ml\_insights' from partially initialized module 'learntools'](#importerror-cannot-import-name-ml_insights-from-partially-initialized-module-learntools)
    - [Use `jupyter notebook`](#use-jupyter-notebook)
    - [Install the dependencies](#install-the-dependencies)
    - [If you are facing `There is no Pip installer available in the selected environment`](#if-you-are-facing-there-is-no-pip-installer-available-in-the-selected-environment)
  - [Notes on ICT162](#notes-on-ict162)
    - [Required to install \`python-tk\`\`](#required-to-install-python-tk)
    - [There are three junior accounts at lab3 q1a, q2b, q2c](#there-are-three-junior-accounts-at-lab3-q1a-q2b-q2c)
  - [Setting exam questions in a GPT/AI era](#setting-exam-questions-in-a-gptai-era)
  - [Added inspection.py](#added-inspectionpy)

---

## Introduction

This is the interactive lab guide. It includes jupyter notebooks as questions. It uses `learntools` and `suss` python packages to power the autograding and autotesting. 

- `lab1-answer.ipynb` contains all the answer and test code for
- `lab1-question.ipynb` is what the student will receive.


### Credits
Kaggle's learningtools https://github.com/Kaggle/learntools
's testbooks 
pytest
  

### Features

1. Interactive learning tools via Kaggle's `learntools`
2. Batch autograding via `pytest` and `testbook` for students and instructors
3. [WIP] Ship test code and solution via packages. Hide the solution behind packaging.
4. Integrate on Jupyter Notebook
5. [WIP] Integrate with Git and Github classroom 
6. [WIP] Integrate with videos of panopto.com/
7. [WIP] Automate generation of autograding.py or __init__.py
8. Support Latex in jupyter notebook

### Todo
- We should run through all the answers into ChatGPT. Compare the answers and use the more optimal answer. 
  
- We should run through all questions into ChatGPT. Check area where the questions can be improved. 

---

## Getting started in development

```
git clone https://github.com/suss-vli/labguide
git clone https://github.com/suss-vli/suss
git clone https://github.com/suss-vli/learntools
cd labguide
python -m venv venv
source venv/bin/activate
pip3 install ../suss
pip3 install ../learntools 
pip3 install -r requirements.txt 
```

You should be ready to go. Remember to select the correct kernel inside the vscode jupyter extension. 

If you are running the notebook using vscode, you should also run `restart` so that the new python package is loaded. 

### Names and Terms

Each assignment is filed under a module e.g. `ict133` or `ict162`

1. Each assignment is called lab. e.g. `lab0`, `lab1`

2. Each question is called exercise. `q1`, `q2`, `q3`. 

3. `lab0` is a starter lab that demostrates on how to use the library `iLabGuide`. WIP

### Reserved phrases and keywords

When creating new labs, take note of the following phrases and keywords that will be picked up by `qc`:
- ` write your answer`
- `pass`


### Import the labs and questions

For ICT133

```
from learntools.core import binder; 
binder.bind(globals())
from suss.ict133.lab1 import *
```

For ICT162
```
from learntools.core import binder; 
binder.bind(globals())
from suss.ict162.lab1 import *
```

### Developing `suss`

You can run the following to upgrade `suss` package to test.

```
pip3 install ../suss --upgrade
```

### Testing the answer 
> The `lab1-answer.ipynb` is for development of each lab guide. The final copy of autogradable lab comes from this answer copy. 

1. Open the lab1-answer.ipynb in your favourite jupyter editor e.g. jupyter notebook or vscode
2. Click `Run all` 

### Clean up for students

This will remove all directories except for the .ipynb files in preparation for production:
```
chmod 700 clean.sh
./clean.sh
```
---
## Config and scripts

### Relating to config

config.yml is what LS team will use for development.
For production & testing, please use `config_<module_name>.yml` e.g config_ict133.yml. For instance,the person deploying should `mv config_ict133.yml config.yml`

`.instructor_config.yml`: provides access to hints and solutions in ilabguide

This includes a list of current semester's instructors emails. Each course has 1 `.instructor_config.yml` saved within the `.encrypted_<course>_solution`. Note: instructor's email is case sensitive. It should be all in lowercase.

### Scripts in `dev` folder

- dev/production.py - check if set up is ok
- dev/generate_questions_ipynb - produce the questions.ipynb
- dev/toggle- comment/uncomment the hint(), solution(), check()
- dev/lock - lock up the markdown cells 
- dev/setup.sh - install learntools, suss, and other dependencies
- dev/setup_jupyter.sh - install the dependencies needed for jupyter servers
- dev/clean.sh - remove everything except for the questions.ipynbs
- dev/inspect - add in `iLabGuide` to generate `incorrect` answers for checking the incorrect messages
- dev/qc - scan through the layout and format of ipynb

### CI/CD

#### Auto-Encryption
`auto-encrypt` is a Github Action workflow using our private `suss-cli` to auto-encrypt any external hints and solutions in a single `.unencrypted_<course>_solution` folder.

You can copy the file into your `.github/workflows/` folder for the labguide.
If you modify the workflow to use your own encrpytion workflow using `cryptography`, update the `.config.yml` file with your `encrypt_key` and `encrypt_marker` for your solutions to be displayed in the labguide.

Note: If you have changes in two or more `.unencrypted_<course>_solution` folders for multiple courses, `auto-encrypt` will fail to work. You need to push changes for a single folder at a time.

`auto-encrypt` does the following:
1. Detect any changes in the latest commit pushed in any of the `.unencrypted_<course>_solution` folder
2. Auto-encrypt all files in the `.unencrypted_<course>_solution` folder and save the encrypted files into `.encrypted_<course>_solution` folder
3. Git commit and push the encrypted folder into repo

---

## Known issues

### Type checking in learner's feedback

code:

```python
    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                actual = fn()
                assert fn()==expected, ("Expected return value of `{}({})` given `input={}`, but got `{}({})` instead.").format(expected, type(expected).__name__, args, actual, type(actual).__name__)
                    
```
Source code is [here](https://github.com/suss-vli/iLabGuide/blob/bf5c0792e5b8d060990d2a9c7ec3c99ef2b96cdf/iLabGuide/ict133/lab1.py#L41) 

---

## Regarding learntools

src: https://github.com/Kaggle/learntools/tree/master/learntools

`learntools.core` contains the basic elements of exercise checking, shared across all Learn micro-courses and exercises.

The course-specific directories subclass ProblemViews from `learntools.core`. Examples of types of ProblemViews are `CodingProblem`, `EqualityCheckProblem` and `ThoughtExperiment`.

The `ProblemView` provides an interface that wraps a `learntools.core.Problem`. The interface it provides generally includes `hint()`, `check()` and `solution()` methods. The behavior of these is determined by the values for `var`, `_hint` and `_solution` in the checking code written by the course author.

### Multiple patches

https://stackoverflow.com/questions/16723591/mock-patch-multiple

You can patch multiple statements in one go. 

---

## Troubleshooting

### Deployment stage issue: `token must be in bytes` for hints and solutions

This is due to incorrect library versions or incorrect `requirements.txt` file. Check the `requirements.txt` file to ensure it has the correct libraries and remove the version numbers.

When testing in Vocareum while resolving this issue, it requires `sudo` to pip install the libraries. Run in the terminal of the jupyter lab:
`sudo pip3 install -r requirements.txt`

### ImportError: cannot import name 'ml_insights' from partially initialized module 'learntools'

```
~/opt/anaconda3/lib/python3.9/site-packages/learntools/__init__.py in <module>
----> 1 from . import core, data_viz_to_coder, deep_learning, embeddings, gans, \
      2               machine_learning, ml_explainability, ml_insights, ml_intermediate, python, \
      3               sql
      4 
      5 __version__ = '0.3.4'

ImportError: cannot import name 'ml_insights' from partially initialized module 'learntools' (most likely due to a circular import) (/Users/ytbryan/opt/anaconda3/lib/python3.9/site-packages/learntools/__init__.py)

```
The problem is because one is not using the learntools that is residing in your localhost. This learntools may be a remote one.  
The solution is to delete the venv and rerun the following commands:

```
python -m venv venv
source venv/bin/activate
pip3 install ../suss
pip3 install ../learntools 
pip3 install -r requirements.txt 
pip3 install ipykernel
python3 -m ipykernel install --user --name=venv
```

### Use `jupyter notebook`

1. If vscode is not working fully for you, you should try `jupyter notebook` to run the labguide.

```
jupyter notebook
```
Then follow the instruction by visiting the jupyter notebook link on your browser.

### Install the dependencies

2. If you don't have the dependencies of `learntools` and `iLabGuide`, you can download them here

```
python -m venv venv

source ./venv/bin/activate 

pip3 install -r requirements.txt
```
### If you are facing `There is no Pip installer available in the selected environment`

https://stackoverflow.com/questions/50993566/vscode-there-is-no-pip-installer-available-in-the-selected-environment

---
## Notes on python GUI questions

### Required to install `python-tk`

```
brew install python-tk
```

Note that if you use `pyenv`, then tkinter does not seem to work. The solution is to remove `pyenv` and use brew to install python instead. 

Windows users will not be able to make it work properly. Alternatively, use an Ubuntu/Linux GUI container to work on the GUI question. 

See notes in [ICT162](https://github.com/suss-vli/labguide_ict162/blob/main/CHANGELOG.md#notes-from-before-2025).

---

## Setting exam questions in a GPT/AI era

After chatting with some instructors, this is a list of considerations when setting exam questions. 

1.  Request students to submit their references in their submission. Enforce reference checking using `references.py`. For each reference link, each student should include the line or page that is relevant to the answer. 

2. Set thinking questions that ChatGPT or AI has difficulty giving a correct answer. Or include questions that require fine-tuning the answer i.e student needs to go to ChatGPT multiple times. 

3. Consider lowering your weightage for less important components.  

4. Include screensharing/video/demo as part of the solution. Give relevant marks for such submission. 

5.  Finally, set questions and require students to submit their prompts. This is doing meta-testing on how to be effective in asking ChatGPT to derive answers.

If you have more suggestions, please email me at bryanlimyt@suss.edu.sg

## Added inspection.py

Change the name to `inspection.py` because inspect.py clash with another inspect within python framework. These will generate `-inspection.ipynb` lab1.ipynb-inspection.ipynb
```
python3 ./dev/inspection.py ./lab1.ipynb ./lab2.ipynb ./lab3.ipynb ./lab4.ipynb ./lab5.ipynb ./lab6.ipynb
```
