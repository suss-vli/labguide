from learntools.core import *
from ...dev import x
import os
import pandas as pd


class Question1A(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        df = pd.read_csv(expected_file)  
        expected = df['default'].value_counts()

        return expected

    _var = 'df'

    _test_cases = [
        ('test_credit.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        # testing actual value of df['default'].value_counts()

        actual_source = x.get_source_code("lab5", 7)
        filtered_actual = x.filter_source(actual_source, '#')

        if "df['default']" in filtered_actual:
            x.justpass()
        else:
            x.justfail("df['default']", "`df['default']` is not used. Please use `df['default']` in your code.")
            
        if ".value_counts()" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".value_counts()", "`.value_counts()` is not used. Please use `.value_counts()`.")

        combined_source = "import pandas as pd\n" + x.get_source_code("lab5", 6) + "\n" + filtered_actual

        variables = {}
        exec(combined_source, globals(), variables)
        actual_df = variables.get('df')
        actual_df_value_count = actual_df['default'].value_counts()

        x.grading_df_series(("df['default'].value_counts()", Question1A._expected, actual_df_value_count))

        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab5", 6, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df2 =  variables.get('df')
            actual_df2_value_count = actual_df2['default'].value_counts()
            expected_df = Question1A.produce_expected(test[1])

            x.grading_df_series((test[1], "df['default'].value_counts()", expected_df, actual_df2_value_count), var="test")

class Question1B(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        df = pd.read_csv(expected_file)  
        expected = df.describe().transpose()

        return expected

    _var = 'df'

    _test_cases = [
        ('test_credit.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        # testing actual value of df.describe().transpose()

        actual_source = x.get_source_code("lab5", 10)
        filtered_actual = x.filter_source(actual_source, '#')

        if ".describe()" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".describe()", "`.describe()` is not used. Please use `.describe()` in your code.")
            
        if ".transpose()" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".transpose()", "`.transpose()` is not used. Please use `.describe()` and `.transpose()` on `df`.")

        combined_source = "import pandas as pd\n" + x.get_source_code("lab5", 6) + "\n" + filtered_actual

        variables = {}
        exec(combined_source, globals(), variables)
        actual_df = variables.get('df')
        actual_df_describe = actual_df.describe().transpose()

        x.grading_df_series(("df.describe().transpose()", Question1B._expected, actual_df_describe))

        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab5", 6, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df2 =  variables.get('df')
            actual_df2_describe = actual_df2.describe().transpose()
            expected_df = Question1B.produce_expected(test[1])

            x.grading_df_series((test[1], "df", expected_df, actual_df2_describe), var="test")

Question1 = MultipartProblem(
    Question1A, 
    Question1B
)
