from learntools.core import *
from ...dev import x
import os
from ..lab4_questions.q4 import Question4I
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, KFold, cross_val_score
from sklearn.metrics import accuracy_score, make_scorer, precision_score, f1_score, average_precision_score
from statsmodels.tools.tools import add_constant
from sklearn.impute import SimpleImputer


class Question6A(EqualityCheckProblem):

    def produce_expected(value1, value2, value3):

        model = LogisticRegression(random_state=value1, penalty=value2, max_iter= value3 ) 

        return model

    _var = "model"
    _expected = produce_expected(101, 'none', 10000)
    _test_cases = [
        ("101", "0", produce_expected(0, 'none', 10000)),
        ("none", "l1", produce_expected(101, 'l1', 10000)),
        ("10000", "0", produce_expected(101, 'none', 0))
    ]

    def check(self, *args):
        # test actual value of model
        # x.determine_the_grading_method(("model", Question6A._expected, args[0])) # this will show exact same output and type but incorrect
        model_params = args[0].get_params()
        expected_params = Question6A._expected.get_params()

        missing_params = set(expected_params.keys()) - set(model_params.keys())

        assert set(model_params.keys()) == set(expected_params.keys()), f"""These parameters are missing in `model`: 
{missing_params}"""

        x.grading_param_attrs(("parameter", expected_params, model_params))
          
        for test in self._test_cases:
            actual_source = x.get_source_code("lab4", 95)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab4", 95, test[0], test[1], "model")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])

            combined_source = x.get_source_code("lab4", 93) + "\n" + updated_source
            variables = {}
            exec(combined_source, globals(), variables)
            executed_model= variables.get("model")
            executed_model_params = executed_model.get_params()
            expected_test_params = test[2].get_params()

            x.grading_param_attrs((updated_source, "parameter", expected_test_params, executed_model_params), var="test")

class Question6B(EqualityCheckProblem):


    # def produce_expected(input_data):

    #     X = add_constant(input_data)
    #     imputer = SimpleImputer(strategy = "mean")
    #     X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    #     expected = X.isna().sum()

    #     return expected

    # _var = "X"
    # _expected = produce_expected(1)
    # _test_cases = [
    #     (".sum", ".count", pd.Series(30000, index=['const', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'AVGBAL']))
    #     # ("(X)", "(pd.DataFrame([[1]]))", pd.DataFrame([[1]]))
    # ]

    def check(self, *args):
        # test actual value of source
        source = x.get_source_code("lab4", 99)
        updated_source = x.filter_source(source, '#')
        
        if "sklearn.model_selection" in updated_source:
            x.justpass()
        else:
            x.justfail("sklearn.model_selection", "`sklearn.model_selection` is not found. Please import from sklearn.model_selection.")
        
        if "StratifiedKFold" in updated_source:
            x.justpass()
        else:
            x.justfail("StratifiedKFold", "`StratifiedKFold` is not found. Please import `StratifiedKFold` from sklearn.model_selection.")
        
        if "KFold" in updated_source:
            x.justpass()
        else:
            x.justfail("KFold", "`KFold` is not found. Please import `KFold` from sklearn.model_selection.")
        
        if "cross_val_score" in updated_source:
            x.justpass()
        else:
            x.justfail("cross_val_score", "`cross_val_score` is not found. Please import `cross_val_score` from sklearn.model_selection.")

class Question6C(EqualityCheckProblem):


    # def produce_expected():

    #     X = add_constant(1)
    #     imputer = SimpleImputer(strategy = "mean")
    #     X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
    #     expected = X.isna().sum()

    #     return expected

    # _var = "X"
    # _expected = produce_expected()
    # _test_cases = [
    #     (".sum", ".count", 30000)
    #     # ("(X)", "(pd.DataFrame([[1]]))", pd.DataFrame([[1]]))
    # ]

    def check(self, *args):
        # test actual value of source
        source = x.get_source_code("lab4", 102)
        updated_source = x.filter_source(source, '#')

        if "sklearn.metrics" in updated_source:
            x.justpass()
        else:
            x.justfail("sklearn.metrics", "`sklearn.metrics` is not found. Please import from sklearn.metrics.")
        
        if "accuracy_score" in updated_source:
            x.justpass()
        else:
            x.justfail("accuracy_score", "`accuracy_score` is not found. Please import `accuracy_score` from sklearn.metrics.")
        
        if "make_scorer" in updated_source:
            x.justpass()
        else:
            x.justfail("make_scorer", "`make_scorer` is not found. Please import `make_scorer` from sklearn.metrics.")
        
