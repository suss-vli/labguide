from learntools.core import *
from ...dev import x

class Question3A(EqualityCheckProblem):

    def produce_expected():
        ex3 = list(range(1,11))
        
        return ex3

    _var = "ex3"
    _expected = produce_expected()

    _test_cases = [
        (1, 11, 2, 8, [2, 3, 4, 5, 6, 7])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            source = x.get_source_code("lab1", 104)

            # test 1 for range(1,11)
            x.test_for_none_588(source, "lab1", 104, f"{test[0]},{test[1]}",f"{test[2]},{test[3]}", f"ex3 = list(range({test[0]},{test[1]}))")
            test_source = x.update_x_in_code(source, f"{test[0]},{test[1]}", f"{test[2]},{test[3]}")
            # print("----test_source----")
            # print(test_source)

            # lines = test_source.split('\n')
            # filtered_lines = [line for line in lines if not line.lstrip().startswith('print')]
            # updated_source = '\n'.join(filtered_lines)   

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_ex3 = local_vars.get('ex3')
            x.determine_the_grading_method(((test[2],test[3]), test[4], executed_ex3))


class Question3B(EqualityCheckProblem):

    def produce_expected():
        ex3 = list(range(1,11))
        ex3a = ex3[2:5]
        return ex3a
    
    _var = "ex3a"
    _expected = produce_expected()

    _test_cases = [
        (2, 5, 1, 4, [2, 3, 4])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            #getting all source code cells for q1a
            source = x.get_multiple_cell_source("lab1", [104,107])

            x.test_for_none_588(source, "lab1", 107, f"{test[0]}:{test[1]}",f"{test[2]}:{test[3]}", f"ex3a = ex3[{test[0]}:{test[1]}]")
            test_source = x.update_x_in_code(source, f"{test[0]}:{test[1]}", f"{test[2]}:{test[3]}")
            # print("----test_source----")
            # print(test_source)
            
            # lines = test_source.split('\n')
            # filtered_lines = [line for line in lines if not line.lstrip().startswith('print')]
            # updated_source2 = '\n'.join(filtered_lines)   

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_ex3a = local_vars.get('ex3a')
            x.determine_the_grading_method(((f"{test[2]}:{test[3]}"), test[4], executed_ex3a))

class Question3C(EqualityCheckProblem):

    def produce_expected():
        ex3 = list(range(1,11))
        ex3a = ex3[2:5]
        ex3a.reverse()
        
        return ex3a

    _var = "ex3a"
    _expected = produce_expected()

    _test_cases = [
        (1, 11, 2, 8, [6, 5, 4], 2, 5, 1, 4, [4, 3, 2])
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
                
            #getting all source code cells for q1a
            source = x.get_multiple_cell_source("lab1", [104,107,110])
            # print("----source----")
            # print(source)

            # test 1 for range(1,11)
            x.test_for_none_588(source, "lab1", 104, f"{test[0]},{test[1]}",f"{test[2]},{test[3]}", f"ex3 = list(range({test[0]},{test[1]}))")
            test_source = x.update_x_in_code(source, f"{test[0]},{test[1]}", f"{test[2]},{test[3]}" )
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
    
            executed_ex3a = local_vars.get('ex3a')
            x.determine_the_grading_method(((test[2],test[3]), test[4], executed_ex3a))

            # test 2 for ex2a = ex2[2:5]
            x.test_for_none_588(source, "lab1", 107, f"{test[5]}:{test[6]}",f"{test[7]}:{test[8]}", f"ex3a = ex3[{test[5]}:{test[6]}]")
            test_source2 = x.update_x_in_code(source, f"{test[5]}:{test[6]}", f"{test[7]}:{test[8]}")
            # print("----test_source2----")
            # print(test_source2)

            updated_source2 = x.filter_source(test_source2, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_ex3a = local_vars.get('ex3a')
            x.determine_the_grading_method(((f"{test[7]}:{test[8]}"), test[9], executed_ex3a))

Question3 = MultipartProblem(
    Question3A,
    Question3B,
    Question3C
)    