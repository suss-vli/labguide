from learntools.core import *
from learntools.core.problem import injected
from ...dev import x

# load mock and patch to solve builtin.input and testcases
from io import StringIO
from unittest.mock import patch

class Question2(FunctionProblem):
    _var="question2"

    _test_cases = [
        ("Jane", "Hello Jane")
    ]

    def check(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                actual = fn()
                x.grading((args, expected, actual))