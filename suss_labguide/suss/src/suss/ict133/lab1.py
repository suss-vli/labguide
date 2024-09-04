# Load kaggle's learntools for autograding inside jupyter labs
from learntools.core import *
from .lab1_questions.q1 import Question1
from .lab1_questions.q2 import Question2
from .lab1_questions.q3 import Question3
from .lab1_questions.q4 import Question4
from .lab1_questions.q5 import Question5
from .lab1_questions.q6 import Question6
from .lab1_questions.q7 import Question7
from .lab1_questions.q8 import Question8
from .lab1_questions.q9 import Question9

# Enter the classes in order and makesure they have different names
# bind_exercises will convert them into ex0, ex1, ex2 for instance.
qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9
    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
