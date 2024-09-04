from learntools.core import *
from unittest.mock import patch
from ...dev import x

# TODO: check if external hints work with this 
class Question4A(EqualityCheckProblem):
    _var = 'marks'
    _hint="Use the `marks` stated in the question"
    _expected = 0
    _solution = CS("""
marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
            """)
    
    def actual_value(self):
        return self.injectable_vars
        # varnames= self.injectable_vars
        # for (var, val) in zip(varnames, args):
    
        # for actual in zip(self.injectable_vars):
        #     return actual
    
class Question4B(FunctionProblem): #question3b only checks for the menu printed out. `choice` is not checked
    _var="question4b"
    _test_cases = [
        ("""Menu
1. Add marks
2. Update marks
3. Remove student
4. Display marks
0. Exit\n""")]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=a):
                out, actual = x.compare_printout(fn)
                # x.print_comparison(out,expected)
                x.grading_with_string_comparison((a,expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)       

class Question4C(FunctionProblem):
    _var="addMarks"
    _test_cases = [
        ('Jane', 1, 1, 'Record exists\n'),
        ('A', 0, 0, 'Added!\n')

         ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                # x.print_comparison(out,expected)
                x.grading_with_string_comparison(([a,b,c],expected, out))
                # ENV=DEV. can be a file. 
                                                    
    def check(self, fn):
        self.check_testbook(fn)  

class Question4D(FunctionProblem):
    _var="updateMarks"
    _test_cases = [
        ('Jane', 'C', '2', """Coursework: 0
Exam: 0
Updated!\n"""),
        ('A', '', '', 'Record does not exist\n')]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison(([a,b,c],expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question4E(FunctionProblem):
    _var="removeStudent"
    _test_cases = [
        ('Jane', 'Record removed: Jane\n'),
        ('Alice', 'Record does not exist: Alice\n')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison((args,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)               

class Question4F(FunctionProblem):
    _var="displayMarks"
    _test_cases = [
        ("""Name     CW  EX  Overall Grade
John     0   0   0.0      F
Jane     0   0   0.0      F
Peter    0   0   0.0      F
Joe      0   0   0.0      F\n""")

    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected):
                marks = {'John':[0,0],'Jane':[0,0],'Peter':[0,0],'Joe':[0,0]}
                out, actual = x.compare_printout_with_args(fn, marks)
                x.grading_with_string_comparison((marks,expected, out))

    def check(self, fn):
        self.check_testbook(fn)

class Question4G(FunctionProblem):
    _var="question4g"
    _test_cases = [
        ('')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((expected,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

Question4 = MultipartProblem(
    Question4A,
    Question4B, 
    Question4C,
    Question4D,
    Question4E,
    Question4F,
    Question4G
)