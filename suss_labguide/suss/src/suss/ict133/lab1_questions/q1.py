from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1(FunctionProblem):
    _var="question1"    
    _test_cases = [
        (80, 26.67),
        (12, -11.11),
        (100000, 55537.78), 
        (0, -17.78)
        # (80, "Temperature in Centigrade: 26.67\n"),
        # (12, "Temperature in Centigrade: -11.11\n"),
        # (100000, "Temperature in Centigrade: 55537.78\n"), 
        # (0, "Temperature in Centigrade: -17.78\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        x.log("calling check_testbook", x.colors.WARN)
        
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                actual = fn()
                x.grading((args, expected, actual))
    
    def check(self, fn):
        self.check_testbook(fn)
        x.log("calling check", x.colors.WARN)