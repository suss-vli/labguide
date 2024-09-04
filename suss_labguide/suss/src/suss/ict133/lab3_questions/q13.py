from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question13(FunctionProblem):
    _var="question13"    
    _test_cases = [
        """Wrong! T
Wrong! T
Correct!
 You got it in 3 tosses!\n"""]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect = ["H","H","T"]):#get_value()):
            with patch('random.choice', return_value="T"): #fix the return value to T
                out, actual = x.compare_printout_from_while_loop(fn)
                x.grading_with_string_comparison(("T", self._test_cases[0], out))

    def check(self, fn):
        self.check_testbook(fn)   