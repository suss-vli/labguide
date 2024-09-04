from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2(FunctionProblem):
    _var="question2"
    _test_cases = [
            ('1','2','3',6.0,2.0),
            ('100','200','300',600.0, 200.0), 
            ('0','0','0',0.0,0.0),
            ('0','1','100000',100001.0, 33333.666666666664)
#             ('1','2','3', """Sum = 6.0
# Average = 2.0\n"""),
#             ('100','200','300',"""Sum = 600.0
# Average = 200.0\n"""), 
#             ('0','0','0', """Sum = 0.0
# Average = 0.0\n"""),
#             ('0','1','100000',"""Sum = 100001.0
# Average = 33333.666666666664\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,sum,average in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                try:
                    actual_sum, actual_average = fn()
                    x.grading(([a,b,c],(sum, average), (actual_sum, actual_average)))
                except AssertionError:
                    raise
                except: # in line 94, when return value is Nonetype (no return value), there will be "TypeError: cannot unpack non-iterable int object". This line is to capture the error and raise incorrect.
                    x.grading(([a,b,c], (sum, average), None))
                
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       