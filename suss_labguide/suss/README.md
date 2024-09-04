# SUSS 

The python package that powers interactive study guide. Work closely with kaggle's learntools.


## Get started

NOTE: [github package](https://docs.github.com/en/packages) don't work with python packages

```bash
git clone https://github.com/suss-vli/suss.git
cd suss
python3 -m pip install --upgrade build
python3 -m build
```

## if you are developing iLabGuide

you can just run the following command to upgrade this package

```
pip3 install ../suss --upgrade
```

## Installing

```bash
pip3 install <path-to-suss>
```

## Use pygount 

```
python3 -m venv venv; source venv/bin/activate
pygount --format=summary --out=pygount_17july.txt . 
```

## Usage

```python
from suss.ict133.lab1 import *
```
                   
## Friday discussion with Jane

We need to write in lab0 about the constraints when `.check()` is uncommented in the multiple cells. And when we call `x.get_source_code` or `x.create_object_from_source_code`, it will generate the an error `____ is not callable`. 

- The solution is comment out all the `.check()` code.
- We need to capture this error within `x.get_source_code` and `x.create_object_from_source_code`  and print out that all `.check()` must be commented out. 


## ✅ Everyone should read this first! - Updates to `suss` check

 For ICT133 and ICT162, you will see a difference where we use the `FunctionProblem` and directly access the student's written function for the answer. and the format for our code is slightly different where instead of writing our customised check in `check`, it is under `check_testbook`: https://github.com/suss-vli/suss/blob/main/src/suss/ict133/lab1_questions/q1.py#L28

From ICT233 onwards, we begin using `get_source_code` : https://github.com/suss-vli/suss/blob/bb2e8593263e7321b283f77bdcc9cc299de24142/src/suss/ict233/lab1_questions/q1.py#L42

and we write our checks within the `check` function. `get_source_code` allows us to get the exact codes written by students to check.
With every `get_source_code`, a `test_for_none_xxx` must accompany it. This is to navigate the issue of difference in the cell number to `get_source_code` from due to missing cells, additional cells.

There's also a more structured format from ict233 onwards where there is:

`produce_expected()`
`_var`
`_expected`
`_test_cases`
`check()`

The standardised format is meant to help us to eventually use AI to generate new labs or checks for us and the instructors.
