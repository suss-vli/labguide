from learntools.core import *
from ...dev import x
import os
import pandas as pd


class Question1(EqualityCheckProblem):

    def produce_expected(file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file
        df = pd.read_spss(expected_file)  

        return df
    
    _var = 'df'

    _test_cases = [
        ('test_prisons.sav', 'test_case.sav'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        # testing actual value of df
        actual_source = x.get_source_code("lab6", 6)
        filtered_actual = x.filter_source(actual_source, '#')

        if "df" in filtered_actual:
            x.justpass()
        else:
            x.justfail("df", "`df` is not used. Please use `df` as the dataframe.")
            
        if ".read_spss" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".read_spss()", "`.read_spss()` is not used. Please use `.read_spss()` method to import `prisons.sav`.")

        x.grading_df_series(("df", Question1._expected, args[0]))

        for test in self._test_cases:
            # update datafile

            combined_source = "import pandas as pd\n" + filtered_actual

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab6", 6, "prisons.sav", new_csv, "df")
            updated_source = x.update_x_in_code(combined_source, "prisons.sav", new_csv)
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df2 =  variables.get('df')
            expected_df = Question1.produce_expected(test[1])

            x.grading_df_series((new_csv, "df", expected_df, actual_df2), var="test")