class Question6D(EqualityCheckProblem):

    def produce_expected(value1, value2, value3):

        kfold = StratifiedKFold(n_splits = value1, random_state = value2, shuffle = value3) 

        return kfold

    _var = "kfold"
    _expected = produce_expected(5, 101, True)
    _test_cases = [
        ("5", "2", produce_expected(2, 101, True), "", ""),
        ("101", "0", produce_expected(5, 0, True), "", ""),
        ("True", "False", produce_expected(5, None, False), "101", "None")
    ]

    def check(self, *args):
        # test actual value of kfold
      
        kfold_attrs = args[0].__dict__
        expected_attrs = Question6D._expected.__dict__

        x.grading_param_attrs(("attribute", expected_attrs, kfold_attrs))
          
        for test in self._test_cases:
            actual_source = x.get_source_code("lab4", 106)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab4", 106, test[0], test[1], "kfold")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            
            if test[3]:
                updated_source = x.update_x_in_code(updated_source,test[3], test[4])

            combined_source = x.get_source_code("lab4", 99) + "\n" + updated_source
            variables = {}
            exec(combined_source, globals(), variables)
            executed_kfold= variables.get("kfold")
            executed_kfold_attrs = executed_kfold.__dict__
            expected_test_attrs = test[2].__dict__

            x.grading_param_attrs((updated_source, "attribute", expected_test_attrs, executed_kfold_attrs), var="test")

class Question6E(EqualityCheckProblem):

    def produce_expected(input):

        scorer_accuracy = make_scorer(input)

        return scorer_accuracy

    _var = "scorer_accuracy"
    _expected = produce_expected(accuracy_score)
    _test_cases = [
        ("accuracy_score", "precision_score", produce_expected(precision_score)),
        ("accuracy_score", "average_precision_score", produce_expected(average_precision_score)),
        ("accuracy_score", "f1_score", produce_expected(f1_score))
    ]

    def check(self, *args):
        # test actual value 
        x.grading_equal(("scorer function for scorer_accuracy", Question6E._expected._score_func.__name__, args[0]._score_func.__name__))
        
        for test in self._test_cases:
            actual_source = x.get_source_code("lab4", 110)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab4", 110, test[0], test[1], "scorer_accuracy")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])

            combined_source = "from sklearn.metrics import precision_score, f1_score, average_precision_score\n" + x.get_source_code("lab4", 104) + "\n" + updated_source
            variables = {}
            exec(combined_source, globals(), variables)
            executed_scorer_accuracy = variables.get("scorer_accuracy")

            x.grading_equal((updated_source, "scorer function for scorer_accuracy", test[2]._score_func.__name__, executed_scorer_accuracy._score_func.__name__), var="test")
      
class Question6F(EqualityCheckProblem):

    def produce_expected(file):
        df2 = Question4I.produce_expected(file, 12,18)
        X = df2.drop('DEFAULT', axis=1)
        y = df2['DEFAULT'] 
        X = add_constant(X)
        imputer = SimpleImputer(strategy = "mean")
        X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
        model = LogisticRegression(random_state=101, penalty='none', max_iter= 10000 ) 
        kfold = StratifiedKFold(n_splits = 5, random_state = 101, shuffle = True)
        scorer_accuracy = make_scorer(accuracy_score)
        results_accuracy = cross_val_score(model, X, y, cv = kfold, scoring = scorer_accuracy)

        return results_accuracy

    _var = "results_accuracy"
    _expected = produce_expected('test_UCI_Credit_Card.csv')
    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]

    def check(self, *args):
        # test actual value 
        x.grading_nparray2(("results_accuracy", args[0], Question6F._expected))

        for test in self._test_cases:
            actual_source = x.get_source_code("lab4", 7)
            filtered_actual = x.filter_source(actual_source, '#')

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_actual, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(filtered_actual, new_csv, "df")

            previous = x.get_multiple_cell_source("lab4", [22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62, 65, 70, 77, 79, 83, 84, 85, 95, 99, 102, 106, 110, 113])
                    
            filtered_previous = x.filter_source(previous, '#')

            combined_source = "import pandas as pd\n" + updated_source + "\n" + filtered_previous

            variables = {}
            exec(combined_source, globals(), variables)
            executed_results_accuracy = variables.get("results_accuracy")
            expected_results_accuracy = Question6F.produce_expected(test[1])
            x.grading_nparray2((f"df = pd.readcsv({test[1]})", "results_accuracy", executed_results_accuracy, expected_results_accuracy), var="test")

Question6 = MultipartProblem(
    Question6A,
    Question6B,
    Question6C,
    Question6D,
    Question6E,
    Question6F
)
