from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question8(FunctionProblem):
    _var="question8"
    _test_cases = [
        (1000, 10, 3, 1343.92),
        (0, 0, 0, 0.00)
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                actual = fn()
                x.grading(((a, b, c), expected, actual))
                    
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       