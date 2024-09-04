from learntools.core import *
from suss.dev import x
        
class Question2(FunctionProblem):
    _var="Rectangle"
    _test_cases = [
        (['getArea', 'getPerimeter', 'increaseSize', 'isBigger', 'length', 'width'], 3, 4, 2, 5, 'Length: 13  Width: 14  Area: 182  Perimeter: 54', 10, 14)
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

            r1 = fn(test[1], test[2])
            r2 = fn(test[3], test[4])
            r1.increaseSize(10,10)

            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[5], r1.__str__))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[6], r2.getArea))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), test[7], r2.getPerimeter))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), True, r1.isBigger(r2)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4]), False, r2.isBigger(r1)))

            x.grading_check_setter("`r1.length = 1`", 1, r1, "length", r1._length, "@length.setter")
            x.grading_check_setter("`r1.width = 1`", 1, r1, "width", r1._width, "@width.setter")

    def check(self, fn):
        self.check_testbook(fn)    