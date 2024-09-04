from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2A(FunctionProblem):
    _var="displayGameScore"   
    _test_cases = [
        ([['A','B'],[21,11],[19,21],[20,22]], """Player A vs B
Game 1 21-11
Game 2 19-21
Game 3 20-22
Overall 1-2
Winner is player B\n""")
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        gameScore=[['A','B'],[21,11],[19,21],[20,22]]
        for a, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=a):
                out, actual = x.compare_printout_with_args(fn, gameScore)
                x.grading_with_string_comparison((a,expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)    

class Question2B(FunctionProblem):
    _var="getPlayerNames"    
    _test_cases = [
        ("A", "B", [['A', 'B']]),
        ("Alice", "Bob", [['Alice', 'Bob']]),
        ("Player1", "Player2", [['Player1', 'Player2']])
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b]):
                out = fn()
                x.grading(([a,b],expected, out))                
    def check(self, fn):
        self.check_testbook(fn)    

class Question2C(FunctionProblem):
    _var="inputGameScores"    
    _test_cases = [
        ('1-2', '2-3', '', [['john', 'matt'], ['1', '2'], ['2', '3']])
        # ("A", "B", "21-10", "21-11", [['A', 'B'], ['21', '10'], ['21', '11']]),
        # ("Alice", "Bob", "0-0", "1-1", [['Alice', 'Bob'], ['0', '0'], ['1', '1']]),
        # ("Player1", "Player2", "1-1", "0-0", [['Player1', 'Player2'], ['0', '0'], ['1', '1']])
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c]):
                scoreList = [['john', 'matt']]
                out = fn(scoreList)
                # x.print_comparison(out,expected)
                x.grading(([a,b,c],expected, out))
                                
    def check(self, fn):
        self.check_testbook(fn)    

class Question2D(FunctionProblem):
    _var="question2d"    
    _test_cases = [
        ("A", "B", '1-2', '2-3', '', """Player A vs B
Game 1 1-2
Game 2 2-3
Overall 0-2
Winner is player B\n""")
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', side_effect=[a,b,c,d,e]):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison(([a,b,c,d,e],expected, out))

    def check(self, fn):
        self.check_testbook(fn)    
        
Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C,
    Question2D
)    