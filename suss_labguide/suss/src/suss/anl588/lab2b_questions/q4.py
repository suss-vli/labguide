from learntools.core import *
from ...dev import x
import pandas as pd
from . import q3

class Question4A(EqualityCheckProblem):

    def produce_expected():
        s1 = pd.Series([75, 56, 64, 82, 89])
        s2 = pd.Series([84, 47, 61, 72, 80])
        name_id = pd.Series(["Abe", "Ben", "Carl", "Dee", "Eun"])
        subject_id = pd.Series(["Stat","Math"])
        scores = pd.concat([s1, s2], axis = 1)
        scores.index = name_id
        scores.columns = subject_id 
        Total = scores.sum(axis = 1)
        Average1 = Total/2

        
        return Total, Average1

    _vars = ["Total", "Average1"]
    _expected = produce_expected()

    _test_cases = [ 
        ("1", "0", (pd.Series([366, 344], index=['Stat', 'Math'])), (pd.Series({'Stat': 183.0, 'Math': 172.0})))
        # (1, [True, True, True, True, True, True, True, True])
    ]

    def check(self, *args):

        # testing actual value of Total
        x.grading_df_series(("Total", Question4A._expected[0], args[0]))

        # testing actual value of Average1
        x.grading_df_series(("Average1", Question4A._expected[1], args[1]))

        for test in self._test_cases:
            actual_source = x.get_source_code("lab2b", 139)
            
            x.test_for_none_588(actual_source, "lab2b", 139, test[0], test[1], f"Total = scores.sum(axis = {test[0]})")
            updated_source = x.update_x_in_code(actual_source, test[0], test[1])

            source = x.get_multiple_cell_source("lab2b", [92, 95, 98, 139])
            test_source = source + "\n" + updated_source

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_Total = local_vars.get('Total')
            executed_Average1 = local_vars.get('Average1')

            x.grading_df_series((f"axis = {test[1]}", "Total", test[2], executed_Total), var="test")

            x.grading_df_series((f"axis = {test[1]}", "Average1", test[3], executed_Average1), var="test")

class Question4B(EqualityCheckProblem):

    def produce_expected():
        s1 = pd.Series([75, 56, 64, 82, 89])
        s2 = pd.Series([84, 47, 61, 72, 80])
        name_id = pd.Series(["Abe", "Ben", "Carl", "Dee", "Eun"])
        subject_id = pd.Series(["Stat","Math"])
        scores = pd.concat([s1, s2], axis = 1)
        scores.index = name_id
        scores.columns = subject_id 
        Total = scores.sum(axis = 1)
        Average1 = Total/2
        Average2 = scores.mean(axis=1)
        
        return Average1, Average2

    _vars = ["Average1", "Average2"]
    _expected = produce_expected()

    _test_cases = [
        ('mean', 'sum', (pd.Series({'Abe': 159, 'Ben': 103, 'Carl': 125, 'Dee': 154, 'Eun': 169})), (pd.Series({'Abe': False, 'Ben': False, 'Carl': False, 'Dee': False, 'Eun': False}))),
        ('mean', 'min', (pd.Series({'Abe': 75, 'Ben': 47, 'Carl': 61, 'Dee': 72, 'Eun': 80})), (pd.Series({'Abe': False, 'Ben': False, 'Carl': False, 'Dee': False, 'Eun': False})))
    ]

    def check(self, *args):

         # testing actual 
        x.grading_df_series(("Average2", Question4B._expected[1], args[1]))
        x.grading_df_series(("Average1 == Average2", Question4B._expected[0] == Question4B._expected[1], args[0] == args[1]))

        for test in self._test_cases:
            # get source code for cell 4b
            answer_source = x.get_source_code("lab2b", 142)
            x.test_for_none_588(answer_source, "lab2b", 142, test[0], test[1], f"Total = scores.{test[0]}(axis=1)")
            updated_source = x.update_x_in_code(answer_source, test[0], test[1])

            # get all other sources
            source = x.get_multiple_cell_source("lab2b", [92, 95, 98, 139])
            
            test_source = source + "\n" + updated_source
            updated_source = x.filter_source(test_source, 'print')
 
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_Average1 = local_vars.get('Average1')
            executed_Average2 = local_vars.get('Average2')

            x.grading_df_series((f"Average2 = sources.{test[1]}(axis=1)", "Average2", test[2], executed_Average2), var="test")
            x.grading_df_series((f"Average2 = sources.{test[1]}(axis=1)", "Average1 == Average2", test[3], executed_Average1 == executed_Average2), var="test")

Question4 = MultipartProblem(
    Question4A,
    Question4B
)    