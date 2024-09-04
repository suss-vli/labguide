from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question3A(FunctionProblem):
    _var = 'question3a'    
    _test_cases = [
        ({'C': ['Clam Chowder', 50], 'M': ['Mushroom', 45], 'T': ['Tomato', 40], 'P': ['Pumpkin', 50], 'O': ['Oxtail', 10]})
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): 
        for expected in self._test_cases: 
            out = fn()
            x.grading(("soups.txt", expected, out))

    def check(self, fn):
        self.check_testbook(fn)
class Question3B(FunctionProblem):
    _var="question3b"
    _test_cases = [
        (['1', 'M', '24'], """Soup type      Qty
Oxtail         10
Tomato         40
Mushroom       45
Clam Chowder   50
Pumpkin        50
[['Clam Chowder', 50], ['Mushroom', 21], ['Tomato', 40], ['Pumpkin', 50], ['Oxtail', 10]]\n"""),
(['2', 'c', '10'], """Maximum number of servings = 50
[['Clam Chowder', 50], ['Mushroom', 45], ['Tomato', 40], ['Pumpkin', 50], ['Oxtail', 10]]\n""" ),
(['3'], "[['Clam Chowder', 50], ['Mushroom', 45], ['Tomato', 40], ['Pumpkin', 50], ['Oxtail', 10]]\n")
]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)            

Question3 = MultipartProblem(
    Question3A,
    Question3B
)