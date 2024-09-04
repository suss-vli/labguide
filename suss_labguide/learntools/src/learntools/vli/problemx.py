import re
from abc import ABC, abstractmethod
import inspect
import os
from typing import List
from learntools.vli.encryption import  decrypt, load_config

class ProblemX(ABC):
    _solution = ''
    def abbreviate_question(self,question):
        return re.sub(r'(?i)question(\d+[a-z]*)', lambda m: 'q' + m.group(1).lower(), question)
        
    def process_path(self, path):
        if path is None:
            return
        exercise, course = path.split('/')[-1].split('.')[0], path.split('/')[-2]
        return exercise, course

    def get_path(self):
        data = load_config()
        class_file = inspect.getfile(self.__class__)
        path = os.path.abspath(class_file)
        exercise, course = self.process_path(path)
        question = self.abbreviate_question(self.__class__.__name__)
        fullpath = course + '/' + exercise + '/' + question + '/'
        return data["suss_path"] + fullpath
    
    _counts_for_points = True
    _bonus = False

    def __init__(self, hint_file: str = '', solution_file: str = ''):
        self._hint_file = hint_file if hint_file else f'{self.get_path()}hint'
        self._solution_file = solution_file if solution_file else f'{self.get_path()}solution'

    @property
    def solution(self):
        try:    
            with open(self._solution_file, 'r') as file:
                encrypted_solution = file.read()
            solution = decrypt(encrypted_solution)
            return '\n\n'+ '```python\n' +''.join(solution) + '\n```' 
        except Exception as e:
            print(e)
            return "No solution available for this question. This may be because the solution file is not present. Please refer to the documentation E12."

    @property
    def hints(self) -> List[str]:
        try:    
            with open(self._hint_file, 'r') as file:
                encrypted_hints = file.read()
                
            content = decrypt(encrypted_hints)
            hints = content.split('\n')
            return ['\n' + '\n'.join(hints)]
        except Exception as e:
            print(e)
            return ["No hints available for this question. This may be because the hint file is not present. Please refer to the documentation E12."]

    @property
    def _correct_message(self):
        if (    self.show_solution_on_correct 
                or (self.show_solution_on_correct is None 
                    and isinstance(self.solution, str)
                    )
                ):
            return '\n\n' + self.solution
        else:
            return ''

    @abstractmethod
    def check(self, *args):
        """If this method runs without exceptions, it indicates that checking passed
        and the solution is correct. To indicate other outcomes, implementations of 
        this method should raise one of the following:
        - Uncheckable: If this problem explicitly has no checking logic.
        - NotAttempted: If it seems the problem hasn't been attempted (i.e. the 
            starter code hasn't been modified.
        - Incorrect, AssertionError: If there's a problem with the user's solution.

        Any messages attached to these exceptions will be passed on in the message shown
        to the user.
        """
        pass

    def check_whether_attempted(self, *args):
        pass

