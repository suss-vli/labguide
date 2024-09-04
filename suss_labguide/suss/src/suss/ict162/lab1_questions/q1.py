from learntools.core import *
from suss.dev import x

class Question1(FunctionProblem):

    _var="Person"
    _test_cases = [
        (['gender', 'getFullName', 'getInitials', 'lastName', 'name'], 'm', 'ah seng', 'tan', "Mr. Tan Ah Seng", "A. S. Tan", "Name: Tan Ah Seng     Gender : Male"),
        (['gender', 'getFullName', 'getInitials', 'lastName', 'name'], 'f', 'mary', 'taylor', "Ms. Taylor Mary", "M. Taylor", "Name: Taylor Mary     Gender : Female")
        ]

    # to fix this https://vlisuss.atlassian.net/browse/VLI-32?focusedCommentId=10018
    def check_testbook(self, fn):
        for test in self._test_cases:
            print(f"Test: {test}")
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                    
                if item == "name":
                    if isinstance(fn.name, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`name` should be a property.")
                elif item == "lastName":
                    if isinstance(fn.lastName, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`lastName` should be a property.")
                elif item == "gender":
                    if isinstance(fn.gender, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`gender` should be a property.")
            
            p1 = fn(test[1], test[2], test[3])

            x.determine_the_grading_method(((test[1], test[2], test[3]), test[4], p1.getFullName))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[5], p1.getInitials))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[6], p1.__str__))

            x.grading_check_setter("`p1.name = Tom`", "Tom", p1, "name", p1._name, "@name.setter")
            x.grading_check_setter("`p1.lastName = Lim`", "Lim", p1, "lastName", p1._lastName, "@lastName.setter")
            
    def check(self, fn):
        self.check_testbook(fn)