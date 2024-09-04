from learntools.core import *
from ...dev import x
import os
import pandas as pd
from ..lab4_questions.q1 import Question1


class Question2A(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        summary = df.describe().transpose()
        return summary

    _var = 'df'

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df.describe().transpose()
        source = x.get_source_code("lab4", 12)
        filtered_source = x.filter_source(source, '#')

        if ".describe()" in filtered_source:
            x.justpass()
        else:
            x.justfail(".describe()", "`.describe()` is not used. Please use `.describe()` method to `df`.")

        if ".transpose()" in filtered_source:
            x.justpass()
        else:
            x.justfail(".transpose()", "`.transpose()` is not used. Please apply `.transpose()` to `df.describe()`.")
        
        combined_source = "import pandas as pd\n" + x.get_source_code("lab4", 7) + "\n" + filtered_source

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df =  variables.get('df')
        executed_summary = executed_df.describe().transpose()

        x.grading_df_series(("df.describe().transpose()", Question2A._expected, executed_summary))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_df2 =  variables.get('df')
            executed_summary2 = executed_df2.describe().transpose()   
            expected_summary = Question2A.produce_expected(test[1])

            x.grading_df_series((f"df = pd.read_csv(test[1])", "df.describe().transpose()", expected_summary, executed_summary2), var="test")

class Question2B(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        num_na = df.isna().sum()
        return num_na

    _var = 'df'

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df.isna().sum()
        source = x.get_source_code("lab4", 16)
        filtered_source = x.filter_source(source, '#')

        if ".isna().sum()" in filtered_source:
            x.justpass()
        else:
            x.justfail(".isna().sum()", "`.isna().sum()` is not used. Please use `.isna().sum().")

        combined_source = "import pandas as pd\n" + x.get_source_code("lab4", 7) + "\n" + filtered_source

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df =  variables.get('df')
        executed_num_na = executed_df.isna().sum()

        x.grading_df_series(("df.isna().sum()", Question2B._expected, executed_num_na))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_df2 =  variables.get('df')      
            executed_num_na2 = executed_df2.isna().sum()
            expected_num_na = Question2B.produce_expected(test[1])

            x.grading_df_series((f"df = pd.read_csv({test[1]})", "df.isna().sum()", expected_num_na, executed_num_na2), var="test")

class Question2C(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        dup_sum = df.duplicated().sum()
        return dup_sum

    _var = 'df'

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df.duplicated().sum()
        source = x.get_source_code("lab4", 19)
        filtered_source = x.filter_source(source, '#')

        if ".duplicated().sum()" in filtered_source:
            x.justpass()
        else:
            x.justfail(".duplicated().sum()", "`.duplicated().sum()` is not used. Please use `.duplicated().sum()`.")

        combined_source = "import pandas as pd\n" + x.get_source_code("lab4", 7) + "\n" + filtered_source

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df =  variables.get('df')
        executed_dup_sum = executed_df.duplicated().sum()

        x.grading_equal(("df.duplicated().sum()", Question2C._expected, executed_dup_sum))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_df=  variables.get('df')      
            executed_dup_sum2 = executed_df.duplicated().sum()
            expected_dup_sum = Question2C.produce_expected(test[1])

            x.grading_equal((f"df = pd.read_csv({test[1]})", "df.duplicated().sum()", expected_dup_sum, executed_dup_sum2), var="test")

class Question2D(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        return df

    _var = 'df'

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df aftter .rename
        source = x.get_source_code("lab4", 22)
        filtered_source = x.filter_source(source, '#')

        if ".rename" in filtered_source:
            x.justpass()
        else:
            x.justfail(".rename", "`.rename` is not used. Please use `.rename` to rename the column.")

        if "default.payment.next.month" in filtered_source:
            x.justpass()
        else:
            x.justfail("default.payment.next.month", "`default.payment.next.month` is not found. Please rename the column `default.payment.next.month`.")  
        
        if "DEFAULT" in filtered_source:
            x.justpass()
        else:
            x.justfail("DEFAULT", "`DEFAULT` is not found. Please rename the column `default.payment.next.month` to `DEFAULT`.")  

        combined_source = "import pandas as pd\n" + x.get_source_code("lab4", 7) + "\n" + filtered_source

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df =  variables.get('df')

        x.grading_df_series(("df", Question2D._expected, executed_df))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_df2 =  variables.get('df')      
            expected_df2 = Question2D.produce_expected(test[1])

            x.grading_df_series((f"df = pd.read_csv({test[1]})", "df", expected_df2, executed_df2), var="test")

class Question2E(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df.set_index('ID')
        return df

    _var = 'df'

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df aftter .rename
        source = x.get_source_code("lab4", 25)
        filtered_source = x.filter_source(source, '#')

        if ".set_index" in filtered_source:
            x.justpass()
        else:
            x.justfail(".set_index", "`.set_index` is not used. Please use `.set_index` to declare ID as the row index.")

        if "ID" in filtered_source:
            x.justpass()
        else:
            x.justfail("ID", "`ID` is not found. Please declare `ID` as the row index.")  

        previous = x.get_multiple_cell_source("lab4", [7, 22])
        combined_source = "import pandas as pd\n" + previous + "\n" + filtered_source
        filtered_combined_source = x.filter_source(combined_source, '#')

        variables = {}
        exec(filtered_combined_source, globals(), variables)
        executed_df =  variables.get('df')

        x.grading_df_series(("df", Question2E._expected, executed_df))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(combined_source, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_source = x.update_csv_in_code(combined_source, new_csv, "df") # need to specify df in the question
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_df2 =  variables.get('df')      
            expected_df2 = Question2E.produce_expected(test[1])

            x.grading_df_series((f"df = pd.read_csv({test[1]})", "df", expected_df2, executed_df2), var="test")

Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C,
    Question2D,
    Question2E
)
