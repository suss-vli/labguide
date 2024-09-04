# Load kaggle's learntools for autograding inside jupyter labs
from learntools.core import *
from .lab3_questions.q1 import Question1
from .lab3_questions.q2 import Question2
from .lab3_questions.q3 import Question3
from .lab3_questions.q4 import Question4
from .lab3_questions.q5 import Question5
from .lab3_questions.q6 import Question6
from .lab3_questions.q7 import Question7
from .lab3_questions.q8 import Question8
from .lab3_questions.q9 import Question9
from .lab3_questions.q10 import Question10
from .lab3_questions.q11 import Question11
from .lab3_questions.q12 import Question12
from .lab3_questions.q13 import Question13
from .lab3_questions.q14 import Question14
from .lab3_questions.q15 import Question15
from .lab3_questions.q16 import Question16
from .lab3_questions.q17 import Question17
from .lab3_questions.q18 import Question18
        
qvars = bind_exercises(globals(), [
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
    Question11,
    Question12,
    Question13,
    Question14,
    Question15,
    Question16,
    Question17,
    Question18

    ],
    start=1,
    var_format='q{n}',
    )
__all__ = list(qvars)
