from learntools.core import *
from ...dev import x
import os
import pandas as pd
from ..lab6_questions.q1 import Question1


class Question2A(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        dfa = df.copy()

        return dfa
    
    _var = 'dfa'

    _test_cases = [
        ('test_prisons.sav', 'test_case.sav'),
    ]
    _expected = produce_expected(_test_cases[0][0])


    def check(self, *args):
        # testing actual value of dfa
        actual_source = x.get_source_code("lab6", 16)
        filtered_actual = x.filter_source(actual_source, '#')


        if "dfa" in filtered_actual:
            x.justpass()
        else:
            x.justfail("dfa", "`dfa` is not used. Please make a copy and save it as `dfa`.")
            
        if ".copy" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".copy()", "`.copy()` is not used. Please use `.copy()` method to copy the data.")


        x.grading_df_series(("dfa", Question2A._expected, args[0]))

        for test in self._test_cases:
            # update datafile
            df_source = x.get_source_code("lab6", 6)
            filtered_df_source = x.filter_source(df_source, '#')

            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_df_source, "lab6", 6, "prisons.sav", new_csv, "df")
            updated_source = x.update_x_in_code(filtered_df_source, "prisons.sav", new_csv)
            combined_source = "import pandas as pd\n" + updated_source + "\n" + filtered_actual

            variables = {}
            exec(combined_source, globals(), variables)
            actual_dfa2 = variables.get('dfa')

            expected_dfa = Question2A.produce_expected(test[1])

            x.grading_df_series((new_csv, "df", expected_dfa, actual_dfa2), var="test")

class Question2B(EqualityCheckProblem):

    def produce_expected(input1):
        df = Question1.produce_expected('test_prisons.sav')
        dfa = df.copy()
        dfa = dfa.drop([input1], axis = 1)

        return dfa
    
    _var = 'dfa'

    _test_cases = [
        ('IDNO', 'OUTCOME'),
        ('IDNO', 'NUM_OFF'),
        ('IDNO', 'RACE'),
        ('IDNO', 'AGE')
    ]
    _expected = produce_expected('IDNO')


    def check(self, *args):
        # testing actual value of dfa
        actual_source = x.get_source_code("lab6", 19)
        filtered_actual = x.filter_source(actual_source, '#')


        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop()", "`.drop()` is not used. Please use `.drop()` to drop `IDNO`.")
        
        if "IDNO" in filtered_actual:
            x.justpass()
        else:
            x.justfail("IDNO", "`IDNO` is not found. Please use drop `IDNO` from the dataset.")
            
        if "axis" and "1" in filtered_actual:
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` is not used. Please use `axis = 1` when you drop `IDNO`.")


        x.grading_df_series(("dfa", Question2B._expected, args[0]))

        for test in self._test_cases:

            x.test_for_none_588(filtered_actual, "lab6", 19, test[0], test[1], "dfa.drop('IDNO', axis = 1)")
            updated_source = x.update_x_in_code(filtered_actual, test[0], test[1])

            source = x.get_multiple_cell_source("lab6", [6, 16])
            filtered_source = x.filter_source(source, '#')

            combined_source = "import pandas as pd\n" + filtered_source + "\n" + updated_source

            variables = {}
            exec(combined_source, globals(), variables)
            actual_dfa2 = variables.get('dfa')

            expected_dfa = Question2B.produce_expected(test[1])

            x.grading_df_series((test[1], "dfa", expected_dfa, actual_dfa2), var="test")

class Question2C(EqualityCheckProblem):

    def produce_expected(input1):
        df = Question1.produce_expected('test_prisons.sav')
        dfa = df.copy()
        dfa = dfa.drop(['IDNO'], axis = 1)
        dfa = dfa.astype(input1)

        return dfa
    
    _var = 'dfa'

    _test_cases = [
        ('category', 'str'),
        ('category', 'bool')
    ]
    _expected = produce_expected('category')


    def check(self, *args):
        # testing actual value of dfa
        actual_source = x.get_source_code("lab6", 24)
        filtered_actual = x.filter_source(actual_source, '#')


        if ".astype" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".astype()", "`.astype()` is not used. Please use `.astype()` to convert the variables.")
        
        if "category" in filtered_actual:
            x.justpass()
        else:
            x.justfail("category", "`category` is not found. Please use `category` to convert the variable types in `dfa` into categorical variables.")
            
        x.grading_df_series(("dfa", Question2C._expected, args[0]))

        for test in self._test_cases:

            x.test_for_none_588(filtered_actual, "lab6", 24, test[0], test[1], "dfa.astype('category')")
            updated_source = x.update_x_in_code(filtered_actual, test[0], test[1])

            source = x.get_multiple_cell_source("lab6", [6, 16, 19])
            filtered_source = x.filter_source(source, '#')

            combined_source = "import pandas as pd\n" + filtered_source + "\n" + updated_source

            variables = {}
            exec(combined_source, globals(), variables)
            actual_dfa2 = variables.get('dfa')

            expected_dfa = Question2C.produce_expected(test[1])

            x.grading_df_series((test[1], "dfa", expected_dfa, actual_dfa2), var="test")


Question2 = MultipartProblem(
    Question2A, 
    Question2B,
    Question2C
)
