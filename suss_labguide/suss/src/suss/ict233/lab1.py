from learntools.core import *
from .lab1_questions.q1 import Question1
from .lab1_questions.q2 import Question2
        
qvars = bind_exercises(globals(), [
    Question1,
    Question2
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
