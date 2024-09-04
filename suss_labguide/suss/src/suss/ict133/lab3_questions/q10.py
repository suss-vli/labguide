from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question10(FunctionProblem):
    _var="question10"
    _test_cases = [
        ([1,3,0], """
Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
Option 1 selected

Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
Option 3 selected

Menu
1. Option 1
2. Option 2
3. Option 3
0. Quit
End of program\n""")]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect = self._test_cases[0][0]):#get_value()):
            out, actual = x.compare_printout_from_while_loop(fn)
            x.grading_with_string_comparison((self._test_cases[0][0], self._test_cases[0][1], out))

    def check(self, fn):
        self.check_testbook(fn)   