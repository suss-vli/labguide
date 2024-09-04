from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question3(FunctionProblem):
    _var="question3"
    _test_cases = [
        ('100',1,0),
        ('000',0,0),
        ('999',27, 729),
        ('777',21, 343)
#         ('100', """Sum = 1
# Product = 0\n"""),
#         ('000', """Sum = 0
# Product = 0\n"""),
#         ('999',"""Sum = 27
# Product = 729\n"""),
#         ('777', """Sum = 21
# Product = 343\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, sum, product in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                try:
                    actual_sum, actual_product = fn()
                    x.grading((args, (sum, product), (actual_sum, actual_product)))
                except AssertionError:
                    raise
                except: # in line 94, when return value is Nonetype (no return value), there will be "TypeError: cannot unpack non-iterable int object". This line is to capture the error and raise incorrect.
                    x.grading((args, (sum, product), None))
                
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       