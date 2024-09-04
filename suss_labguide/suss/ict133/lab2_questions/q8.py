from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question8(FunctionProblem):
    _var="question8"    
    _test_cases = [
        (10.0, """Amount of data used (GB): 10.0
Charge is $25.00\n"""),
        (3.0, """Amount of data used (GB): 3.0
Charge is $15.00\n"""),
        (1.0, """Amount of data used (GB): 1.0
Charge is $5.00\n"""),
        (0, """Amount of data used (GB): 0.0
Invalid input!\n""")    
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