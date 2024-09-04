from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4(FunctionProblem):
    _var="question4"
    _test_cases = [
        (1000000000, 277777, 46, 40),
        (0, 0, 0, 0),
        (1, 0, 0, 1),
        (100, 0, 1, 40)
        # (1000000000, """1000000000 seconds is equal to 277777 hours, 46 minutes and 40 seconds\n"""),
        # (0, """0 seconds is equal to 0 hours, 0 minutes and 0 seconds\n"""),
        # (1, """1 seconds is equal to 0 hours, 0 minutes and 1 seconds\n"""),
        # (100, """100 seconds is equal to 0 hours, 1 minutes and 40 seconds\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, hours, minutes, seconds in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                try:
                    expected_hours, expected_minutes, expected_seconds = fn()
                    x.grading((args, (hours, minutes, seconds), (expected_hours, expected_minutes, expected_seconds)))
                except AssertionError:
                    raise
                except:
                    x.grading((args, (hours, minutes, seconds), None))
                
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       