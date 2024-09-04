from learntools.core import *
from ...dev import x
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd
import statsmodels.api as sm
from ..lab3_questions.q1 import Question1
from ..lab3_questions.q5 import Question5
from ..lab3_questions.q9 import Question9A

class Question11A(EqualityCheckProblem):

    # def produce_expected(data1 = 0.3, data2 = 101):
    #     df2 = Question3A._expected
    #     df2 = df2.drop('lwage', axis = 1)
    #     X = df2.drop('wage' , axis = 1)
    #     y = df2['wage' ]
    #     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = data1, random_state = data2)
        
    #     return X_train, X_test, y_train, y_test

    # _vars = ['X_train', 'X_test', 'y_train', 'y_test']
    # _expected = produce_expected()

    # _test_cases = [ 
    #     ('0.3', '0.1', 'test_size', produce_expected(0.1, 101)),
    #     ('101', '100', 'random_state', produce_expected(0.3, 100))
    # ]

    def check(self, *args):
  
        source = x.get_source_code("lab3", 80)
        updated_source = x.filter_source(source, '#')
        
        if "statsmodels.api" in updated_source:
            x.justpass()
        else:
            x.justfail("statsmodels.api", "`statsmodels.api` is not found. Please import statsmodels.api.")
        
        if "as sm" in updated_source:
            x.justpass()
        else:
            x.justfail("as sm", "`as sm` is not found. Please import `statsmodels.api as sm`.")
        
class Question11B(EqualityCheckProblem):

    df = Question1._expected
    def produce_expected():
        df = Question1._expected
        y = df['lwage']
        X = df[['looks', 'educ', 'exper', 'female']]
        X = sm.add_constant(X)
        
        return y, X

    _vars = ['y', 'X']
    _expected = produce_expected()

    _test_cases = [ 
        ('lwage', 'wage', df['wage'], sm.add_constant(df[['looks', 'educ', 'exper', 'female']])),
        ('looks', 'married', df['lwage'], sm.add_constant(df[['married', 'educ', 'exper', 'female']])),
        ('educ', 'goodhlth', df['lwage'], sm.add_constant(df[['looks', 'goodhlth', 'exper', 'female']])),
        ('exper', 'union', df['lwage'], sm.add_constant(df[['looks', 'educ', 'union', 'female']])),
        ('female', 'black', df['lwage'], sm.add_constant(df[['looks', 'educ', 'exper', 'black']]))
    ]

    def check(self, *args):
        # testing actual y and X
        x.grading_df_series(("y", Question11B._expected[0], args[0]))
        x.grading_df_series(("X", Question11B._expected[1], args[1]))

        for test in self._test_cases:

            actual_source = x.get_source_code("lab3", 83)
            filtered_actual_source = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual_source, "lab3", 83, test[0], test[1], "y, X")
            test_source = x.update_x_in_code(filtered_actual_source, test[0], test[1])

            previous = x.get_multiple_cell_source("lab3", [10, 80])
            combined_source = "import pandas as pd\n" + previous + "\n" + test_source
            updated_source = x.filter_source(combined_source, '#')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}

            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_y = local_vars.get('y')
            executed_X = local_vars.get('X')

            x.grading_df_series((test[1], "y", test[2], executed_y), var="test")
            x.grading_df_series((test[1], "X", test[3], executed_X), var="test")

