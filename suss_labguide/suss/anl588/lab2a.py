from learntools.core import *
from .lab2a_questions.q1 import Question1
from .lab2a_questions.q2 import Question2
# from .lab1_questions.q3 import Question3
# from .lab1_questions.q4 import Question4


qvars = bind_exercises(globals(), [
    Question1,
    Question2
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
