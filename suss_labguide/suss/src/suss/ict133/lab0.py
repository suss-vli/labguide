# Load kaggle's learntools for autograding inside jupyter labs
from learntools.core import *
from .lab0_questions.q1 import Question1
from .lab0_questions.q2 import Question2
from .lab0_questions.q3 import Question3
from .lab0_questions.q4 import Question4
from .lab0_questions.q5 import Question5
from .lab0_questions.q6 import Question6
from .lab0_questions.q7 import Question7
from .lab0_questions.q8 import Question8
from .lab0_questions.q9 import Question9


# Autograding is the act of automating grading in order to achieve graded work. These graded work comprises of grades, graded assignnment or exam, feedback.
# Autotesting is a way for instructors to run batch testing code to do autograding. 
# The learning tools by kaggle are hint(), check(), solution()
# ***There should be a way to automativally generate these learning tools from the tests that the instructors write.
    
#IGORNE Variables are names given to computer memory locations in order to store data in a program. This data can be known or unknown based on the assignment of value to the variables.
#Variables can also be considered as ‘containers’ which are used to hold more than one value. Their sole purpose is to label and store data in the memory and then this Variable can be accessed throughout the program whenever needed.

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
