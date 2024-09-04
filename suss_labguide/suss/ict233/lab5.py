from learntools.core import *
from .lab5_questions.q1 import Question1
        
qvars = bind_exercises(globals(), [
    Question1,
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
