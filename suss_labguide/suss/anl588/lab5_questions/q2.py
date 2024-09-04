from learntools.core import *
from ...dev import x
import os
import pandas as pd


class Question2A(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        df = pd.read_csv(expected_file)  
        for feature in df.columns: # Loop through all columns in the dataframe 
            if df[feature].dtype == 'object': # Only apply for columns with categorical strings
                df[feature] = pd.Categorical(df[feature])# Replace a string variable as a categorical variable
        recodevalues = {
                "checking_balance":     {"< 0 DM": 0, "1 - 200 DM": 0 ,"> 200 DM": 1 ,"unknown":0},
                "credit_history": {"critical": 0, "poor":0 , "good": 0, "very good": 1,"perfect": 1},
                 "savings_balance": {"< 100 DM": 0, "100 - 500 DM":0 , "500 - 1000 DM": 1, "> 1000 DM": 1,"unknown": 0},
                 "employment_duration":     {"unemployed": 0, "< 1 year": 0 ,"1 - 4 years": 0 ,"4 - 7 years": 1 ,"> 7 years": 1},
                "phone":     {"no": 0, "yes": 1 },
                "default":    {"no": 0, "yes": 1 } 
                    }
        oneHotCols=["purpose","housing","other_credit","job"]
        df = df.replace(recodevalues)
        df = pd.get_dummies(df, columns=oneHotCols)
        df = df.astype(int)

        return df

    _var = 'df'

    _test_cases = [
        ('test_credit.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        actual_source = x.get_source_code("lab5", 23)
        filtered_actual = x.filter_source(actual_source, '#')

        if ".info()" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".info()", "`.info()` is not used. Please use `.info()` method on df to check that all variables are integers.")

        x.grading_df_series(("df.info()", Question2A._expected, args[0]))

        for test in self._test_cases:
            # update datafile
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22])
            filtered_previous = x.filter_source(previous, '#')

            combined_source = "import pandas as pd\n" + filtered_previous

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab5", 6, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df2 =  variables.get('df')
            expected_df = Question2A.produce_expected(test[1])

            x.grading_df_series((test[1], "df.info()", expected_df, actual_df2), var="test")

class Question2B(EqualityCheckProblem):

    def produce_expected(file):
        df = Question2A.produce_expected(file)
        X = df.drop("default", axis=1)

        return X

    _var = 'X'

    _test_cases = [
        ('test_credit.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        actual_source = x.get_source_code("lab5", 27)
        filtered_actual = x.filter_source(actual_source, '#')

        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop", "`.drop()` is not used. Please use `.drop()` method.")
            
        if "default" in filtered_actual:
            x.justpass()
        else:
            x.justfail("default", "`default` is not used. Please use drop `default` from `df`.")

        if "axis" and "=" and "1" in filtered_actual:
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` option is not used. Please use the option `axis = 1` when you drop `default` from `df`.")

        x.grading_df_series(("X", Question2B._expected, args[0]))

        for test in self._test_cases:
            # update datafile
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22])
            filtered_previous = x.filter_source(previous, '#')

            combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab5", 6, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_X =  variables.get('X')
            expected_X = Question2B.produce_expected(test[1])

            x.grading_df_series((test[1], "X", expected_X, actual_X), var="test")

class Question2C(EqualityCheckProblem):

    def produce_expected(file):
        df = Question2A.produce_expected(file)
        X = df.drop("default", axis=1)
        y = df.pop("default") 

        return y

    _var = 'y'

    _test_cases = [
        ('test_credit.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        actual_source = x.get_source_code("lab5", 30)
        filtered_actual = x.filter_source(actual_source, '#')
            
        if "default" in filtered_actual:
            x.justpass()
        else:
            x.justfail("default", "`default` is not used. Please use drop `default` from `df`.")

        if ".pop" or "df[" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".pop or df[]", "`.pop()` method or `df[]` is not found. Please use either the `.pop()` method on `df` or `df[]` to save `default` as `y`.")

        x.grading_df_series(("y", Question2C._expected, args[0]))

        for test in self._test_cases:
            # update datafile
            previous = x.get_multiple_cell_source("lab5", [6,15,19,20,22,27])
            filtered_previous = x.filter_source(previous, '#')

            combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab5", 6, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_y =  variables.get('y')
            expected_y = Question2C.produce_expected(test[1])

            x.grading_df_series((test[1], "y", expected_y, actual_y), var="test")

Question2 = MultipartProblem(
    Question2A, 
    Question2B,
    Question2C
)
