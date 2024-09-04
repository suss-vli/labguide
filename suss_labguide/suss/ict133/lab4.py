# This is Lab2 - Strings & Selection
from learntools.core import *
from .lab4_questions.q1 import Question1
from .lab4_questions.q2 import Question2
from .lab4_questions.q3 import Question3
from .lab4_questions.q4 import Question4
from .lab4_questions.q5 import Question5
from .lab4_questions.q6 import Question6
from .lab4_questions.q7 import Question7

# Enter the classes in order and makesure they have different names
# bind_exercises will convert them into ex0, ex1, ex2 for instance.
qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
