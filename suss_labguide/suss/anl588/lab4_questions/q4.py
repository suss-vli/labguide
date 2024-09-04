from learntools.core import *
from ...dev import x
import os
import re
import pandas as pd
from ..lab4_questions.q1 import Question1


class Question4A(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3'] 
        return df["BAL3"]

    _var = "df"

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df['BAL3']
        
        df_source = x.get_source_code("lab4", 7)
        filtered_dfsource = x.filter_source(df_source, "#")

        previous = x.get_multiple_cell_source("lab4", [22, 25, 41])   
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_dfsource + "\n"+ filtered_previous

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df = variables.get("df")
        executed_BAL3 =  executed_df['BAL3']
        x.grading_df_series(("df['BAL3']", Question4A._expected, executed_BAL3))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_dfsource, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_dfsource = x.update_csv_in_code(filtered_dfsource, new_csv, "df") # need to specify df in the question
            combined_source2 = "import pandas as pd\n" + updated_dfsource + "\n"+ filtered_previous

            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2 =  variables.get("df")
            executed_BAL3_2 =  executed_df2['BAL3'] 
            expected_BAL3 = Question4A.produce_expected(test[1])

            x.grading_df_series((updated_dfsource, "df['BAL3']", expected_BAL3, executed_BAL3_2), var="test")

class Question4B(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4'] 
        return df["BAL4"]

    _var = "df"

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df['BAL4']

        df_source = x.get_source_code("lab4", 7)
        filtered_dfsource = x.filter_source(df_source, "#")

        previous = x.get_multiple_cell_source("lab4", [22, 25, 44])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_dfsource + "\n" + filtered_previous

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df = variables.get("df")
        executed_BAL4 =  executed_df['BAL4']
        x.grading_df_series(("df['BAL4']", Question4B._expected, executed_BAL4))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_dfsource, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_dfsource = x.update_csv_in_code(filtered_dfsource, new_csv, "df") # need to specify df in the question
            combined_source2 = "import pandas as pd\n" + updated_dfsource + "\n" + filtered_previous

            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2 =  variables.get("df")
            executed_BAL4_2 =  executed_df2['BAL4'] 
            expected_BAL4 = Question4B.produce_expected(test[1])

            x.grading_df_series((updated_dfsource, "df['BAL4']", expected_BAL4, executed_BAL4_2), var="test")

class Question4C(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        return df["BAL5"]

    _var = "df"

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df['BAL5']

        df_source = x.get_source_code("lab4", 7)
        filtered_dfsource = x.filter_source(df_source, "#")

        previous = x.get_multiple_cell_source("lab4", [22, 25, 47])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_dfsource + "\n" +  filtered_previous

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df = variables.get("df")
        executed_BAL5 =  executed_df['BAL5']
        x.grading_df_series(("df['BAL5']", Question4C._expected, executed_BAL5))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_dfsource, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_dfsource = x.update_csv_in_code(filtered_dfsource, new_csv, "df") # need to specify df in the question
            combined_source2 = "import pandas as pd\n" + updated_dfsource + "\n"+ filtered_previous

            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2 =  variables.get("df")
            executed_BAL5_2 =  executed_df2['BAL5'] 
            expected_BAL5 = Question4C.produce_expected(test[1])
            
            x.grading_df_series((updated_dfsource, "df['BAL5']", expected_BAL5, executed_BAL5_2), var="test")

class Question4D(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6'] 
        return df["BAL6"]

    _var = "df"

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df['BAL6']

        df_source = x.get_source_code("lab4", 7)
        filtered_dfsource = x.filter_source(df_source, "#")

        previous = x.get_multiple_cell_source("lab4", [22, 25, 50])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_dfsource + "\n" + filtered_previous

        variables = {}
        exec(combined_source, globals(), variables)
        executed_df = variables.get("df")
        executed_BAL6 =  executed_df['BAL6']
        x.grading_df_series(("df['BAL6']", Question4D._expected, executed_BAL6))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_dfsource, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_dfsource = x.update_csv_in_code(filtered_dfsource, new_csv, "df") # need to specify df in the question
            combined_source2 = "import pandas as pd\n" + updated_dfsource + "\n" + filtered_previous

            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2 =  variables.get("df")
            executed_BAL6_2 =  executed_df2['BAL6'] 
            expected_BAL6 = Question4D.produce_expected(test[1])
            
            x.grading_df_series((updated_dfsource, "df['BAL6']", expected_BAL6, executed_BAL6_2), var="test")

class Question4E(EqualityCheckProblem):

    def produce_expected(file):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL1'] = df['BILL_AMT1']- df['PAY_AMT1']
        df['BAL2'] = df['BILL_AMT2']- df['PAY_AMT2']
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3']
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4']
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6']

        df['AVGBAL']= (df['BAL1']+df['BAL2']+df['BAL3']+df['BAL4']+df['BAL5']+df['BAL6'])/6

        df2 = df.copy()

        return df2

    _var = "df2"

    _test_cases = [
        ('test_UCI_Credit_Card.csv', 'test_case.csv'),
    ]
    _expected = produce_expected(_test_cases[0][0])
    
    def check(self, *args):
        # test actual value of df2

        df_source = x.get_source_code("lab4", 7)
        filtered_dfsource = x.filter_source(df_source, "#")

        previous = x.get_multiple_cell_source("lab4", [22, 25, 39, 40, 41, 44, 47, 50, 54, 55])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_dfsource + "\n" + filtered_previous
        variables = {}
        exec(combined_source, globals(), variables)
        executed_df2 = variables.get("df2")
        x.grading_df_series(("df2", Question4E._expected, executed_df2))

        # inserting test cases
        for test in self._test_cases:
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_588(filtered_dfsource, "lab4", 7, new_csv, new_csv, "df", var="csv")
            updated_dfsource = x.update_csv_in_code(filtered_dfsource, new_csv, "df") # need to specify df in the question
            combined_source2 = "import pandas as pd\n" + updated_dfsource + "\n"+ filtered_previous
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2_2 =  variables.get("df2")
            expected_df2 = Question4E.produce_expected(test[1])
            x.grading_df_series((updated_dfsource, "df2", expected_df2, executed_df2_2), var="test")

class Question4F(EqualityCheckProblem):

    def produce_expected(column1, column2):
        df = Question1.produce_expected('test_UCI_Credit_Card.csv')
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL1'] = df['BILL_AMT1']- df['PAY_AMT1']
        df['BAL2'] = df['BILL_AMT2']- df['PAY_AMT2']
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3']
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4']
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6']

        df['AVGBAL']= (df['BAL1']+df['BAL2']+df['BAL3']+df['BAL4']+df['BAL5']+df['BAL6'])/6

        df2 = df.copy()
        df2.drop([f'{column1}', f'{column2}'], axis = 1, inplace = True) 

        return df2

    _var = "df2"
    _expected = produce_expected('BILL_AMT1', 'BILL_AMT2')
    
    _test_cases = [
        ('BILL_AMT1', 'BILL_AMT3', 'BILL_AMT3', 'BILL_AMT2'),
        ('BILL_AMT2', 'BILL_AMT4', 'BILL_AMT1', 'BILL_AMT4')
    ]

    def check(self, *args):
        # test actual value of df2
        actual_source = x.get_source_code("lab4", 59)
        filtered_actual = x.filter_source(actual_source, "#")

        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop", "`.drop` is not used. Please use `.drop` to drop the `BILL_AMT1` and `BILL_AMT2`.")

        # Define the regular expression pattern
        axis_pattern = r'axis\s*=\s*1'

        # Define variations of the pattern
        axis_patterns = [
            axis_pattern,
            axis_pattern.replace(' ', r'\s*'),
            axis_pattern.replace('=', r'\s*=\s*'),
            axis_pattern.replace('axis', r'axis\s*').replace('1', r'1\s*')
        ] 
        # Check if any of the axis patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in axis_patterns):
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` is not found. Please specify the `axis`.")

        # Define the regular expression pattern
        inplace_pattern = r'inplace\s*=\s*True'

        # Define variations of the pattern
        inplace_patterns = [
            inplace_pattern,
            inplace_pattern.replace(' ', r'\s*'),
            inplace_pattern.replace('=', r'\s*=\s*'),
            inplace_pattern.replace('inplace', r'inplace\s*').replace('True', r'True\s*')
        ]   

        # Check if any of the inplace patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in inplace_patterns):
            x.justpass()
        else:
            x.justfail("inplace = True", "`inplace = True` is not found. Please use the options `inplace = True`.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_df2 = variables.get("df2")
        x.grading_df_series(("df2", Question4F._expected, executed_df2))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 59, test[0], test[1], "df2.drop")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2_2 =  variables.get("df2")
            expected_df2 = Question4F.produce_expected(test[2], test[3])
            x.grading_df_series((updated_source, "df2", expected_df2, executed_df2_2), var="test")

class Question4G(EqualityCheckProblem):

    def produce_expected(column1):
        df = Question1.produce_expected('test_UCI_Credit_Card.csv')
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL1'] = df['BILL_AMT1']- df['PAY_AMT1']
        df['BAL2'] = df['BILL_AMT2']- df['PAY_AMT2']
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3']
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4']
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6']

        df['AVGBAL']= (df['BAL1']+df['BAL2']+df['BAL3']+df['BAL4']+df['BAL5']+df['BAL6'])/6

        df2 = df.copy()
        df2.drop(['BILL_AMT1', 'BILL_AMT2'], axis = 1, inplace = True) 
        df2.drop([f'{column1}'], axis = 1, inplace = True)

        return df2

    _var = "df2"
    _expected = produce_expected('ID')
    
    _test_cases = [
        ('ID', 'LIMIT_BAL'),
        ('ID', 'AGE')
    ]

    def check(self, *args):
        # test actual value of df2
        actual_source = x.get_source_code("lab4", 62)
        filtered_actual = x.filter_source(actual_source, "#")

        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop", "`.drop` is not used. Please use `.drop` to drop the `BILL_AMT1` and `BILL_AMT2`.")

        # Define the regular expression pattern
        axis_pattern = r'axis\s*=\s*1'

        # Define variations of the pattern
        axis_patterns = [
            axis_pattern,
            axis_pattern.replace(' ', r'\s*'),
            axis_pattern.replace('=', r'\s*=\s*'),
            axis_pattern.replace('axis', r'axis\s*').replace('1', r'1\s*')
        ] 
        # Check if any of the axis patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in axis_patterns):
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` is not found. Please specify the `axis`.")

        # Define the regular expression pattern
        inplace_pattern = r'inplace\s*=\s*True'

        # Define variations of the pattern
        inplace_patterns = [
            inplace_pattern,
            inplace_pattern.replace(' ', r'\s*'),
            inplace_pattern.replace('=', r'\s*=\s*'),
            inplace_pattern.replace('inplace', r'inplace\s*').replace('True', r'True\s*')
        ]   

        # Check if any of the inplace patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in inplace_patterns):
            x.justpass()
        else:
            x.justfail("inplace = True", "`inplace = True` is not found. Please use the options `inplace = True`.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_df2 = variables.get("df2")
        x.grading_df_series(("df2", Question4G._expected, executed_df2))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 62, test[0], test[1], "df2.drop")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2_2 =  variables.get("df2")
            expected_df2 = Question4G.produce_expected(test[1])
            x.grading_df_series((updated_source, "df2", expected_df2, executed_df2_2), var="test")


class Question4H(EqualityCheckProblem):

    def produce_expected(columns1, columns2):
        df = Question1.produce_expected('test_UCI_Credit_Card.csv')
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL1'] = df['BILL_AMT1']- df['PAY_AMT1']
        df['BAL2'] = df['BILL_AMT2']- df['PAY_AMT2']
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3']
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4']
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6']

        df['AVGBAL']= (df['BAL1']+df['BAL2']+df['BAL3']+df['BAL4']+df['BAL5']+df['BAL6'])/6

        df2 = df.copy()
        df2.drop(['BILL_AMT1', 'BILL_AMT2'], axis = 1, inplace = True) 
        df2.drop(['ID'], axis = 1, inplace = True)
        df2.drop(columns1, axis=1, inplace=True)
        df2.drop(columns2, axis=1, inplace=True)

        return df2

    _var = "df2"
    _expected = produce_expected(['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'],
                                ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'])
    _test_cases = [
        ('BILL_AMT3', 'LIMIT_BAL', ['LIMIT_BAL', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('BILL_AMT4', 'AGE', ['BILL_AMT3', 'AGE', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('BILL_AMT5', 'EDUCATION', ['BILL_AMT3', 'BILL_AMT4', 'EDUCATION', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('BILL_AMT6', 'MARRIAGE', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'MARRIAGE'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('PAY_AMT1', 'AGE', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['AGE', 'PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('PAY_AMT2', 'EDUCATION', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1', 'EDUCATION','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('PAY_AMT3', 'LIMIT_BAL', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','LIMIT_BAL', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']),
        ('PAY_AMT4', 'MARRIAGE', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'MARRIAGE', 'PAY_AMT5', 'PAY_AMT6']),
        ('PAY_AMT5', 'AVGBAL', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'AVGBAL', 'PAY_AMT6']),
        ('PAY_AMT6', 'DEFAULT', ['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], ['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'DEFAULT'])
    ]

    def check(self, *args):
        # test actual value of df2
        actual_source = x.get_source_code("lab4", 65)
        filtered_actual = x.filter_source(actual_source, "#")

        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop", "`.drop` is not used. Please use `.drop` to drop the `BILL_AMT1` and `BILL_AMT2`.")

        # Define the regular expression pattern
        axis_pattern = r'axis\s*=\s*1'

        # Define variations of the pattern
        axis_patterns = [
            axis_pattern,
            axis_pattern.replace(' ', r'\s*'),
            axis_pattern.replace('=', r'\s*=\s*'),
            axis_pattern.replace('axis', r'axis\s*').replace('1', r'1\s*')
        ] 
        # Check if any of the axis patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in axis_patterns):
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` is not found. Please specify the `axis`.")

        # Define the regular expression pattern
        inplace_pattern = r'inplace\s*=\s*True'

        # Define variations of the pattern
        inplace_patterns = [
            inplace_pattern,
            inplace_pattern.replace(' ', r'\s*'),
            inplace_pattern.replace('=', r'\s*=\s*'),
            inplace_pattern.replace('inplace', r'inplace\s*').replace('True', r'True\s*')
        ]   

        # Check if any of the inplace patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in inplace_patterns):
            x.justpass()
        else:
            x.justfail("inplace = True", "`inplace = True` is not found. Please use the options `inplace = True`.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62])
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_df2 = variables.get("df2")
        x.grading_df_series(("df2", Question4H._expected, executed_df2))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 65, test[0], test[1], "df2.drop")
            updated_source = x.update_x_in_code(filtered_actual,test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2_2 =  variables.get("df2")
            expected_df2 = Question4H.produce_expected(test[2], test[3])
            x.grading_df_series((updated_source, "df2", expected_df2, executed_df2_2), var="test")

class Question4I(EqualityCheckProblem):

    def produce_expected(file, column_no1, column_no2):
        df = Question1.produce_expected(file)
        df.rename(columns = {'default.payment.next.month':'DEFAULT'}, inplace = True)
        df['BAL1'] = df['BILL_AMT1']- df['PAY_AMT1']
        df['BAL2'] = df['BILL_AMT2']- df['PAY_AMT2']
        df['BAL3'] = df['BILL_AMT3']- df['PAY_AMT3']
        df['BAL4'] = df['BILL_AMT4']- df['PAY_AMT4']
        df['BAL5'] = df['BILL_AMT5']- df['PAY_AMT5'] 
        df['BAL6'] = df['BILL_AMT6']- df['PAY_AMT6']

        df['AVGBAL']= (df['BAL1']+df['BAL2']+df['BAL3']+df['BAL4']+df['BAL5']+df['BAL6'])/6

        df2 = df.copy()
        df2.drop(['BILL_AMT1', 'BILL_AMT2'], axis = 1, inplace = True) 
        df2.drop(['ID'], axis = 1, inplace = True)
        df2.drop(['BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'], axis = 1, inplace = True) 
        df2.drop(['PAY_AMT1','PAY_AMT2','PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'], axis = 1, inplace = True)

        df2.drop(df2.columns[column_no1:column_no2], axis=1, inplace=True)

        return df2

    _var = "df2"
    _expected = produce_expected('test_UCI_Credit_Card.csv', 12,18)
    _test_cases = [
        ("12", "18", "None", None),
        ("12", "18", "19", 19)
    ]

    def check(self, *args):
        # test actual value of df2
        actual_source = x.get_source_code("lab4", 70)
        filtered_actual = x.filter_source(actual_source, "#")

        if ".drop" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".drop", "`.drop` is not used. Please use `.drop` to drop the `BILL_AMT1` and `BILL_AMT2`.")
        
        if ".columns" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".columns", "`.columns` is not used. Please use `.columns` to drop the columns [12:18].")

        # Define the regular expression pattern
        axis_pattern = r'axis\s*=\s*1'

        # Define variations of the pattern
        axis_patterns = [
            axis_pattern,
            axis_pattern.replace(' ', r'\s*'),
            axis_pattern.replace('=', r'\s*=\s*'),
            axis_pattern.replace('axis', r'axis\s*').replace('1', r'1\s*')
        ] 
        # Check if any of the axis patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in axis_patterns):
            x.justpass()
        else:
            x.justfail("axis = 1", "`axis = 1` is not found. Please specify the `axis`.")

        # Define the regular expression pattern
        inplace_pattern = r'inplace\s*=\s*True'

        # Define variations of the pattern
        inplace_patterns = [
            inplace_pattern,
            inplace_pattern.replace(' ', r'\s*'),
            inplace_pattern.replace('=', r'\s*=\s*'),
            inplace_pattern.replace('inplace', r'inplace\s*').replace('True', r'True\s*')
        ]   

        # Check if any of the inplace patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in inplace_patterns):
            x.justpass()
        else:
            x.justfail("inplace = True", "`inplace = True` is not found. Please use the options `inplace = True`.")

        # Define the regular expression pattern
        slice_pattern = r'\[\s*12\s*:\s*18\s*\]'

        # Define variations of the pattern
        slice_patterns = [
            slice_pattern,
            slice_pattern.replace(':', r'\s*:\s*'),
            slice_pattern.replace('12', r'\s*12\s*').replace('18', r'\s*18\s*')
        ] 

        # Check if any of the slice patterns are found in filtered_actual
        if any(re.search(pattern, filtered_actual) for pattern in slice_patterns):
            x.justpass()
        else:
            x.justfail("[12:18]", "`[12:18]` is not found. Please drop the columns `[12:18]`.")

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25, 39, 40, 41, 44, 47, 50, 54, 55, 59, 62, 65])        
        filtered_previous = x.filter_source(previous, "#")

        combined_source = "import pandas as pd\n" + filtered_previous + "\n" + filtered_actual
        variables = {}
        exec(combined_source, globals(), variables)
        executed_df2 = variables.get("df2")
        x.grading_df_series(("df2", Question4I._expected, executed_df2))

        # inserting test cases
        for test in self._test_cases:
            x.test_for_none_588(filtered_actual, "lab4", 70, test[0], test[1], "df2.drop(df2.columns[12:18], axis=1, inplace=True))")
            updated_no1 = x.update_x_in_code(filtered_actual,test[0], test[2])
            updated_source = x.update_x_in_code(updated_no1,test[1], test[2])
            combined_source2 = "import pandas as pd\n" + filtered_previous + "\n" + updated_source
            
            variables = {}
            exec(combined_source2, globals(), variables)
            executed_df2_2 =  variables.get("df2")
            expected_df2 = Question4I.produce_expected('test_UCI_Credit_Card.csv', test[3], test[3])
            x.grading_df_series((updated_source, "df2", expected_df2, executed_df2_2), var="test")


Question4 = MultipartProblem(
    Question4A,
    Question4B,
    Question4C,
    Question4D,
    Question4E,
    Question4F,
    Question4G,
    Question4H,
    Question4I
)
