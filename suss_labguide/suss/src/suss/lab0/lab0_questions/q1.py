from learntools.core import *
from ...dev import x


class Question1(EqualityCheckProblem):
    _var="test"
    _expected = "hello"
    _test_cases = [
        ("hello", "bye", "bye"),
        # (12, -11.11),
        # (100000, 55537.78), 
        # (0, -17.78)
    ]

    def check(self, *args):
        super().check(*args)
        for test in self._test_cases:
            source = x.get_source_code("lab0", 7)
            x.test_for_none_588(source, "lab0", 7, f"{test[0]}", f"{test[1]}", "test")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")
            local_vars = {}
            try:
                exec(test_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            executed_question1 = local_vars.get('test')
            x.determine_the_grading_method(("test", test[2], executed_question1))
