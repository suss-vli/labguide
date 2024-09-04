from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4(FunctionProblem):
    _var="question4"
    _test_cases = [
        ("""Dice Occurrence
1     0
2     0
3     0
4     0
5     100
6     0
Total 100\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        with patch('random.randint', return_value=5): #fix the return value to T
            out, actual = x.compare_printout_from_while_loop(fn)
            x.grading_with_string_comparison(("a hundred of 5s in place of random.randint", self._test_cases[0], out))
                     
    def check(self, fn):
        self.check_testbook(fn)       