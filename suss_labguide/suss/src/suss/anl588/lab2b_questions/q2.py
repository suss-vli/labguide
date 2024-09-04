from learntools.core import *
from ...dev import x
import numpy as np
import pandas as pd

class Question2A(EqualityCheckProblem):

    def produce_expected():
        np.random.seed(1)
        math = np.random.randint(45, 99, 5)
        science = np.random.randint(45, 99, 5)
        
        return math, science

    _vars = ['math', 'science']
    _expected = produce_expected()

    _test_cases = [
        ("45", "1", (1,99,5), np.array([38,13,73,10,76]), np.array([6,80,65,17,2])), 
        ("99", "80", (45,80,5), np.array([57,53,54,56,50]), np.array([60,45,61,46,57])), 
        ("5", "4", (45,99,4), np.array([82,88,57,53]), np.array([54,56,50,60])),
        ("1", "2", "np.random.seed(2)", np.array([85,60,90,53,67]), np.array([88,63,56,85,52]))
    ]

    def check(self, *args):
        # testing actual value of math
        x.grading_nparray2(("math", Question2A._expected[0], args[0]))
        
        # testing actual value of science
        x.grading_nparray2(("science", Question2A._expected[1], args[1]))

        # inserting test cases
        for test in self._test_cases:

            #replacing 45 / 99/ 5 / 1
            source = x.get_source_code("lab2b", 60)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 60, test[0], test[1], test[0])
            test_source = x.update_x_in_code(source, test[0], test[1])
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
    
            executed_math = local_vars.get('math')
            executed_science = local_vars.get('science')

            #assert executed_math 
            x.grading_nparray2((test[2], "math", test[3], executed_math),var="test")

            # assert executed_science 
            x.grading_nparray2((test[2], "science", test[4], executed_science), var="test")

class Question2B(EqualityCheckProblem):

    def produce_expected():
        classnames = ['Abruzzo', 'Todi', 'Umbria', 'Raiano', 'Molise']

        return classnames

    _var = 'classnames'
    _expected = produce_expected()
    _test_cases = [
        ('Abruzzo', 'Apple', ['Apple', 'Todi', 'Umbria', 'Raiano', 'Molise']),
        ('Todi', 'Tomato', ['Abruzzo', 'Tomato', 'Umbria', 'Raiano', 'Molise']),
        ('Umbria', 'Ume', ['Abruzzo', 'Todi', 'Ume', 'Raiano', 'Molise']),
        ('Raiano', 'Raisin', ['Abruzzo', 'Todi', 'Umbria', 'Raisin', 'Molise']),
        ('Molise', 'Mango', ['Abruzzo', 'Todi', 'Umbria', 'Raiano', 'Mango'])
        ]

    def check(self, *args):
        # testing actual value of classnames       
        x.grading_equal(("classnames", Question2B._expected, args[0]))

        for test in self._test_cases:

            source = x.get_source_code("lab2b", 63)

            x.test_for_none_588(source, "lab2b", 63, test[0], test[1], "classnames")
            test_source = x.update_x_in_code(source, test[0], test[1])

            
            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}

            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_classnames = local_vars.get('classnames')
            x.grading_equal((test[1], "classnames", test[2], executed_classnames), var="test")

class Question2C(EqualityCheckProblem):

    def produce_expected():
        np.random.seed(1)
        math = np.random.randint(45, 99, 5)
        science = np.random.randint(45, 99, 5)

        classnames = ['Abruzzo', 'Todi', 'Umbria', 'Raiano', 'Molise']

        math = pd.Series(math)
        science = pd.Series(science)
        math.index = classnames
        science.index = classnames

        return math, science

    _vars = ['math', 'science']
    _expected = produce_expected()
    _test_cases = [
        ('(math)', '(np.array([1,1,1,1,1]))', (pd.Series({'Abruzzo': 1, 'Todi': 1, 'Umbria': 1, 'Raiano': 1, 'Molise': 1})), '(np.array([56,50,60,45,61]))', (pd.Series({'Abruzzo': 56, 'Todi': 50, 'Umbria': 60, 'Raiano': 45, 'Molise': 61})))
        # ('AveRooms')
        ]

    def check(self, *args):  
        # testing actual value of math
        x.grading_df_series(("math", Question2C._expected[0], args[0]))
                           
        # testing actual value of science
        x.grading_df_series(("science", Question2C._expected[1], args[1]))

        for test in self._test_cases:
            source = x.get_source_code("lab2b", 66)
            if "pd.Series(math)" in source:
                x.justpass()
            else:
                x.justfail("pd.Series", "`pd.Series` is not used to convert `math`. Please use pandas series to convert `math`: `pd.Series(math)`.")
            
            if "pd.Series(science)" in source:
                x.justpass()
            else:
                x.justfail("pd.Series", "`pd.Series` is not used to convert `science`. Please use pandas series to convert `science`: `pd.Series(science)`.")
            if "math.index" in source:
                x.justpass()
            else:
                x.justfail("math.index", "`.index` is not used to assign `classnames` as index. Please use `.index`: `math.index`.")
            
            if "science.index" in source:
                x.justpass()
            else:
                x.justfail("science.index", "`.index` is not used to assign `classnames` as index. Please use `.index`: `science.index`.")

            x.test_for_none_588(source, "lab2b", 66, test[0], test[1], f"pd.Series{test[0]}")
            test_source = x.update_x_in_code(source, test[0], test[1])

            combined_source = x.get_source_code("lab2b", 60) + "\n" + x.get_source_code("lab2b", 63) + "\n" + test_source

            updated_source = x.filter_source(combined_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_math = local_vars.get('math')
            executed_science = local_vars.get('science')

            x.grading_df_series((test[1], "math", test[2], executed_math), var="test")
            x.grading_df_series((test[3], "science", test[4], executed_science), var="test")
        
Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C
)    