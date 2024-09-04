from learntools.core import *
from unittest.mock import patch
from ...dev import x

class Question1A(FunctionProblem):
    _var="BoxException"
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
        
class Question1B(FunctionProblem):
    _var="Box"    
    _test_cases = [
        (['_maxItems', 'add', 'remove'], 5, 2, 7, """Number of items: 5""", """Number of items: 3""", """Number of items: 10""", """"""),
        (['_maxItems', 'add', 'remove'], 1, 2, 0, """Number of items: 1""", """""","""""", """Box currently has 1 items. Cannot remove 2 items"""),
        (['_maxItems', 'add', 'remove'], 10, 0, 1, """Number of items: 10""", """Number of items: 10""", """""", """Box currently has 10 items. Cannot add 1 items because 11 exceeds max 10"""),
        (['_maxItems', 'add', 'remove'], -1, 0, 0, """""", """""", """""","""Cannot have a negative value for number of items in a box. Current given is -1"""),
        (['_maxItems', 'add', 'remove'], 11, 0, 0, """""", """""", """""", """11 items cannot fit into a box. Max number is 10"""),
        (['_maxItems', 'add', 'remove'], 1, -1, 0, """Number of items: 1""", """""", """""", """Cannot remove negative number of items: -1"""),
        (['_maxItems', 'add', 'remove'], 1, 0, -1, """Number of items: 1""", """Number of items: 1""", """""", """Cannot add negative number of items: -1""")
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
                if item == "_maxItems":
                    if fn._maxItems == 10:
                        x.justpass()
                    else:
                        x.justfail(item, f"`_maxItems` is `{fn._maxItems}`. It should be `10`.")

            try:
                b1 = fn(test[1])
                x.determine_the_grading_method((test[1], test[4], b1.__str__))
                b1.remove(test[2])
                x.determine_the_grading_method(((test[1], test[2]), test[5], b1.__str__))
                b1.add(test[3])
                x.determine_the_grading_method(((test[1], test[3]), test[6], b1.__str__()))
            except AssertionError as e:
                raise
            except Exception as e:
                # TODO: need to change the question to define message for exception
                x.determine_the_grading_method((test[1], test[7], e.__str__))

    def check(self, fn):
        self.check_testbook(fn)

class Question1C(FunctionProblem):
    _var="question1c"
    _test_cases = [
        # TODO: The testing works, but student's messages may vary because the question does not define the messages.
        (1, 1, 4, 2, 3, 0, """Number of items: 1
Number of items: 5
Number of items: 2
Thank you for using Box application\n"""),
        (5, 2, 7, 'n', 1, 0, """Number of items: 5
Box currently has 5 items. Cannot remove 7 items
Number of items: 4
Thank you for using Box application\n"""),
        (6, 1, 5, 'n', 2, 0, """Number of items: 6
Box currently has 6 items. Cannot add 5 items because 11 exceeds max 10
Number of items: 8
Thank you for using Box application\n""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for a,b,c,d,e,f, expected in self._test_cases:
            with patch('builtins.input', side_effect=[a,b,c,d,e,f]):
                out, actual = x.compare_printout(fn)
                x.determine_the_grading_method(([a,b,c,d,e,f], expected, out))
                # TODO: Check whether the test above is complete. We are check __str__ when the answer need to be filled up in question1b.
    
    def check(self, fn):
        self.check_testbook(fn)


Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C
)    
