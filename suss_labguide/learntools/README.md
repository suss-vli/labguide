# learntools 

This is the actual Kaggle's learntools minus the `ml_insights` that was causing issue


## Get started

NOTE: [github package](https://docs.github.com/en/packages) don't work with python packages

```bash
git clone https://github.com/suss-vli/learntools.git
cd suss
python3 -m pip install --upgrade build
python3 -m build
```


## Installing

```bash
pip3 install <path-to-learntools>
```
      

## Usage

```python
from learntools.core import binder; 
binder.bind(globals())
```

## CHANGELOG

- analytics.py is required to produce .csv for kibana 
- ProblemX is a class to enable `external hints`. 
- hide_solution_before_count allows students to not get solution instantly. We hide the solution for them to discover it. Increase their ability to try before getting the free solution.
 
## Naming convention and default values

ProblemX ensures that there is a naming convention e.g. `ict162/lab1/q1/`. There will be `hint`, `solution`, `testcases` and `check.py`. 

The default value of these external hints assumes to be the same directory as the notebooks
