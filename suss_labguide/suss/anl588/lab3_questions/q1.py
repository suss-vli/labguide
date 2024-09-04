from learntools.core import *
from ...dev import x
import os
import pandas as pd


class Question1(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        df = pd.read_csv(expected_file)  

        return df

    _var = 'df'

    _test_cases = [
        ('test_beauty.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        # testing actual value of df
        x.grading_df_series(("df", Question1._expected, args[0]))

        source = x.get_source_code("lab3", 10)
        if "pd.read_csv" in source:
            x.justpass()
        else:
            x.justfail("pd.read_csv", "`pd.read_csv` is not used. Please use `pd.read_csv` to read the dataset.")
            
        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(source, "lab3", 10, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            df_actual =  variables.get('df')      
            expected_df = Question1.produce_expected(test[1])

            x.grading_df_series((updated_source, "df", df_actual, expected_df), var="test")

