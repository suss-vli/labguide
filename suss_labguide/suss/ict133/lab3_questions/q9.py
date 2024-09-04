from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question9(FunctionProblem):
    _var="question9"
    _test_cases = [
        ([2,1.5,4,2.25,-1], """Subtotal is $3.00
Subtotal is $9.00
Total price is $12.00
GST is $0.84
Please pay $12.84\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        # failed! the patch and return_value does not respond with dynamic random value 
        # according to the while loop inside the fn(). This is because while loop did not exit to retrieve it.
        with patch('builtins.input', side_effect = self._test_cases[0][0]):#get_value()):
            out, actual = x.compare_printout_from_while_loop(fn)
            # x.print_comparison(out, self._test_cases[0][1])
            x.grading_with_string_comparison((self._test_cases[0][0], self._test_cases[0][1], out))
                     
    def check(self, fn):
        self.check_testbook(fn)       