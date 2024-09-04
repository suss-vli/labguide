from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question6(FunctionProblem):
    _var="question6"
    _test_cases = [
        (4, 2, "The 2 numbers are even\n"),
        (3, 1, "The 2 numbers are odd\n"),
        (4, 3, "One number is even and the other is odd\n"),
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for first, second, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[first,second]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([first,second], expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)       