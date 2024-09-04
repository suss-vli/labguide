from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question3(FunctionProblem):
    _var="question3"
    _test_cases = [
        ("""Name     Weight   Height   BMI     
John     50       1.4      25.51
Peter    60       1.7      20.76
Amy      40       1.3      23.67
Nathan   70       1.7      24.22
Joe      45       1.45     21.4\n""", 'bmi.dat')
    ]
        
    def test_cases(self):   
        return self._test_cases
        
    def check_testbook(self, fn):            
        for expected, filename in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=filename):
                out, actual = x.read_dat_file(fn, filename)
                x.grading_with_string_comparison(("Report in bmi.dat", expected, out))
                        
    def check(self, fn):
        self.check_testbook(fn) 