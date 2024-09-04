from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question6(FunctionProblem):
    _var="question6"
    _test_cases = [
        (["Singapore", 3, "exit"], """Singapore
Singapore
Singapore
end\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        with patch('builtins.input', side_effect=self._test_cases[0][0]):
            out, actual = x.compare_printout_from_while_loop(fn)                
            x.grading_with_string_comparison((self._test_cases[0][0], self._test_cases[0][1], out))
                        
    def check(self, fn):
        self.check_testbook(fn)       