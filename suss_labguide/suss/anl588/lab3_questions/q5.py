from learntools.core import *
from ...dev import x
import pandas as pd
from ..lab3_questions.q3 import Question3A
from sklearn.model_selection import train_test_split

class Question5(EqualityCheckProblem):

    def produce_expected(data1 = 0.3, data2 = 101):
        df2 = Question3A._expected
        df2 = df2.drop('lwage', axis = 1)
        X = df2.drop('wage' , axis = 1)
        y = df2['wage' ]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = data1, random_state = data2)
        
        return X_train, X_test, y_train, y_test

    _vars = ['X_train', 'X_test', 'y_train', 'y_test']
    _expected = produce_expected()

    _test_cases = [ 
        ('0.3', '0.1', 'test_size', produce_expected(0.1, 101)),
        ('101', '100', 'random_state', produce_expected(0.3, 100))
    ]

    def check(self, *args):

        # testing actual value of X_train
        x.grading_df_series(("X_train", Question5._expected[0], args[0]))

        # testing actual value of X_test
        x.grading_df_series(("X_test", Question5._expected[1], args[1]))

        # testing actual value of y_train
        x.grading_df_series(("y_train", Question5._expected[2], args[2]))

        # testing actual value of y_test
        x.grading_df_series(("y_test", Question5._expected[3], args[3]))

        source = x.get_source_code("lab3", 43) + "\n" + x.get_source_code("lab3", 44)
        updated_source = x.filter_source(source, '#')
        
        if "from sklearn.model_selection import train_test_split" in updated_source:
            x.justpass()
        else:
            x.justfail("from sklearn.model_selection import train_test_split", "`from sklearn.model_selection import train_test_split` is not found. Please import train_test_split from sklearn.model_selection.")
        

        for test in self._test_cases:
            x.test_for_none_588(updated_source, "lab4", 43, test[0], test[1], "X_train, X_test, y_train, y_test")
            test_source = x.update_x_in_code(updated_source, test[0], test[1])

            source2 = x.get_multiple_cell_source("lab3", [10, 31, 34, 39])

            updated_source2 = x.filter_source(source2, '#')
            
            combined_source = updated_source2 + "\n" + test_source
        
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(combined_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_X_train = local_vars.get('X_train')
            executed_X_test = local_vars.get('X_test')
            executed_y_train = local_vars.get('y_train')
            executed_y_test = local_vars.get('y_test')
  
            x.grading_df_series((f"{test[2]} = {test[1]}", "X_train", test[3][0], executed_X_train), var="test")
            x.grading_df_series((f"{test[2]} = {test[1]}", "X_test", test[3][1], executed_X_test), var="test")

            x.grading_df_series((f"{test[2]} = {test[1]}", "y_train", test[3][2], executed_y_train), var="test")
            x.grading_df_series((f"{test[2]} = {test[1]}", "y_test", test[3][3], executed_y_test), var="test")