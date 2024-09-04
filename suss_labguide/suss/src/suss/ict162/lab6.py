from learntools.core import *
from .lab6_questions.q1 import Question1
from .lab6_questions.q2 import Question2
from .lab6_questions.q3 import Question3
from .lab6_questions.q4 import Question4

qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)