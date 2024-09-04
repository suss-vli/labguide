from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question2(FunctionProblem): 
    _var="question2"
    _test_cases = [
        """Processing guess of A: 50 Too high
Processing guess of B: 60 Too high
Processing guess of C: 70 Too high
Processing guess of A: 20 Too high
Processing guess of B: 30 Too high
Processing guess of C: 10 Correct! in 2 tries
Winner: C
Processing guess of A: 1 Too low
Processing guess of B: 5 Too low
Processing guess of C: 22 Too high
Processing guess of A: 10 Correct! in 2 tries
Processing guess of B: 10 Correct! in 2 tries
Processing guess of C: 15 Too high
Winners: A B
Games winners
Game 1 Winner: C
Game 2 Winners: A B\n"""
    ]
        
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        with patch('random.randint', return_value=10):
            with patch('builtins.input', side_effect = ["A","B","C","", "50", "60","70","20", "30", "10", "Y", "1", "5", "22", "10", "10", "15", "N"]):#get_value()):
                out, actual = x.compare_printout_from_while_loop(fn)
                x.grading_with_assertion((out == self._test_cases[0]), (["A","B","C","", "50", "60","70","20", "30", "10", "Y", "1", "5", "22", "10", "10", "15", "N"] , self._test_cases[0], out))
                
    def check(self, fn):
        self.check_testbook(fn)    