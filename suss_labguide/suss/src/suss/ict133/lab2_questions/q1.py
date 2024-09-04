from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1(FunctionProblem):
    _var="question1"    
    _test_cases = [
        ("john@suss.edu.sg", """Name is john
Organisation is suss.edu.sg\n"""),
        ("12345@suss.edu.sg","""Name is 12345
Organisation is suss.edu.sg\n"""),
    ]
        
    def test_cases(self):
        return self._test_cases
    
    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)