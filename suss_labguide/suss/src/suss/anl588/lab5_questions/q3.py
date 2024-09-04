from learntools.core import *
from ...dev import x
import os
import pandas as pd
from ..lab5_questions.q2 import Question2A
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
import numpy as np


class Question3A(EqualityCheckProblem):


    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        X = df.drop("default", axis=1)
        y = df.pop("default") 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=1,stratify=y)
        ab_estimator = AdaBoostClassifier(random_state=1, 
                                        n_estimators = 200, 
                                        learning_rate = 0.1)

        ab_estimator.fit(X_train, y_train)

        y_pred_ab = ab_estimator.predict(X_test)

        return y_pred_ab

    _var = 'y_pred_ab'
    _expected = produce_expected()
    
    _test_cases = [
        ('X_train', "np.random.rand(100, 5)", 'y_train', "np.random.randint(0, 2, 100)", 'X_test', "np.random.rand(50, 5)", np.array([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0])),
        ('X_train', "np.random.rand(150, 4)", 'y_train', "np.random.randint(0, 3, 150)", 'X_test', "np.random.rand(75, 4)", np.array([1, 0, 1, 2, 2, 1, 2, 2, 1, 2, 0, 0, 2, 2, 0, 0, 1, 1, 2, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 2, 0, 1, 1, 0, 2, 1, 2, 2, 1, 1, 0, 1, 1, 1, 2, 1, 0, 2, 2, 1, 1, 1, 2, 1, 0, 0, 1, 2, 0, 2, 1, 0, 0, 2, 0, 0, 1, 1, 1])),
        ('X_train', "np.random.rand(200, 3)", 'y_train', "np.random.randint(0, 4, 200)", 'X_test', "np.random.rand(100, 3)", np.array([0, 3, 0, 0, 1, 3, 1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 2, 1, 3, 3, 2, 1, 2, 1, 0, 3, 1, 1, 3, 3, 2, 3, 1, 0, 1, 2, 3, 1, 3, 1, 1, 3, 1, 3, 1, 3, 3, 0, 1, 2, 0, 1, 3, 1, 3, 2, 1, 3, 3, 1, 2, 2, 1, 2, 1, 1, 1, 0, 1, 0, 0, 3, 1, 3, 1, 3, 0, 3, 1, 1, 0, 2, 1, 0, 3, 3, 1, 0, 3, 0, 1, 2, 2, 1, 1, 1, 0, 0, 0, 0]))
]


    def check(self, *args):

        actual_source = x.get_source_code("lab5", 40)
        filtered_actual = x.filter_source(actual_source, '#')

        if "ab_estimator" in filtered_actual:
            x.justpass()
        else:
            x.justfail("ab_estimator", "`ab_estimator` is not found. Please use `ab_estimator` when you instantiate the AdaBoostClassifier.")


        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator`, to compute.")


        x.grading_nparray2(("y_pred_ab", Question3A._expected, args[0]))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 40, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 40, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 40, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_lines = """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
import numpy as np"""

            combined_source = import_lines + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_ab =  variables.get('y_pred_ab')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_ab", test[6], executed_y_pred_ab), var="test")

class Question3B(EqualityCheckProblem):

    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        X = df.drop("default", axis=1)
        y = df.pop("default") 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=1,stratify=y)

        gb_estimator = GradientBoostingClassifier(random_state = 1, 
                                                n_estimators = 200, 
                                                learning_rate = 0.1)

        gb_estimator.fit(X_train, y_train)

        y_pred_gb = gb_estimator.predict(X_test)

        return y_pred_gb

    _var = 'y_pred_gb'
    _expected = produce_expected()
    
    # TODO: if you face incorrect for the `check` in 3b, it is most likely test cases!!!!!!
    _test_cases = [
        # ('X_train', "np.random.rand(100, 5)", 'y_train', "np.random.randint(0, 2, 100)", 'X_test', "np.random.rand(50, 5)", np.array([1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0])),
        # ('X_train', "np.random.rand(150, 4)", 'y_train', "np.random.randint(0, 3, 150)", 'X_test', "np.random.rand(75, 4)", np.array([1, 0, 1, 0, 2, 1, 1, 2, 1, 2, 2, 1, 0, 1, 1, 0, 1, 1, 2, 0, 0, 2, 1, 1, 2, 0, 2, 1, 1, 2, 1, 0, 2, 0, 1, 2, 0, 1, 1, 0, 2, 1, 2, 2, 0, 0, 1, 1, 0, 1, 2, 1, 1, 2, 0, 2, 2, 1, 2, 1, 0, 0, 0, 2, 1, 1, 0, 0, 1, 2, 1, 0, 1, 1, 1])),
        # ('X_train', "np.random.rand(200, 3)", 'y_train', "np.random.randint(0, 4, 200)", 'X_test', "np.random.rand(100, 3)", np.array([1, 0, 0, 1, 2, 3, 3, 1, 2, 2, 2, 0, 3, 2, 0, 1, 2, 1, 2, 3, 2, 3, 3, 3, 3, 2, 0, 1, 3, 3, 1, 3, 1, 0, 2, 2, 1, 1, 3, 1, 1, 3, 3, 0, 0, 3, 3, 1, 1, 1, 3, 1, 0, 3, 2, 2, 3, 2, 2, 1, 2, 2, 0, 2, 0, 2, 0, 0, 3, 3, 0, 1, 3, 3, 3, 3, 0, 1, 2, 1, 0, 2, 1, 2, 3, 2, 1, 2, 2, 1, 0, 3, 2, 0, 0, 2, 3, 1, 2, 3]))
    # Test case 1
    ('X_train', "np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])", 
     'y_train', "np.array([0, 1, 0, 1])", 
     'X_test', "np.array([[21, 22, 23, 24, 25], [26, 27, 28, 29, 30], [31, 32, 33, 34, 35], [36, 37, 38, 39, 40]])", 
     np.array([1, 1, 1, 1])),

    # Test case 2
    ('X_train', "np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])", 
     'y_train', "np.array([0, 1, 2, 0, 1, 2])", 
     'X_test', "np.array([[25, 26, 27, 28], [29, 30, 31, 32], [33, 34, 35, 36]])", 
     np.array([2, 2, 2])),

    # Test case 3
    ('X_train', "np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]])", 
     'y_train', "np.array([0, 1, 2, 3, 0, 1, 2])", 
     'X_test', "np.array([[22, 23, 24], [25, 26, 27], [28, 29, 30], [31, 32, 33]])", 
     np.array([2, 2, 2, 2]))
]


    def check(self, *args):

        actual_source = x.get_source_code("lab5", 47)
        filtered_actual = x.filter_source(actual_source, '#')
        
        if "gb_estimator" in filtered_actual:
            x.justpass()
        else:
            x.justfail("gb_estimator", "`gb_estimator` is not found. Please use `gb_estimator` when you instantiate the GradientBoostingClassifier.")

        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator`, to compute.")


        x.grading_nparray2(("y_pred_gb", Question3B._expected, args[0]))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 47, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 47, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 47, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_lines = """import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np"""

            combined_source = import_lines + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_gb =  variables.get('y_pred_gb')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_gb", test[6], executed_y_pred_gb), var="test")


Question3 = MultipartProblem(
    Question3A, 
    Question3B
)
