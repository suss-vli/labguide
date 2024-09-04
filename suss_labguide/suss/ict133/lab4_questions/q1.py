from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1(FunctionProblem):
    _var="question1"    
    _test_cases = [
        ("""Rainfall Summary
Average rainfall 5.65mm
No of days with no rain 3 days
Highest rainfall recorded 20.6mm\n""")
    ]
    
    def test_cases(self):
        return self._test_cases
    
    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(("Data in rainfall.dat", expected, out))
                        
    def check(self, fn):
        self.check_testbook(fn)