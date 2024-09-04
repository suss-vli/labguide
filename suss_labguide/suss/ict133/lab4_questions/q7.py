from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question7A(FunctionProblem):
    _var="inputSwimmers"
    _test_cases = [
        ("Alice", "Bob", "Cindy", "Dan", "Eric", ['Alice', 'Bob', 'Cindy', 'Dan', 'Eric']),
        ("A", "B", "C", "D", "E", ['A', 'B', 'C', 'D', 'E'])
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]): #NB: note the use of side_effect
                out = fn()
                x.grading(([a,b,c,d,e], expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)

class Question7B(FunctionProblem):
    _var="inputTiming"    
    _test_cases = [ # NB: should i include math ValueError: math domain error? Testcases: 10, 5, 2
        (0, 1, 2, 3, 4, [0.0, 1.0, 2.0, 3.0, 4.0]),
        (0, 0, 0, 0, 0, [0.0, 0.0, 0.0, 0.0, 0.0])
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]): #NB: note the use of side_effect
                swimmers = ['A', 'B', 'C', 'D', 'E']
                out = fn(swimmers)
                x.grading(([a,b,c,d,e], expected, out))
                     
    def check(self, fn):
        self.check_testbook(fn)

class Question7C(FunctionProblem):
    _var="question7c"
    _test_cases = [
        ("A", "B", "C", "D", "E", 0, 0, 0, 0, 0, """A        0.0s
B        0.0s
C        0.0s
D        0.0s
E        0.0s\n"""),
        ("Alice", "Bob", "Cindy", "Dan", "Eric", 0, 1, 2, 3, 4, """Alice    0.0s
Bob      1.0s
Cindy    2.0s
Dan      3.0s
Eric     4.0s\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]): #NB: note the use of side_effect
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e,f,g,h,i,j], expected, out))

    def check(self, fn):
        self.check_testbook(fn)

class Question7D(FunctionProblem):
    _var="question7d"
    _test_cases = [
        ("Alice", "Bob", "Cindy", "Dan", "Eric", 4, 3, 2, 1, 0, """Eric     0.0s
Dan      1.0s
Cindy    2.0s
Bob      3.0s
Alice    4.0s
Fastest is 0.0s\n"""),
        ("A", "B", "C", "D", "E", 1, 2, 3, 4, 5, """A        1.0s
B        2.0s
C        3.0s
D        4.0s
E        5.0s
Fastest is 1.0s\n""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn): # NB: 
        for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]): #NB: note the use of side_effect
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e,f,g,h,i,j], expected, out))
      
    def check(self, fn):
        self.check_testbook(fn)


Question7 = MultipartProblem(
    Question7A,
    Question7B, 
    Question7C,
    Question7D
)    