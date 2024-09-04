from learntools.core import *
from ...dev import x
import pandas as pd
from ..lab3_questions.q1 import Question1

class Question3A(EqualityCheckProblem):

    def produce_expected():
        df = Question1._expected
        df2 = df.copy()

        return df2

    _var = 'df2'
    _expected = produce_expected()

    # TODO: test cases below are not for q3a, not sure what test_cases should be input
    _test_cases = [
        ([75, 56, 64, 82, 89], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], pd.Series([0, 0, 0, 0, 0]), [84, 47, 61, 72, 80], pd.Series([84, 47, 61, 72, 80])),
        ([84, 47, 61, 72, 80], [0, 0, 0, 0, 0], [75, 56, 64, 82, 89], pd.Series([75, 56, 64, 82, 89]), [0, 0, 0, 0, 0], pd.Series([0, 0, 0, 0, 0]))
    ]

    def check(self, *args):
        # testing actual value of df2
        x.grading_df_series(("df2", Question3A._expected, args[0]))

        source = x.get_source_code("lab3", 31)

        updated_source = x.filter_source(source, '#')
        
        if "df.copy" in updated_source:
            x.justpass()
        else:
            x.justfail("df.copy", "`df.copy` is not used. Please use `df.copy` to make a copy of `df`.")
            
class Question3B(EqualityCheckProblem):

    def produce_expected(data):        
        df = Question1._expected
        df2 = df.copy()
        df2 = df2.drop(f'{data}', axis = 1)

        return df2

    _var = 'df2'
    _expected = produce_expected("lwage")

    _test_cases = [
        ("lwage", "wage", produce_expected("wage"))
    ]

    def check(self, *args):
        # testing actual value of df2
        x.grading_df_series(("df2", Question3B._expected, args[0]))

        source = x.get_source_code("lab3", 34)

        updated_source = x.filter_source(source, '#')
        
        if "df2.drop" in updated_source:
            x.justpass()
        else:
            x.justfail("df2.drop", "`df2.drop` is not detected. Please use `df2.drop`.")
        if "inplace" not in updated_source:
            x.justpass()
        else:
            x.justfail("inplace = True", "Avoid using `inplace = True` in the `.drop()` method.")
        
        for test in self._test_cases:
            # replace 'lwage'
            x.test_for_none_588(source, "lab3", 34, test[0], test[1], "df2")
            source2 = x.update_x_in_code(updated_source, test[0], test[1])
            
            combined_source = x.get_source_code("lab3", 10) + "\n" + x.get_source_code("lab3", 31) + "\n" + source2
                      
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(combined_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_df2 = local_vars.get('df2')
            x.grading_df_series((f"df2.drop('{test[1]}')", "df2", executed_df2, test[2]), var="test")

Question3 = MultipartProblem(
    Question3A,
    Question3B
)    