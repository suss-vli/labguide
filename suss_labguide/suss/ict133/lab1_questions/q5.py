from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question5(FunctionProblem):
    _var="question5"    
    _test_cases = [
        (100, 2, 0, 0, 0, """50 cent:  2
10 cent:  0
5 cent:  0
1 cent:  0\n"""),
        (47, 0, 4, 1, 2, """50 cent:  0
10 cent:  4
5 cent:  1
1 cent:  2\n"""), 
        (0, 0, 0, 0, 0, """50 cent:  0
10 cent:  0
5 cent:  0
1 cent:  0\n"""),
        (100000, 2000, 0, 0, 0, """50 cent:  2000
10 cent:  0
5 cent:  0
1 cent:  0\n""")
#         (100, 2, 0, 0, 0, """50 cent:  2
# 10 cent:  0
# 5 cent:  0
# 1 cent:  0\n"""),
#         (47, 0, 4, 1, 2, """50 cent:  0
# 10 cent:  4
# 5 cent:  1
# 1 cent:  2\n"""), 
#         (0, 0, 0, 0, 0, """50 cent:  0
# 10 cent:  0
# 5 cent:  0
# 1 cent:  0\n"""),
#         (100000, 2000, 0, 0, 0, """50 cent:  2000
# 10 cent:  0
# 5 cent:  0
# 1 cent:  0\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]):
                try:
                    out, actual = x.compare_printout(fn)
                    x.grading((a, (b, c, d, e), (actual[0], actual[1], actual[2], actual[3])))
                    x.grading_with_string_comparison((a, expected, out))
                except AssertionError:
                    raise
                except:
                    x.grading((a, (b, c, d, e), None))

    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)      