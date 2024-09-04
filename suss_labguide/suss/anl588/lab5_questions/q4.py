from learntools.core import *
from ...dev import x
import os
import re
import pandas as pd
from ..lab5_questions.q2 import Question2A
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
import numpy as np
from sklearn.metrics import recall_score, make_scorer, precision_score, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier




class Question4A(EqualityCheckProblem):

    np.random.seed(0)
    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        X = df.drop("default", axis=1)
        y = df.pop("default") 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=1,stratify=y)

        np.random.seed(0)
        ab_estimator_tuned = AdaBoostClassifier(random_state=1)

        parameters = {
            "base_estimator":[DecisionTreeClassifier(max_depth=1),DecisionTreeClassifier(max_depth=2),
                            DecisionTreeClassifier(max_depth=3)],
            "n_estimators": np.arange(100, 1000, 100),
            "learning_rate": np.arange(0.05, 0.5, 0.05)
        }

        scorer = make_scorer(recall_score)
        
        # line 39 is where we need to patch, see here: https://github.com/suss-vli/suss/blob/9a64ff839e0049e3f23b443f0ab0f78ab54e4e68/src/suss/ict133/lab2_questions/q3.py#L17
        grid_obj = RandomizedSearchCV(ab_estimator_tuned, parameters, scoring=scorer, cv=5) #5-fold CV
        grid_obj = grid_obj.fit(X_train, y_train)

        ab_estimator_tuned = grid_obj.best_estimator_

        ab_estimator_tuned.fit(X_train, y_train)

        y_pred_ab_t = ab_estimator_tuned.predict(X_test)

        return y_pred_ab_t

    _var = 'y_pred_ab_t'
    _expected = produce_expected()

    # TODO: if you face incorrect for the `check` in 3b, it is most likely test cases!!!!!!
    _test_cases = [
        # ('X_train', "np.random.rand(100, 5)", 'y_train', "np.random.randint(0, 2, 100)", 'X_test', "np.random.rand(50, 5)", np.array([1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1])),
        # ('X_train', "np.random.rand(150, 4)", 'y_train', "np.random.randint(0, 3, 150)", 'X_test', "np.random.rand(75, 4)", np.array([0, 1, 1, 1, 1, 0, 2, 2, 0, 2, 1, 1, 1, 1, 0, 2, 2, 0, 1, 0, 1, 2, 2, 2, 0, 0, 0, 2, 0, 0, 1, 0, 0, 1, 1, 2, 1, 1, 2, 1, 0, 1, 0, 0, 2, 1, 2, 0, 2, 1, 1, 2, 2, 1, 2, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 1, 0, 0, 0, 2, 2, 2, 1, 1])),
        # ('X_train', "np.random.rand(200, 3)", 'y_train', "np.random.randint(0, 4, 200)", 'X_test', "np.random.rand(100, 3)", np.array([0, 0, 3, 3, 0, 3, 3, 1, 3, 1, 3, 3, 1, 1, 3, 3, 3, 3, 0, 3, 0, 0, 2, 0, 2, 0, 2, 1, 2, 3, 2, 0, 3, 1, 1, 2, 2, 3, 3, 1, 1, 0, 3, 3, 1, 1, 1, 0, 0, 3, 0, 1, 0, 3, 3, 3, 1, 2, 1, 0, 1, 3, 1, 0, 1, 3, 3, 3, 0, 3, 1, 1, 0, 0, 0, 0, 2, 3, 1, 0, 1, 1, 2, 0, 3, 3, 3, 3, 3, 0, 3, 1, 3, 1, 1, 1, 0, 3, 3, 3]))
        ('X_train', "np.array([[0.1, 0.2, 0.3, 0.4, 0.5], [0.5, 0.4, 0.3, 0.2, 0.1], [0.6, 0.7, 0.8, 0.9, 1.0], [1.0, 0.9, 0.8, 0.7, 0.6], [0.3, 0.3, 0.3, 0.3, 0.3], [0.1, 0.2, 0.3, 0.4, 0.5], [0.5, 0.4, 0.3, 0.2, 0.1], [0.6, 0.7, 0.8, 0.9, 1.0], [1.0, 0.9, 0.8, 0.7, 0.6], [0.3, 0.3, 0.3, 0.3, 0.3]])", 
        'y_train', "np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])", 
        'X_test', "np.array([[0.2, 0.3, 0.4, 0.5, 0.6], [0.6, 0.5, 0.4, 0.3, 0.2]])", 
        np.array([0, 0])),
        
        ('X_train', "np.array([[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [8, 7, 6, 5], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [5, 5, 5, 5], [6, 6, 6, 6]])", 
        'y_train', "np.array([0, 1, 1, 0, 1, 0, 1, 0, 1, 0])", 
        'X_test', "np.array([[2, 3, 4, 5], [5, 4, 3, 2]])", 
        np.array([0, 1])),
        
        ('X_train', "np.array([[0, 0, 1], [1, 1, 0], [0, 1, 0], [1, 0, 1], [0, 0, 0], [1, 1, 1], [0, 1, 1], [1, 0, 0], [0, 1, 1], [1, 0, 0]])", 
        'y_train', "np.array([0, 1, 1, 0, 0, 1, 1, 0, 1, 0])", 
        'X_test', "np.array([[0, 1, 1], [1, 0, 0]])", 
        np.array([1, 0]))
    ]


    def check(self, *args):

        actual_source = x.get_source_code("lab5", 56)
        filtered_actual = x.filter_source(actual_source, '#')
        
        if "100" and "1000" in filtered_actual:
            x.justpass()
        else:
            x.justfail("100, 1000, 100", "`(100, 1000, 100)` parameter is not found. Please use specify the correct parameter for `n_estimators`.")
        
        if "0.05" and "0.5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("0.05, 0.5, 0.05", "`(0.05, 0.5, 0.05)` parameter is not found. Please use specify the correct parameter for `learning_rate`.")

        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator_tuned`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator_tuned`, to compute.")
        
        previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
        filtered_previous = x.filter_source(previous, '#')

        import_source = x.get_source_code("lab5", 4)
        filtered_import_source = x.filter_source(import_source, "%")

        combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + filtered_actual
       
        variables = {}
        exec(combined_source, globals(), variables)
        
        executed_y_pred_ab_t =  variables.get('y_pred_ab_t')

        x.grading_nparray2(("y_pred_ab_t", Question4A._expected, executed_y_pred_ab_t))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 56, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 56, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 56, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_source = x.get_source_code("lab5", 4)
            filtered_import_source = x.filter_source(import_source, "%")

            combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_ab_t2 =  variables.get('y_pred_ab_t')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_ab_t", test[6], executed_y_pred_ab_t2), var="test")


