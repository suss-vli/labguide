from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question7(FunctionProblem):
    _var="question7"
    _test_cases = [ # NB: should i include math ValueError: math domain error? Testcases: 10, 5, 2
        ("S1234567D", "Valid NRIC\n"),
        ("T1234567Z", "Valid NRIC\n"),
        ("T123457Z", "Length must be exactly 9\n"),
        ("T123457ZZ", "Must consist of 7 digits\n"),
        ("A1234567Z", "The first letter must be S, T, F or G\n"),
        ("S12345678", "Reference letter must be A to Z or a to z\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args): #NB: note the use of side_effect
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)       