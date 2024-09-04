from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question6(FunctionProblem):
    _var="question6"
    _test_cases = [
        ("a","b","b","a","d","c","b","a","b","c", """Q1: a
Q2: b
Q3: b
Q4: a
Q5: d
Q6: c
Q7: b
Q8: a
Q9: b
Q10: c
Q1: a correct
Q2: b correct
Q3: b correct
Q4: a correct
Q5: d correct
Q6: c correct
Q7: b correct
Q8: a correct
Q9: b correct
Q10: c correct
Total 10 out of 10 correct\n"""),
        ("a","b","c","d","a","b","c","d","a","b", """Q1: a
Q2: b
Q3: c
Q4: d
Q5: a
Q6: b
Q7: c
Q8: d
Q9: a
Q10: b
Q1: a correct
Q2: b correct
Q3: c incorrect, answer is b
Q4: d incorrect, answer is a
Q5: a incorrect, answer is d
Q6: b incorrect, answer is c
Q7: c incorrect, answer is b
Q8: d incorrect, answer is a
Q9: a incorrect, answer is b
Q10: b incorrect, answer is c
Total 2 out of 10 correct\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e,f,g,h,i,j], expected, out))

    def check(self, fn):
        self.check_testbook(fn)       