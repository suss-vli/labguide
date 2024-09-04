from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question7(FunctionProblem):
    _var="question7"
    _test_cases = [
        (10, 8, 6, 24.0),
        (100, 80, 60, 2400.0), # NB: 0,0,0 will pass
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                actual = fn()
                x.grading(((a, b, c), expected, actual))
                
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       