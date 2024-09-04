from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1A(FunctionProblem):
    _var="question1a"
    _test_cases = [
        (['100','1'], "Cost of postage is: $1.10\n"), 
        (['-1','1', '1'], "Weight must be positive and non-zero\nCost of postage is: $0.50\n"),
        (['-1','1', '4', '4', '1'], "Weight must be positive and non-zero\nZone must be either 1, 2 or 3\nZone must be either 1, 2 or 3\nCost of postage is: $0.50\n"),
        (['2001', '1990', '2'], "Max 2000g only\nCost of postage is: $49.95\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)    

class Question1B(FunctionProblem):
    _var="question1b"        
    _test_cases = [
        (['100','1', '200', '2', ''], "Cost of postage is: $1.10\nCost of postage is: $5.20\n"), 
        (['1', '1', '2', '2', '3', '3', ''], "Cost of postage is: $0.50\nCost of postage is: $0.70\nCost of postage is: $1.30\n"),
        (['-1','1', '4', '4', '1', '10', '2', ''], "Weight must be positive and non-zero\nZone must be either 1, 2 or 3\nZone must be either 1, 2 or 3\nCost of postage is: $0.50\nCost of postage is: $0.70\n"),
        (['2001', '1990', '2', '10', '1', '30', '3', ''], "Max 2000g only\nCost of postage is: $49.95\nCost of postage is: $0.50\nCost of postage is: $1.65\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=a):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)    

class Question1C(FunctionProblem):
    _var="question1c"    
    _test_cases = [ # Note: test is unable to 'create' the output file or change the output file content according to the input
        (['100','1', '20', '1', '10', '2', ''], """Cost of postage is: $1.10
Cost of postage is: $0.50
Cost of postage is: $0.70
Zone 1: 2 items - Postage cost: $1.60
Zone 2: 1 items - Postage cost: $0.70
Zone 3: 0 items - Postage cost: $0.00
Total Items: 3 - Total Postage cost: $2.30\n""", "L6Q2Out.dat")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected, filename in self._test_cases: 
            with patch('builtins.input', side_effect=a): 
                (out, actual) = x.read_dat_file(fn, filename)
                x.grading_with_string_comparison((a, expected, out))

    def check(self, fn):
        self.check_testbook(fn)    

Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C
)    