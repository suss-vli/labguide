from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2(FunctionProblem):
    _var="question2"     
    _test_cases = [
        ("hello world", "Output: olleh dlrow\n"),#,"olleh", "dlrow"),
        ("01234 56789", "Output: 43210 98765\n") #"43210", "98765"),
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
          for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))

    def check(self, fn):
        self.check_testbook(fn)       