class Question11C(EqualityCheckProblem):
    y, X = Question11B._expected
    def produce_expected(data1, data2):
        model = sm.OLS(data1, data2).fit()
        
        return model

    _var = 'model'
    _expected = produce_expected(y, X)

    _test_cases = [ 
        ('X', 'y', produce_expected(y, y), """                            OLS Regression Results                            
==============================================================================
Dep. Variable:                  lwage   R-squared:                       0.336
Model:                            OLS   Adj. R-squared:                  0.334
Method:                 Least Squares   F-statistic:                     158.8
Prob (F-statistic):          5.55e-110
Log-Likelihood:                -874.18
No. Observations:                1260   AIC:                             1758.
Df Residuals:                    1255   BIC:                             1784.
Df Model:                           4                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.5061      0.097      5.203      0.000       0.315       0.697
looks          0.0527      0.020      2.586      0.010       0.013       0.093
educ           0.0708      0.005     13.238      0.000       0.060       0.081
exper          0.0140      0.001     11.577      0.000       0.012       0.016
female        -0.4643      0.030    -15.643      0.000      -0.523      -0.406
==============================================================================
Omnibus:                       54.959   Durbin-Watson:                   1.886
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              145.029
Skew:                           0.174   Prob(JB):                     3.22e-32
Kurtosis:                       4.625   Cond. No.                         176.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.""")
    ]

    def check(self, *args):
        for test in self._test_cases:
            # testing actual model
            x.grading_equal(("model", type(Question11C._expected), type(args[0])))

            # Define the relevant attributes to compare
            relevant_attributes = ['params', 'resid', 'rsquared']

                # Compare based on attribute
            for attr in relevant_attributes:
                expected_attr_value = getattr(Question11C._expected, attr)
                actual_attr_value = getattr(args[0], attr)
                if attr == 'params':
                    # Compare using numpy's allclose for arrays with floating-point values
                    x.grading_npallclose((f"model.{attr}", expected_attr_value, actual_attr_value))
                elif attr == 'resid':
                    # Compare residuals to ensure they are within a small tolerance of zero
                    x.grading_npallclose((f"model.{attr}", expected_attr_value, actual_attr_value))

                elif attr == 'rsquared':
                    # Compare R-squared values to ensure they are within a small tolerance of 1.0
                    x.grading_npisclose((f"model.{attr}", expected_attr_value, actual_attr_value))
                                        
            for test in self._test_cases:
                actual_source = x.get_source_code("lab3", 86)
                filtered_actual_source = x.filter_source(actual_source, '#')
                filtered_actual_source = x.filter_source(filtered_actual_source, 'print')
 
                x.test_for_none_588(filtered_actual_source, "lab3", 86, test[0], test[1], "model")
                test_source = x.update_x_in_code(filtered_actual_source, test[0], test[1])

                previous = x.get_multiple_cell_source("lab3", [10, 80, 83])
                combined_source = "import pandas as pd\n" + previous + "\n" + test_source
                updated_source = x.filter_source(combined_source, '#')
                updated_source = x.filter_source(updated_source, 'print')

                # Create a dictionary to capture the local variables and assessment results
                local_vars = {}

                # Execute the code in test_source within the local_vars context
                try:
                    exec(updated_source, None, local_vars)
                except Exception as e:
                    print(f"Error executing code: {e}")
                    raise e
                
                executed_model = local_vars.get('model')

                x.grading_equal((test[1], f"model", type(test[2]), type(executed_model)), var="test")

            for attr in relevant_attributes:
                expected_attr_value = getattr(test[2], attr)
                actual_attr_value = getattr(executed_model, attr)
                if attr == 'params':
                    # Compare using numpy's allclose for arrays with floating-point values
                    x.grading_npallclose((f"{test_source}", attr, expected_attr_value, actual_attr_value), var="test")

                elif attr == 'resid':
                    # Compare residuals to ensure they are within a small tolerance of zero
                    x.grading_npallclose((f"{test_source}", attr, expected_attr_value, actual_attr_value), var="test") 
                
                elif attr == 'rsquared':
                    x.grading_npisclose((f"{test_source}", attr,expected_attr_value, actual_attr_value), var="test")

            # test print out
            cell_numbers = [10, 80, 83, 86]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab3", item)
                previous = previous + "\n" + current
        
            source = "import pandas as pd\n" + previous

            # print("----source----")
            # print(source)

            # lines below : remove comments and pass + fix indentation in source code
            lines = source.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('#')]
            filtered_lines2 = [line for line in filtered_lines if not line.lstrip().startswith('pass')]
            updated_source = '\n'.join(['    ' + line for line in filtered_lines2]) 

            print(str(Question11C._expected))
            fn_name = "fn"
            fn_source = f"def fn():\n{updated_source}"
            # Execute the function definition
            exec(fn_source, globals())
            
            # Access the dynamically created function by its name
            fn = globals()[fn_name]
            out, actual = x.compare_printout(fn)

            # Split the actual output into lines
            actual_lines = out.split('\n')
            
            # Remove the date and time parts of the relevant lines
            import re
            filtered_actual_lines = []
            for line in actual_lines:
                if line.startswith('Date:'):
                    line = re.sub(r'Date:\s+\S+\s+\S+\s+\S+\s+\S+\s+', '', line)  # Remove the date part
                if line.startswith('Time:'):
                    line = re.sub(r'Time:\s+\S+\s+', '', line)  # Remove the time part
                filtered_actual_lines.append(line)

            # Join the filtered lines back into a string
            filtered_actual_output = '\n'.join(filtered_actual_lines)
            
            # Strip any leading/trailing whitespace from the expected output
            expected_output = test[3].strip()
            
            # Strip any leading/trailing whitespace from the actual output
            filtered_actual_output = filtered_actual_output.strip()

            x.determine_the_grading_method(("print(model.summary())", expected_output, filtered_actual_output))


Question11 = MultipartProblem(
    Question11A,
    Question11B,
    Question11C
)    