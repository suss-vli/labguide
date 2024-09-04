from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question4(FunctionProblem):
    _var="question4"    
    _test_cases = [
        ("lEVEL", "Message is not a palindrome.\n"),
        ("LEVEL", "Message is a palindrome.\n"),
        ("Level", "Message is not a palindrome.\n"),
        ("tattarrattat", "Message is a palindrome.\n"),
        ("saippuakivikauppias", "Message is a palindrome.\n"), 
        ("Singapore is a beautiful island nation in South East Asia.", "Message is not a palindrome.\n")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
          for args, expected in self._test_cases: # for each testcase, we assert that it is similar to the test value.
            with patch('builtins.input', return_value=args):
                out, actual = x.compare_printout(fn)
                x.grading_with_string_comparison((args, expected, out))
                         
    def check(self, fn):
        self.check_testbook(fn)       