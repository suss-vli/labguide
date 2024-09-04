from learntools.core import *
from ...dev import x
from unittest.mock import patch


class Question2A(FunctionProblem):
    _var="InvalidAssessmentException"
    _test_cases = [
        ()
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        test = fn.__bases__.__str__()
        if 'Exception' in test:
            x.justpass()
        else: 
            assert test == 'Exception', (f"""The parent class of {fn.__name__} should be an Exception""")

    def check(self, fn):
        self.check_testbook(fn)       

class Question2B(FunctionProblem):
    _var="Assessment"
    _test_cases = [
        (['_max', 'getMaxMarks', 'mark', 'setMaxMarks', 'studentId'], '001', 80, """Student id: 001 Mark: 80""" ),
        (['_max', 'getMaxMarks', 'mark', 'setMaxMarks', 'studentId'], '002', 101, """Mark can only be between 0 and 100""" )
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                if item == "_max":
                    if fn._max == 100:
                        x.justpass()
                    else:
                        x.justfail(item, f"`_max` is `{fn._max}`. It should be `100`.")
                if item == "studentId":
                    if isinstance(fn.studentId, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`studentId` should be a property.")

            try: 

                a1 = fn(test[1], test[2])
                if a1.getMaxMarks() == None:
                    x.justfail("NoneType", f"`a1.getMaxMarks` is {a1.getMaxMarks()}. Please attempt the question and run the question again.")
                else:
                    x.determine_the_grading_method(('', 100, a1.getMaxMarks()))
                    x.determine_the_grading_method(((test[1], test[2]), test[3], a1.__str__))

            except AssertionError:
                raise   
            except AttributeError:
                x.justfail("", "@mark.setter is not defined. Please check your code.")
            except NameError as e:
                    x.justfail('', f"{e}. Run the cell for `InvalidAssessmentException` first.")
            except Exception as e:
                    x.determine_the_grading_method(((test[1], test[2]), test[3], e.__str__))
    
    def check(self, fn):
        self.check_testbook(fn)

class Question2C(FunctionProblem):
    _var="TutorialGroup"
    _test_cases = [
        ('T01', '001', 80, '002', 70, '003', 50, '002', '002', """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70
Student id: 003 Mark: 50""", """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 0
Student id: 003 Mark: 50""", """T01
Student id: 001 Mark: 80
Student id: 003 Mark: 50""", ""),
# testing InvalidAssessmentException
('T01', '001', 80, '001', 88, "", "", "", "", "", "", "", """Assessment for 001 already added previously! Cannot add!"""),
('T01', '001', 80, '002', 70, '003', 50, '002', '004', """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70
Student id: 003 Mark: 50""", """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 0
Student id: 003 Mark: 50""", "", """Assessment for 004 not found!"""),
('T01', '001', 80, '002', 70, '003', 50, '002', '003', """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70
Student id: 003 Mark: 50""", """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 0
Student id: 003 Mark: 50""", "", """Cannot remove if assessment mark is not 0"""),
('T01', '001', 80, '002', 88, '003', 60, '004', "", """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 88
Student id: 003 Mark: 60""", "", "", """Assessment for 004 not found!"""),
('T01', '001', 80, '002', 0, '003', 50, '002', '002', """T01
Student id: 001 Mark: 80
Student id: 002 Mark: 0
Student id: 003 Mark: 50""", "", "", "Mark to adjust is the same as existing mark!") ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            try:
                tg = fn(test[0])

                tg.addAssessment(test[1], test[2])
                tg.addAssessment(test[3], test[4])
                tg.addAssessment(test[5], test[6])

                x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6]), test[9], tg.__str__))
                tg.adjustAssessment(test[7], 0)
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], 0), test[10], tg.__str__))
                tg.removeAssessment(test[8])
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6]), test[11], tg.__str__))
            except AssertionError:
                raise
            except Exception as e:
                error_message = str(e)
                if "NoneType" in error_message:
                    x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6]), test[9], tg.__str__))
                else:
                    x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[12], e.__str__))

    def check(self, fn):
        self.check_testbook(fn)

class Question2D(FunctionProblem):
    _var="question2d"
    _test_cases = [
        (1, '001', 80, 1, '002', 70, 1, '003', 50, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70
Student id: 003 Mark: 50

"""),
        (1, '001', 80, 3, '001', 0, 2, '001', 4, 5, """Added!
T01
Student id: 001 Mark: 80

Adjusted!
T01
Student id: 001 Mark: 0

Removed!
T01
No assessment currently

T01
No assessment currently
T01
No assessment currently

"""),
(1, '001', 80, 1, '002', 70, 1, '001', 80, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Assessment for 001 already added previously! Cannot add!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n"""),
(1, '001', 80, 1, '002', 70, 1, '003', 101, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Mark can only be between 0 and 100
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n"""),
(1, '001', 80, 1, '002', 70, 3, '003', 50, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Assessment for 003 not found!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n"""),
(1, '001', 80, 1, '002', 70, 3, '003', 50, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Assessment for 003 not found!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n"""),
(1, '001', 80, 1, '002', 70, 2, '003', 5, '', """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Assessment for 003 not found!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n"""),
(1, '001', 80, 1, '002', 70, 3, '002', 70, 5, """Added!
T01
Student id: 001 Mark: 80

Added!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70

Mark to adjust is the same as existing mark!
T01
Student id: 001 Mark: 80
Student id: 002 Mark: 70\n\n""")
#TODO:test case below is different from instructor solution: instructor solution rewrote the `removeAssessment` and no exception message is displayed - which is also different from question
# (1, '001', 80, 1, '002', 70, 2, '002', 5, '', """Added!
# T01
# Student id: 001 Mark: 80

# Added!
# T01
# Student id: 001 Mark: 80
# Student id: 002 Mark: 70

# Cannot remove if assessment mark is not 0
# T01
# Student id: 001 Mark: 80
# Student id: 002 Mark: 80\n\n""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e,f,g,h,i,j, expected in self._test_cases: 
            with patch('builtins.input', side_effect=[a,b,c,d,e,f,g,h,i,j]):
                out, actual = x.compare_printout(fn)
                x.determine_the_grading_method(([a,b,c,d,e,f,g,h,i,j], expected, out))
                
    def check(self, fn):
        self.check_testbook(fn)

Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C,
    Question2D
) 
