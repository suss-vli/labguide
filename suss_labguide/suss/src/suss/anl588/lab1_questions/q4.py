from learntools.core import *
from ...dev import x

class Question4A(EqualityCheckProblem):

    def produce_expected():
        mylist = list(range(0,8))
        mylist4 = [num % 2 == 0 for num in mylist]
        
        return mylist4

    _var = "mylist4"
    _expected = produce_expected()

    _test_cases = [
        (2, 3, [True, False, False, True, False, False, True, False]),
        (2, 1, [True, True, True, True, True, True, True, True])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            #getting all source code cells for q1a
            source = x.get_multiple_cell_source("lab1", [115,121])
            # print("----source----")
            # print(source)

            x.test_for_none_588(source, "lab1", 121, f"{test[0]}", f"{test[1]}", f"mylist4 = [num % {test[0]} == 0 for num in mylist]")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")
            # print("----test_source----")
            # print(test_source)   

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_mylist4 = local_vars.get('mylist4')
            x.determine_the_grading_method((test[1], test[2], executed_mylist4))

class Question4B(EqualityCheckProblem):

    def produce_expected():
        mylist = list(range(0,8))
        mylist4 = [num for num in mylist if num % 2 != 0]
        
        return mylist4

    _var = "mylist4"
    _expected = produce_expected()

    _test_cases = [
        (2, 3, [1, 2, 4, 5, 7]),
        (2, 1, [])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            #getting all source code cells for q1a
            source = x.get_multiple_cell_source("lab1", [115,124])
            # print("----source----")
            # print(source)

            x.test_for_none_588(source, "lab1", 124, f"{test[0]}", f"{test[1]}", f"mylist4 = [num for num in mylist if num % {test[0]} != 0]")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")
            # print("----test_source----")
            # print(test_source)

            updated_source = x.filter_source(test_source, 'print') 

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_mylist4 = local_vars.get('mylist4')
            x.determine_the_grading_method((test[1], test[2], executed_mylist4))

Question4 = MultipartProblem(
    Question4A,
    Question4B
)    