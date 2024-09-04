from learntools.core import *
from unittest.mock import patch
from ...dev import x

# Question3 - step by step multiple part functional problem
class Question3A(EqualityCheckProblem):
    _var = 'currs'    
    def actual_value(self):
        return self.injectable_vars
        # varnames= self.injectable_vars
        # for (var, val) in zip(varnames, args):
    
        # for actual in zip(self.injectable_vars):
        #     return actual
    
class Question3B(FunctionProblem): #question3b only checks for the menu printed out. `choice` is not checked
    _var="question3b"
    _test_cases = [
        (1, """Menu
1. Add Currency
2. Adjust Currency
3. Remove Currency
4. Display Currency rates
0. Quit\n""")]
    
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

class Question3C(FunctionProblem):
    _var="addCurrency"
    _test_cases = [
        ('MYR',3, """Currency updated {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73, 'MYR': 3.0}\n"""),
        ('hkd',4, """Currency already exists! {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}\n""")
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                # x.print_comparison(out,expected)
                x.grading_with_string_comparison(([a,b],expected, out))
                                                    
    def check(self, fn):
        self.check_testbook(fn)  

class Question3D(FunctionProblem):
    _var="adjustCurrency"
    _test_cases = [
        ('sgd', '', 'Currency not found!\n'),
        ('usd', '1', """Rate is 0.73
USD adjusted to 1.0\n""")

    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison(([a,b],expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question3E(FunctionProblem):
    _var="removeCurrency"
    _test_cases = [
        ('hkd', 'Currency removed!\n'),
        ('myr', 'Currency not found!\n')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for args,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison((args,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)               

class Question3F(FunctionProblem):
    _var="displayCurrencyRates"    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected): # TODO: remove this? 
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout_with_args(fn, currs)
                x.grading_with_string_comparison((currs,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

class Question3G(FunctionProblem):
    _var="question3g"
    _test_cases = [
        ('')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=expected): #TODO remove this?
                currs = {'USD': 0.73, 'RMB': 5.01, 'HKD': 5.73}
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((expected,expected, out))
        
    def check(self, fn):
        self.check_testbook(fn)

Question3 = MultipartProblem(
    Question3A,
    Question3B, 
    Question3C,
    Question3D,
    Question3E,
    Question3F,
    Question3G
)