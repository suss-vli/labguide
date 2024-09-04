from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question11(FunctionProblem):
    _var="question11"
    _test_cases = [
        (800, 0, "Please pay $800.00. No instalment plan.\n"),
        (1200, 12, "12 month instalment plan of $110.00 per month\n"),
        (2400, 6, "6 month instalment plan of $420.00 per month\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b], expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)   