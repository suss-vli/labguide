from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question15(FunctionProblem):
    _var="question15"
    _test_cases = [
        """10
11
12
13
14
15
16
17
18
19
20\n"""
]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect = ["10", "20"]):#get_value()):
            out, actual = x.compare_printout_from_while_loop(fn)
            x.grading_with_string_comparison((["10", "20"], self._test_cases[0], out))
                     
    def check(self, fn):
        self.check_testbook(fn)   