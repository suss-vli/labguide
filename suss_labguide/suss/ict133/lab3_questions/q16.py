from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question16(FunctionProblem):
    _var="question16"
    _test_cases = [
        ("10", "Sum: 385\n"),
        ("20", "Sum: 2870\n"),
        ("0", "Sum: 0\n")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                out, well = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison((args, expected, out))
   
    def check(self, fn):
        self.check_testbook(fn)   