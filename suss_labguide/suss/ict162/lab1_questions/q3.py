from learntools.core import *
from suss.dev import x

class Question3(FunctionProblem):
    _var="Point"
    _test_cases = [
        (['distanceTo', 'move', 'quadrant', 'x', 'y'], 5, 1, 10, -10, '(5, 1)', 1, 9.486832980505138, 2)
    ]

    def check_testbook(self, fn):
        for test in self._test_cases: 
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                if item == "width":
                    if isinstance(fn.width, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`width` should be a property.")
                elif item == "length":
                    if isinstance(fn.length, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`length` should be a property.")

            p1 = fn(test[1], test[2])
            p2 = fn(test[3], test[4])

            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[5], p1.__str__))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[6], p1.quadrant))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[8], p2.quadrant))
            
            p1.move(2, -2)
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[7], p1.distanceTo(p2)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]),  test[8], p1.quadrant))

            x.grading_check_setter("`p1.x = 3`", 1, p1, "x", p1._x, "@x.setter")
            x.grading_check_setter("`p1.y = 3`", 1, p1, "y", p1._y, "@y.setter")
                
    def check(self, fn):
        self.check_testbook(fn)  