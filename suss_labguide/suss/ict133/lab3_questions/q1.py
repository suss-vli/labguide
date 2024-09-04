from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1(FunctionProblem):
    _var="question1"
    _test_cases = [
        (3,5, """3
4
5\n""")]
        
    def test_cases(self):
        return self._test_cases
            
    def check_testbook(self, fn):
        for a, b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b], expected, out))
                    
    def check(self, fn):
        self.check_testbook(fn)