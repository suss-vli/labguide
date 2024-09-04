from learntools.core import *
from ...dev import x
from sklearn.linear_model import LinearRegression
import numpy as np
from ..lab3_questions.q5 import Question5

class Question8(EqualityCheckProblem):

    def produce_expected():
        
        model = LinearRegression()
        X_train, X_test, y_train, y_test = Question5._expected
        train_model = model.fit(X_train, y_train)
        
        return train_model

    _var = "train_model"
    _expected = produce_expected()

    _test_cases = [ 
        ('y_train', 'X_train', LinearRegression().fit(Question5._expected[0], Question5._expected[0]))
    ]

    def check(self, *args):
        # testing actual 
        actual_source = x.get_source_code("lab3", 57)
        filtered_actual_source = x.filter_source(actual_source, '#')

        previous = x.get_multiple_cell_source("lab3", [10, 31, 34, 39, 43, 44, 53])
        combined_source = "import pandas as pd\n" + previous + "\n" + filtered_actual_source
        
        updated_source = x.filter_source(combined_source, '#')

        # Create a dictionary to capture the local variables and assessment results
        local_vars = {}
        
        # Execute the code in test_source within the local_vars context
        try:
            exec(updated_source, None, local_vars)
        except Exception as e:
            print(f"Error executing code: {e}")
            raise e
        
        executed_train_model = local_vars.get('train_model')
        
        # Compare attributes
        attributes_to_compare = ['coef_', 'intercept_']  # these 2 attributes are the one producing a difference when the data is different

        # Assuming Question8._expected and executed_train_model are arrays
        for attr in attributes_to_compare:
            x.grading_nparray2((f"train_model.{attr}", getattr(Question8._expected, attr), getattr(executed_train_model, attr)))

        for test in self._test_cases:
            
            x.test_for_none_588(filtered_actual_source, "lab3", 57, test[0], test[1], "train_model")
            test_source = x.update_x_in_code(filtered_actual_source, test[0], test[1])
            combined_source2 = "import pandas as pd\n" + previous + "\n" + test_source

            updated_source2 = x.filter_source(combined_source2, '#')
                    
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
        
            executed_train_model2 = local_vars.get('train_model')
            # Compare attributes
            attributes_to_compare = ['coef_', 'intercept_']  # these 2 attributes are the one producing a difference when the data is different

            # Assuming Question8._expected and executed_train_model are arrays
            for attr in attributes_to_compare:
                # print(f"Comparing attribute '{attr}'")
                # print(f"executed_train_model: {getattr(executed_train_model, attr)}")
                # print(f"Question8._expected: {getattr(Question8._expected, attr)}")
                x.grading_nparray2((f"{test_source}", f"train_model.{attr}", getattr(test[2], attr), getattr(executed_train_model2, attr)), var="test")