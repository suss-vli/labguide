from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question12(FunctionProblem):
    _var="question12"
    _test_cases = [
"""Round 1: Correct!
Round 2: Wrong! H
Round 3: Correct!
You guess correct 2 out of 3 rounds.\n""",
"""Round 1: Wrong! T
Round 2: Wrong! T
Round 3: Wrong! T
You guess correct 0 out of 3 rounds.\n"""]
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect = ["3","H","1","H", "3","H","1","H"]):#get_value()):
            with patch('random.choice', return_value="H"):
                out, actual = x.compare_printout_from_while_loop(fn)
                
            with patch('random.choice', return_value="T"):
                out2, actual = x.compare_printout_from_while_loop(fn)
            
            x.grading_with_assertion((out == self._test_cases[0] and out2 == self._test_cases[1]), (["3","H","1","H", "3","H","1","H"] , self._test_cases[0] + self._test_cases[1] ,out + out2))
                     
    def check(self, fn):
        self.check_testbook(fn)   