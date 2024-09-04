from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question9(FunctionProblem):
    _var="question9"    
    #TODO: Is the solution still having this issue? Bryan, had some issues with the solution below that is from chatGPT. Had to resolve by copy and pasting the # round and # print lines for every condition
    _test_cases = [
        ("23.6 + 33.2", "Result:  56.8\n"),
        ("85 % 15", "Invalid arithmetic operator\n"),
        ("2.1 - 1.9", "Result:  0.2\n"),
        ("9.9 * 0", "Result:  0.0\n"),
        ("2.2 / 1.1", "Result:  2.0\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args): #NB: note the use of side_effect
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)       