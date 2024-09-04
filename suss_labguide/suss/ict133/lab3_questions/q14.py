from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question14(FunctionProblem):
    _var="question14"
    _test_cases = ["""Correct!
 You got it in 1 tosses!
Wrong! T
Wrong! T
Wrong! T
Correct!
 You got it in 4 tosses!
Program end\n"""
]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        with patch('builtins.input', side_effect = ["T","Y","H", "H", "H", "T", "N"]):#get_value()):
            with patch('random.choice', side_effect=["T", "T", "T", "T","T"]): #fix the return value to T
                out, actual = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison((["T", "T", "T", "T","T"], self._test_cases[0], out))

    def check(self, fn):
        self.check_testbook(fn)   