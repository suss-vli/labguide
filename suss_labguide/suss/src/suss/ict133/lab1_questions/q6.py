from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question6(FunctionProblem):
    _var="question6"
    _test_cases = [
        (10, 10.0, 5.0, 0.5, 0.39, 5.88, """Receipt
Cost of meal:    $ 10.00
50% discount:    $ 5.00
Service charge:  $ 0.50
GST:             $ 0.39
Total amount:    $ 5.88\n"""),
        (10000, 10000.0, 5000.0, 500.0, 385.0, 5885.0, """Receipt
Cost of meal:    $ 10000.00
50% discount:    $ 5000.00
Service charge:  $ 500.00
GST:             $ 385.00
Total amount:    $ 5885.00\n"""), 
        (0, 0.0, 0.0, 0.0, 0.0, 0.0, """Receipt
Cost of meal:    $ 0.00
50% discount:    $ 0.00
Service charge:  $ 0.00
GST:             $ 0.00
Total amount:    $ 0.00\n""")
#         (10, """Receipt
# Cost of meal:    $ 10.00
# 50% discount:    $ 5.00
# Service charge:  $ 0.50
# GST:             $ 0.39
# Total amount:    $ 5.89\n"""),
#         (10000, """Receipt
# Cost of meal:    $ 10000.00
# 50% discount:    $ 5000.00
# Service charge:  $ 500.00
# GST:             $ 385.00
# Total amount:    $ 5885.00\n"""), 
#         (0, """Receipt
# Cost of meal:    $ 0.00
# 50% discount:    $ 0.00
# Service charge:  $ 0.00
# GST:             $ 0.00
# Total amount:    $ 0.00\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for arg, a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[arg,a,b,c,d,e]):
                try:
                    out, actual = x.compare_printout(fn)
                    x.grading((arg, (a, b, c, d, e), (actual[0], actual[1], actual[2], actual[3], actual[4])))
                    x.grading_with_string_comparison((arg, expected, out))
                except AssertionError:
                    raise
                except:
                    x.grading((arg, (a, b, c, d, e), None))
                
    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       