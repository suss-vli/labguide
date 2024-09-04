from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question8(FunctionProblem):
    _var="question8"    
    # note the difference in test cases where there is only one giant test cases 
    # with a combination 
    _test_cases = [
        ([1,2,3,4,5], """1 x 1 = 1
1 x 2 = 2
2 x 2 = 4
1 x 3 = 3
2 x 3 = 6
3 x 3 = 9
1 x 4 = 4
2 x 4 = 8
3 x 4 = 12
4 x 4 = 16
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect=self._test_cases[0][0]):
            out, actual = x.compare_printout_from_while_loop(fn)
            x.grading_with_string_comparison((self._test_cases[0][0], self._test_cases[0][1], out))
               
    def check(self, fn):
        self.check_testbook(fn)       