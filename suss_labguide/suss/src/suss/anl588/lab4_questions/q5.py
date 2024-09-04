from learntools.core import *
from ...dev import x
import pandas as pd
from ..lab4_questions.q4 import Question4I
from statsmodels.tools.tools import add_constant
from sklearn.impute import SimpleImputer

class Question5A(EqualityCheckProblem):
    df2 = Question4I._expected
    X = df2.drop('DEFAULT', axis=1) 

    def produce_expected(input_data):

        expected_X = add_constant(input_data)

        return expected_X

    _var = "X"
    _expected = produce_expected(X)
    _test_cases = [
        ("(X)", "(pd.DataFrame([[0]]))", pd.DataFrame([[0]])),
        ("(X)", "(pd.DataFrame([[1]]))", pd.DataFrame([[1]]))
    ]

    def check(self, *args):
        # test actual value of X
        x.grading_df_series(("X", Question5A._expected, args[0]))

        for test in self._test_cases:
            actual_source = x.get_source_code("lab4", 79)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab4", 79, test[0], test[1], "(X)")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])

            if "add_constant" in filtered_actual:
                x.justpass()
            else:
                x.justfail("add_constant", "`add_constant` is not used. Please use `add_constant()` to add a constant to X.")

            previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62, 65, 70, 77])
            filtered_previous = x.filter_source(previous, '#')

            combined_source = "import pandas as pd\nfrom statsmodels.tools.tools import add_constant\n" + filtered_previous + "\n" + updated_source
            variables = {}
            exec(combined_source, globals(), variables)
            executed_X= variables.get("X")
            expected_X = Question5A.produce_expected(test[2])
            x.grading_df_series((updated_source, "X", expected_X, executed_X), var="test")

class Question5B(EqualityCheckProblem):

    df2 = Question4I._expected
    X = df2.drop('DEFAULT', axis=1) 
    def produce_expected(input_data):

        X = add_constant(input_data)
        imputer = SimpleImputer(strategy = "mean")
        X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
        expected = X.isna().sum()

        return expected

    _var = "X"
    _expected = produce_expected(X)
    _test_cases = [
        (".sum", ".count", pd.Series(30000, index=['const', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'AVGBAL']))
    ]

    def check(self, *args):
        # test actual value of source
        actual_source = x.get_source_code("lab4", 86)
        filtered_actual = x.filter_source(actual_source, '#')

        if ".isna" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".isna", "`.isna` is not used. Please use `.isna()` to checking for missing value.")
        
        if ".sum" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".sum", "`.sum()` is not used. Please use `.isna().sum()` method.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62, 65, 70, 77, 79, 83, 84, 85])
        filtered_previous = x.filter_source(previous, '#')

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_X = variables.get("X")
        executed_X_isnasum = executed_X.isna().sum()
        x.grading_df_series(("X.isna().sum()", Question5B._expected, executed_X_isnasum))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 86, test[0], test[1], "X.isna().sum()")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_X_2 =  variables.get("X")
            executed_X_isnasum2 = executed_X_2.isna().count()
            x.grading_df_series(("X.isna().count()", "X.isna().count()", test[2], executed_X_isnasum2), var="test")

class Question5C(EqualityCheckProblem):

    df2 = Question4I._expected
    X = df2.drop('DEFAULT', axis=1)
    y = df2['DEFAULT'] 

    def produce_expected(input_data1, input_data2):

        X = add_constant(input_data1)
        imputer = SimpleImputer(strategy = "mean")
        X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)
        expected = input_data2.isna().sum()

        return expected

    _var = "y"
    _expected = produce_expected(X,y)
    _test_cases = [
        (".sum", ".count", 30000)
        # ("(X)", "(pd.DataFrame([[1]]))", pd.DataFrame([[1]]))
    ]

    def check(self, *args):
        # test actual value of source
        actual_source = x.get_source_code("lab4", 89)
        filtered_actual = x.filter_source(actual_source, '#')

        if ".isna" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".isna", "`.isna` is not used. Please use `.isna()` to checking for missing value.")
        
        if ".sum" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".sum", "`.sum()` is not used. Please use `.isna().sum()` method.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62, 65, 70, 77, 79, 83, 84, 85])
        filtered_previous = x.filter_source(previous, '#')

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_y = variables.get("y")
        executed_y_isnasum = executed_y.isna().sum()
        x.determine_the_grading_method(("y.isna().sum()", Question5C._expected, executed_y_isnasum))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 89, test[0], test[1], "y.isna().sum()")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_y_2 =  variables.get("y")
            executed_y_isnasum2 = executed_y_2.isna().count()
            x.determine_the_grading_method(("y.isna().count()", test[2], executed_y_isnasum2))

            
Question5 = MultipartProblem(
    Question5A,
    Question5B,
    Question5C
)
