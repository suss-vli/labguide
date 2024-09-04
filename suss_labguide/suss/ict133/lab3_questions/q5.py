from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question5(FunctionProblem):
    _var="question5"
    _test_cases = [
                ("hello", """h
he
hel
hell
hello\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value = args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                      
    def check(self, fn):
        self.check_testbook(fn)      