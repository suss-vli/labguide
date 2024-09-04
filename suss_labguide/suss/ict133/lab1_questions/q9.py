from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question9(FunctionProblem):
    _var="question9"
    _test_cases = [
        (10,10,10,10,10,11, """Clock time is 10:10:10
After 1 second, the time is 10:10:11\n"""),
        (9,9,9,9,9,10,"""Clock time is 09:09:09
After 1 second, the time is 09:09:10\n"""), 
        (0,0,0,0,0,1,"""Clock time is 00:00:00
After 1 second, the time is 00:00:01\n"""),
        (23,59,59,0,0,0,"""Clock time is 23:59:59
After 1 second, the time is 00:00:00\n""")
        # (10,10,10, """Clock time is 10:10:11\n"""),
        # (9,9,9,"""Clock time is 09:09:10\n"""), 
        # (0,0,0,"""Clock time is 00:00:01\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e,f, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e,f]):
                try:
                    out, actual = x.compare_printout(fn)
                    x.grading(([a,b,c], (d,e,f), (actual[0], actual[1], actual[2])))
                    x.grading_with_string_comparison(([a,b,c], expected, out))
                except AssertionError:
                    raise
                except:
                    x.grading(([a,b,c], (d,e,f), None))

    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       