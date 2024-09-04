from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question10(FunctionProblem):
    _var="question10"
    _test_cases = [
        (1,1,3, "Not possible to form a triangle\n"),
        (1,1,1, "Triangle type: Equilateral (All 3 sides are equal)\n"),
        (2,3,4, "Triangle type: Scalene (All 3 sides are unequal)\n"),
        (2,2,3, "Triangle type: Isosceles (Any 2 sides are equal)\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c], expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)   