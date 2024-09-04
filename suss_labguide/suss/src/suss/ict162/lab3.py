from learntools.core import *
from .lab3_questions.q1 import Question1
from .lab3_questions.q2 import Question2
from .lab3_questions.q3 import Question3
from .lab3_questions.q4 import Question4
from .lab3_questions.q5 import Question5
from .lab3_questions.q6 import Question6


qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
