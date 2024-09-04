from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4(FunctionProblem):
    _var="question4"
    _test_cases = [
                ("Singapore",3, """Singapore
Singapore
Singapore\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b], expected, out))
                          
    def check(self, fn):
        self.check_testbook(fn)       