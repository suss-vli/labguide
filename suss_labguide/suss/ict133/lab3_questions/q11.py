from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question11(FunctionProblem):
    _var="question11"
    _test_cases = [
        ("H", "Correct!\n"), 
        ("h", "Correct!\n"),
        ("T", "Wrong! H\n"), 
        ("t", "Wrong! H\n"),
        ("Z", "Please use H or T.\n"), 
        ("z", "Please use H or T.\n")
]
    
    def test_cases(self):
        return self._test_cases
          
    def check_testbook(self,fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect =[a]):
                with patch('random.choice', return_value="H"):
                    out, actual = x.compare_printout(fn)
                    x.grading_with_string_comparison((a,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)   