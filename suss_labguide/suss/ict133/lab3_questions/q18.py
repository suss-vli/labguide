from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question18(FunctionProblem):
    _var="question18"
    _test_cases = [
        ("10", "10","x divided by y is 1, with remainder 0\n"),
        ("100", "100","x divided by y is 1, with remainder 0\n"),
        ("10","5", "x divided by y is 2, with remainder 0\n"),
]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out, well = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison(([a,b], expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)   