class Question4B(EqualityCheckProblem):

    def produce_expected():
        df = Question2A.produce_expected('test_credit.csv')
        X = df.drop("default", axis=1)
        y = df.pop("default") 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30, random_state=1,stratify=y)

        np.random.seed(0)
        gb_estimator_tuned = GradientBoostingClassifier(random_state = 1)

        parameters = {
            "max_depth": np.arange(1, 5), # We want to range from 1 to 4, but this is not correct.
            "n_estimators": np.arange(100, 1000, 100),
            "learning_rate": np.arange(0.05, 0.5, 0.05) 
        }

        scorer = make_scorer(recall_score)

        grid_obj = RandomizedSearchCV(gb_estimator_tuned, parameters, scoring=scorer, cv=5)
        grid_obj = grid_obj.fit(X_train, y_train)

        gb_estimator_tuned = grid_obj.best_estimator_

        gb_estimator_tuned.fit(X_train, y_train)

        y_pred_gb_t = gb_estimator_tuned.predict(X_test)

        return y_pred_gb_t

    _var = 'y_pred_gb_t'
    _expected = produce_expected()

    _test_cases = [
        ('X_train', "np.random.rand(100, 5)", 'y_train', "np.random.randint(0, 2, 100)", 'X_test', "np.random.rand(50, 5)", np.array([1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1])),
        ('X_train', "np.random.rand(150, 4)", 'y_train', "np.random.randint(0, 3, 150)", 'X_test', "np.random.rand(75, 4)", np.array([2, 1, 1, 2, 2, 0, 2, 1, 1, 1, 1, 1, 0, 2, 0, 2, 1, 1, 1, 0, 2, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 2, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 2, 1, 1])),
        ('X_train', "np.random.rand(200, 3)", 'y_train', "np.random.randint(0, 4, 200)", 'X_test', "np.random.rand(100, 3)", np.array([2, 2, 3, 3, 2, 2, 2, 1, 1, 0, 0, 0, 2, 2, 1, 3, 2, 2, 3, 2, 2, 3, 2, 3, 3, 2, 1, 3, 2, 2, 3, 2, 3, 1, 1, 2, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 0, 3, 2, 3, 3, 2, 1, 1, 1, 2, 0, 1, 1, 0, 0, 1, 2, 2, 1, 3, 2, 0, 1, 1, 0, 0, 3, 2, 3, 1, 0, 0, 0, 0, 1, 2, 1, 2, 2, 3, 1, 0, 1, 0, 3, 1, 3, 3, 3, 2, 3, 0, 1, 3]))
]

    def check(self, *args):

        actual_source = x.get_source_code("lab5", 65)
        filtered_actual = x.filter_source(actual_source, '#')
        
        if "max_depth" in filtered_actual:
            x.justpass()
        else:
            x.justfail("max_depth", "`max_depth` is not found. Please use specify the correct parameter for `max_depth`.")
        
        if "1,5" or "1, 5" or "1 , 5" or "1 ,5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("1, 5", "`np.arange(1, 5)` is not found. Please use specify the correct parameter for `max_depth`.")
        
        if "100" and "1000" in filtered_actual:
            x.justpass()
        else:
            x.justfail("100, 1000, 100", "`(100, 1000, 100)` parameter is not found. Please use specify the correct parameter for `n_estimators`.")
        
        if "0.05" and "0.5" in filtered_actual:
            x.justpass()
        else:
            x.justfail("0.05, 0.5, 0.05", "`(0.05, 0.5, 0.05)` parameter is not found. Please use specify the correct parameter for `learning_rate`.")

        if ".fit" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".fit()", "`.fit()` is not used. Please apply the `.fit()` method on the model instance, `ab_estimator_tuned`, to train it.")

        if ".predict" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".predict()", "`.predict()` is not used. Please apply the `.predict()` method on the tuned model instance, `ab_estimator_tuned`, to compute.")
        
        previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
        filtered_previous = x.filter_source(previous, '#')

        import_source = x.get_source_code("lab5", 4)
        filtered_import_source = x.filter_source(import_source, "%")

        combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + filtered_actual
       
        variables = {}
        exec(combined_source, globals(), variables)
        
        executed_y_pred_gb_t =  variables.get('y_pred_gb_t')

        x.grading_nparray2(("y_pred_gb_t", Question4B._expected, executed_y_pred_gb_t))

        for test in self._test_cases:

            # test case for X train
            x.test_for_none_588(filtered_actual, "lab5", 65, test[0], test[1], "X_train")
            update1 = x.update_x_in_code(filtered_actual, test[0], test[1])
            # test case for y train
            x.test_for_none_588(filtered_actual, "lab5", 65, test[2], test[3], "y_train")
            update2 = x.update_x_in_code(update1, test[2], test[3])
            # test case for X test
            x.test_for_none_588(filtered_actual, "lab5", 65, test[4], test[5], "X_test")
            updated_source = x.update_x_in_code(update2, test[4], test[5])
            
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22, 27, 30, 34])
            filtered_previous = x.filter_source(previous, '#')

            import_source = x.get_source_code("lab5", 4)
            filtered_import_source = x.filter_source(import_source, "%")

            combined_source = filtered_import_source + "\n"+ filtered_previous + "\nnp.random.seed(0)\n" + updated_source
            
            variables = {}
            exec(combined_source, globals(), variables)
            
            executed_y_pred_gb_t2 =  variables.get('y_pred_gb_t')

            x.grading_nparray2(((test[1], test[3], test[5]), "y_pred_gb_t", test[6], executed_y_pred_gb_t2), var="test")


Question4 = MultipartProblem(
    Question4A,
    Question4B,

)
