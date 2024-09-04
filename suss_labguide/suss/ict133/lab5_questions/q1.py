from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1A(FunctionProblem): 
    _var="question1a"    
    _test_cases = [
        ("""Diver A1  A2  A3  Total
   1  7.9 7.8 8.2 23.9
   2  8.0 8.5 8.4 24.9
   3  9.0 9.1 9.5 27.6
   4  9.0 9.2 9.2 27.4
   5  8.5 8.8 9.0 26.3
   6  9.7 9.8 9.7 29.2\n""") #single definition of "passing the test"
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(("Score in the list", expected, out))
                    
    def check(self, fn):
        self.check_testbook(fn)    

class Question1B(FunctionProblem):
    _var="question1b"
    # Important! Do not add new line to the test values
    _test_cases = [
        ("""Diver A1  A2  A3  Total
   1  7.9 7.8 8.2 23.9
   2  8.0 8.5 8.4 24.9
   3  9.0 9.1 9.5 27.6
   4  9.0 9.2 9.2 27.4
   5  8.5 8.8 9.0 26.3
   6  9.7 9.8 9.7 29.2
Top three positions
Diver Total
   6  29.2
   3  27.6
   4  27.4\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(("Score in the list", expected, out))
                       
    def check(self, fn):
        self.check_testbook(fn)    

Question1 = MultipartProblem(
    Question1A,
    Question1B
)    