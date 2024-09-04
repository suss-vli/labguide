from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question7(FunctionProblem):
    _var="question7"
    _test_cases = [
    (5, """1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25\n"""),
    (7, """1 x 7 = 7
2 x 7 = 14
3 x 7 = 21
4 x 7 = 28
5 x 7 = 35
6 x 7 = 42
7 x 7 = 49\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value = args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                  
    def check(self, fn):
        self.check_testbook(fn)       