from learntools.core import *
from ...dev import x
import numpy as np
import matplotlib.pyplot as plt

class Question1A(EqualityCheckProblem):

    def produce_expected():
        np.random.seed(1)
        a1 = np.arange(6,11)
        a2 = np.random.randint(2,8, 2)  

        return a1, a2

    _vars = ['a1', 'a2']
    _expected = produce_expected()

    _test_cases = [
        ("6", "5", (5,11), np.arange(5, 11), "8", "7", (2,7,2), np.array([5,6])),

    ]

    def check(self, *args):
        # testing actual value of a1
        x.grading_nparray2(("a1", Question1A.produce_expected()[0], args[0]))

        # testing actual value of a2
        x.grading_nparray2(("a2", Question1A.produce_expected()[1], args[1]))

        # inserting test cases
        for test in self._test_cases:
            source = x.get_source_code("lab2b", 41)

            x.test_for_none_588(source, "lab2b", 41, f"{test[0]}", f"{test[1]}", f"a1 = np.arange({test[0]}, 11)")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"{test[1]}")

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_a1 = local_vars.get('a1')

            x.grading_nparray2((test[2], "a1", test[3], executed_a1), var="test")

            source2 = x.get_source_code("lab2b", 41)
            x.test_for_none_588(source2, "lab2b", 41, f"{test[4]}", f"{test[5]}", f"a2 = np.random.randint(2, {test[4]}, 2)")
            test_source2 = x.update_x_in_code(source2, f"{test[4]}", f"{test[5]}")

            updated_source2 = x.filter_source(test_source2, 'print')
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_a2 = local_vars.get('a2')

            x.grading_nparray2((test[6], "a2", test[7], executed_a2), var="test")
        
class Question1B(EqualityCheckProblem):

    def produce_expected():
        np.random.seed(1)
        a1 = np.arange(6,11)
        a2 = np.random.randint(2,8, 2) 
        myarray = a1*a2[0]+a1*a2[1] 

        return myarray

    _var = 'myarray'
    _expected = produce_expected()
    _test_cases = [
        ('a1', np.array([5,6,7,8,9]), np.array([60, 72, 84, 96, 108]), 'a2', 'a1', np.array([78,91,104,117,130])),
        # ('AveRooms')
        ]

    def check(self, *args):
        # testing actual value of myarray

        x.grading_nparray2(("myarray", Question1B._expected, args[0]))
        
        for test in self._test_cases:
            # testing myarray with test case replacing `a1`
            source = x.get_source_code("lab2b", 44)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 44, f"{test[0]}", f"np.array({list(test[1])})", f"myarray = {test[0]}*a2[0]+{test[0]}*a2[1]")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"np.array({list(test[1])})")
            combined_source = x.get_source_code("lab2b", 41) + "\n" + test_source 

            updated_source = x.filter_source(combined_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_myarray = local_vars.get('myarray')

            x.grading_nparray2((f"np.array(list({test[1]}))", "myarray", test[2], executed_myarray), var="test")

            # testing myarray with test case replacing `a2`
            source2 = x.get_source_code("lab2b", 44)
            x.test_for_none_588(source2, "lab2b", 44, f"{test[3]}", f"{test[4]}", f"myarray = a1*{test[3]}[0]+a1*{test[3]}[1]")
            test_source2 = x.update_x_in_code(source2, f"{test[3]}", f"{test[4]}")
            combined_source2 = x.get_source_code("lab2b", 41) + "\n" + test_source2

            updated_source2 = x.filter_source(combined_source2, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_myarray2 = local_vars.get('myarray')
            
            x.grading_nparray2(("np.array([6,7,8,9,10])", "myarray", test[5], executed_myarray2), var="test")

class Question1C(EqualityCheckProblem):

    def produce_expected():
        np.random.seed(1)
        a1 = np.arange(6,11)
        a2 = np.random.randint(2,8, 2) 
        myarray = a1*a2[0]+a1*a2[1] 
        myarray_mean = myarray.mean()

        return myarray_mean

    _var = 'myarray_mean'
    _expected = produce_expected()
    _test_cases = [
        ('a1', np.array([5,6,7,8,9]), np.array([60, 72, 84, 96, 108]).mean(), 'a2', 'a1', np.array([78,91,104,117,130]).mean()),
        # ('AveRooms')
        ]

    def check(self, *args):
        # testing actual value of mean calculated in cell
        x.grading_nparray2(("myarray_mean", Question1C._expected, args[0]))

        for test in self._test_cases:
            # testing myarray with test case replacing `a1`
            source = x.get_source_code("lab2b", 44)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 44, f"{test[0]}", f"np.array({list(test[1])})", f"myarray = {test[0]}*a2[0]+{test[0]}*a2[1]")
            test_source = x.update_x_in_code(source, f"{test[0]}", f"np.array({list(test[1])})")
            combined_source = x.get_source_code("lab2b", 41) + "\n" + test_source + x.get_source_code("lab2b", 47)

            updated_source = x.filter_source(combined_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_myarraymean = local_vars.get('myarray_mean')

            x.grading_nparray2((f"np.array(list({test[1]}))", "myarray_mean", test[2], executed_myarraymean), var="test")

            # testing myarray with test case replacing `a2`
            source2 = x.get_source_code("lab2b", 44)
            x.test_for_none_588(source2, "lab2b", 44, f"{test[3]}", f"{test[4]}", f"myarray = a1*{test[3]}[0]+a1*{test[3]}[1]")
            test_source2 = x.update_x_in_code(source2, f"{test[3]}", f"{test[4]}")
            
            combined_source2 = x.get_source_code("lab2b", 41) + "\n" + test_source2 + x.get_source_code("lab2b", 47)

            updated_source2 = x.filter_source(combined_source2, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_myarraymean2 = local_vars.get('myarray_mean')
            
            x.grading_nparray2(("np.array([6,7,8,9,10])", "myarray_mean", test[5], executed_myarraymean2), var="test")

Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C
)    