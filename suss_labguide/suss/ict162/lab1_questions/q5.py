from learntools.core import *
from suss.dev import x

class Question5(FunctionProblem):
    _var="ToDo"
    _test_cases = [
        (['addToDo', 'removeToDoItem'], 'Travel', 'travel.txt', 'pack bag', 2, 3, """Event: Travel
1.buy ticket
2.book hotel
3.do PCR Test\n""", """Event: Travel
1.buy ticket
2.pack bag
3.book hotel
4.do PCR Test\n""", """Event: Travel
1.buy ticket
2.pack bag
3.do PCR Test\n""")
    ]
    
    def check_testbook(self, fn):
        for test in self._test_cases: 
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))

            td = fn(test[1], test[2])
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5]), test[6], td.__str__))
            td.addToDo(test[3], test[4])
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5]), test[7], td.__str__))
            td.removeToDoItem(test[5])
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5]), test[8], td.__str__))

    def check(self, fn):
        self.check_testbook(fn)      