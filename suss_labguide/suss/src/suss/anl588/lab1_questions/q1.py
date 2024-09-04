from learntools.core import *
from ...dev import x

class Question1A(EqualityCheckProblem):

    def produce_expected():
        mystr1 = ["a", "b", "c"]
        mynum1 = [0, 1, 2, 3]
        mysum = mystr1 + mynum1

        return mysum

    _var = "mysum"
    _expected = produce_expected()

    _test_cases = [
        ("a", "d", ['d', 'b', 'c', 0, 1, 2, 3]),
        (2, 4, ['a', 'b', 'c', 0, 1, 4, 3])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            source = x.get_source_code("lab1", 68)
            # print("----source----")
            # print(source)

            x.test_for_none_588(source, "lab1", 68, f"{test[0]}", f"{test[1]}", f"{test[0]}")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")
            # print("----test_source----")
            # print(test_source)

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(test_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_mysum = local_vars.get('mysum')
            x.determine_the_grading_method((test[1], test[2], executed_mysum))

class Question1B(CodingProblem):

    def produce_expected():
        mystr1 = ["a", "b", "c"]
        mynum1 = [0, 1, 2, 3]
        mysum = mystr1 + mynum1  
        expected = """<class 'str'>
<class 'int'>\n"""

        return expected

    _var="mysum"
    _expected = produce_expected()

    _test_cases = [
        ("0", "3", """<class 'int'>
<class 'int'>\n"""),
        ("4", "1", """<class 'str'>
<class 'str'>\n"""),
]

    def check(self, *args):
        source = x.get_source_code("lab1", 68) + "\n" + x.get_source_code("lab1", 71)

        # print("----source----")
        # print(source)

        # lines below : remove comments and pass + fix indentation in source code
        updated_source = x.filter_source(source, "#")
        lines = updated_source.split('\n')
        filtered_lines = [line for line in lines if not line.lstrip().startswith('pass')]
        updated_source2 = '\n'.join(['    ' + line for line in filtered_lines]) 

        fn_name = "fn"
        fn_source = f"def fn():\n{updated_source2}"
        # Execute the function definition
        exec(fn_source, globals())
        
        # Access the dynamically created function by its name
        fn = globals()[fn_name]
        out, actual = x.compare_printout(fn)

        args_escaped = ("actual", Question1B._expected.replace('<', '&lt;').replace('>', '&gt;'), out.replace('<', '&lt;').replace('>', '&gt;'))

        x.determine_the_grading_method((args_escaped))

        for test in self._test_cases:
            actual_source = x.get_source_code("lab1", 71)
            x.test_for_none_588(actual_source, "lab1", 71, test[0], test[1], "actual")
            updated_actual = x.update_x_in_code(actual_source, test[0], test[1])

            source = x.get_source_code("lab1", 68) + "\n" + updated_actual

            # print("----source----")
            # print(source)

            # lines below : remove comments and pass + fix indentation in source code
            updated_source = x.filter_source(source, "#")
            lines = updated_source.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('pass')]
            updated_source2 = '\n'.join(['    ' + line for line in filtered_lines]) 

            fn_name = "fn"
            fn_source = f"def fn():\n{updated_source2}"
            # Execute the function definition
            exec(fn_source, globals())
            
            # Access the dynamically created function by its name
            fn = globals()[fn_name]
            out, actual = x.compare_printout(fn)

            args_escaped = ("actual", test[2].replace('<', '&lt;').replace('>', '&gt;'), out.replace('<', '&lt;').replace('>', '&gt;'))

            x.determine_the_grading_method((args_escaped))


Question1 = MultipartProblem(
    Question1A,
    Question1B
)    