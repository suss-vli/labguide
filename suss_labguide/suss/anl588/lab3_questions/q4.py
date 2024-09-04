from learntools.core import *
from ...dev import x
import pandas as pd
from ..lab3_questions.q3 import Question3A

class Question4(EqualityCheckProblem):

    def produce_expected(data):
        df2 = Question3A._expected
        df2 = df2.drop('lwage', axis = 1)
        X = df2.drop(f'{data}' , axis = 1)
        y = df2[f'{data}' ]

        
        return X, y

    _vars = ["X", "y"]
    _expected = produce_expected('wage')

    _test_cases = [ 
        ('wage', 'exper', produce_expected('exper'))
    ]

    def check(self, *args):

        # testing actual value of X
        x.grading_df_series(("X", Question4._expected[0], args[0]))

        # testing actual value of y
        x.grading_df_series(("y", Question4._expected[1], args[1]))

        for test in self._test_cases:
            source = x.get_source_code("lab3", 39)

            updated_source = x.filter_source(source, '#')
        
            # replace 'wage'
            x.test_for_none_588(source, "lab3", 39, test[0], test[1], "X, y")
            source2 = x.update_x_in_code(updated_source, test[0], test[1])
            
            combined_source = x.get_source_code("lab3", 10) + "\n" + x.get_source_code("lab3", 31) + "\n" + x.get_source_code("lab3", 34) + "\n" + source2
                      
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(combined_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_X = local_vars.get('X')
            x.determine_the_grading_method((f"X = df2.drop('{test[1]}')", test[2][0], executed_X))

            executed_y = local_vars.get('y')

            x.grading_df_series((test[1], "y", test[2][1], executed_y), var="test")