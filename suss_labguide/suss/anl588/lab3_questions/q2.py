from learntools.core import *
from ...dev import x
from ..lab3_questions.q1 import Question1
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

class Question2A(EqualityCheckProblem):
    df = Question1._expected
    def produce_expected(var1, var2, var3, data1, hue1):
        
        pairplot = sns.pairplot(vars=[var1, var2, var3], data = data1, hue= hue1);
        
        return pairplot
    
    # _vars = ["wage", "educ", "exper"]
    # _expected = produce_expected("wage", "educ", "exper", df, "female")
    
    _test_cases = [
        ("wage", "lwage", "lwage", "educ", "exper", df, "female"),
        ("educ", "looks", "wage", "looks", "exper", df, "female"),
        ("exper", "married", "wage", "educ", "married", df, "female"),
        ("df", "pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'educ': [0, 0, 0, 0, 0], 'exper': [0, 0, 0, 0, 0], 'female': [0, 0, 0, 0, 0]})", "wage","educ", "exper", pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'educ': [0, 0, 0, 0, 0], 'exper': [0, 0, 0, 0, 0], 'female': [0, 0, 0, 0, 0]}), "female"),
        ("female", "black", "wage", "educ", "exper", df, "black")
]
    
    def check(self, *args):
        # actual test
        plt.ioff()
        source = x.get_source_code("lab3", 20)
        filtered_source = x.filter_source(source, '#')

        # assert seaborn used
        if "sns.pairplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.pairplot", "`sns.pairplot` is not used. Please use `sns.pairplot` to construct a pairplot.")

        # we want to return the pairplot to retrieve the actual pairplot object details
        lines = filtered_source.split('\n')
        sns_pairplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.pairplot'):
                sns_pairplot_line = 'pairplot = ' + line.rstrip(';')  # Store the line starting with 'sns.pairplot'

        updated_source = x.get_source_code("lab3", 10) + "\n" + sns_pairplot_line
        # print(updated_source)

        variables = {}
        exec(updated_source, globals(), variables)

    
        expected_plot = Question2A.produce_expected("wage", "educ", "exper", Question2A.df, "female")      
        actual_plot = variables.get("pairplot")
        x.grading_anl588_seaborn_pairplot((actual_plot, expected_plot))

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_pairplot_line, "lab3", 20, test[0], test[1], "sns.pairplot")
            test_source = x.update_x_in_code(sns_pairplot_line, test[0], test[1])
            test_source = x.get_source_code("lab3", 10) + "\n" + test_source
    
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('pairplot')
            expected_plot = Question2A.produce_expected(test[2], test[3], test[4], test[5], test[6])
            x.grading_anl588_seaborn_pairplot((actual_plot, expected_plot))
            
            plt.close('all')


class Question2B(EqualityCheckProblem):
    df = Question1._expected
    def produce_expected(data1, var1, var2):
        # Clear any previous figures before generating expected plot
        plt.close("all")
        
        histplot = sns.histplot(data = data1, x = var1, hue = var2)
        
        return histplot

    # _var = 'classnames'
    # _expected = produce_expected(df, "wage", "belavg")
    
    _test_cases = [
        ("df", "pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'belavg': [0, 0, 0, 0, 0]})", pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'belavg': [0, 0, 0, 0, 0]}), "wage", "belavg"),
        ("wage", "lwage", df, "lwage", "belavg"),
        ("belavg", "abvavg", df, "wage", "abvavg")
]

    def check(self, *args):
        plt.ioff()
        source = x.get_source_code("lab3", 23)
        
        filtered_source = x.filter_source(source, '#')
        # assert seaborn used
        if "sns.histplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.histplot", "`sns.histplot` is not used. Please use `sns.histplot` to construct a histogram.")

        lines = source.split('\n')
        filtered_lines = []
        sns_histplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.histplot'):
                sns_histplot_line = 'histplot = ' + line.rstrip(';')  # Store the line starting with 'sns.histplot'
            else:
                filtered_lines.append(line) # Store the rest into filtered lines
        
        updated_source = x.get_source_code("lab3", 10) + "\n" + sns_histplot_line
        
        # expected_plot = Question2B._expected # leaving this here for reminder: this does not seem to be able to get the proper expected_plot (thus incorrect length). need to test and see why this is the case, especially if we want to stick to using _expected variable
        # calling produce_expected here is able to retrieve the proper expected_plot histplot and its details
        expected_plot = Question2B.produce_expected(Question1._expected, "wage", "belavg")
        
        # Clear any previous (expected_plot) figures
        plt.close("all")
        plt.figure()

        variables = {}
        exec(updated_source, globals(), variables)
        actual_plot = variables.get("histplot")
        x.grading_anl588_seaborn_histplot((actual_plot, expected_plot))

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_histplot_line, "lab3", 23, test[0], test[1], "sns.histplot")
            test_source = x.update_x_in_code(sns_histplot_line, test[0], test[1])
            test_source = x.get_source_code("lab3", 10) + "\n" + test_source
            expected_plot = Question2B.produce_expected(test[2], test[3], test[4])
            plt.close("all")
            plt.figure()
            
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('histplot')

            x.grading_anl588_seaborn_histplot((actual_plot, expected_plot))
            plt.close('all')
            
class Question2C(EqualityCheckProblem):
    df = Question1._expected
    def produce_expected(data1, var1, var2):
        # Clear any previous figures before generating expected plot
        plt.close("all")
        
        histplot = sns.histplot(data = data1, x = var1, hue = var2)
        
        return histplot

    # _var = 'classnames'
    # _expected = produce_expected(df, "wage", "abvavg")
    
    _test_cases = [
        ("df", "pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'abvavg': [0, 0, 0, 0, 0]})", pd.DataFrame({'wage': [0, 0, 0, 0, 0], 'abvavg': [0, 0, 0, 0, 0]}), "wage", "abvavg"),
        ("wage", "lwage", df, "lwage", "abvavg"),
        ("abvavg", "belavg", df, "wage", "belavg")
]

    def check(self, *args):
        plt.ioff()
        source = x.get_source_code("lab3", 26)
        
        filtered_source = x.filter_source(source, '#')
        # assert seaborn used
        if "sns.histplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.histplot", "`sns.histplot` is not used. Please use `sns.histplot` to construct a histogram.")

        lines = source.split('\n')
        filtered_lines = []
        sns_histplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.histplot'):
                sns_histplot_line = 'histplot = ' + line.rstrip(';')  # Store the line starting with 'sns.histplot'
            else:
                filtered_lines.append(line) # Store the rest into filtered lines
        
        updated_source = x.get_source_code("lab3", 10) + "\n" + sns_histplot_line
        
        # expected_plot = Question2B._expected # leaving this here for reminder: this does not seem to be able to get the proper expected_plot (thus incorrect length). need to test and see why this is the case, especially if we want to stick to using _expected variable
        # calling produce_expected here is able to retrieve the proper expected_plot histplot and its details
        expected_plot = Question2C.produce_expected(Question1._expected, "wage", "abvavg")
        
        # Clear any previous (expected_plot) figures
        plt.close("all")
        plt.figure()

        variables = {}
        exec(updated_source, globals(), variables)
        actual_plot = variables.get("histplot")
        x.grading_anl588_seaborn_histplot((actual_plot, expected_plot))

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_histplot_line, "lab3", 26, test[0], test[1], "sns.histplot")
            test_source = x.update_x_in_code(sns_histplot_line, test[0], test[1])
            test_source = x.get_source_code("lab3", 10) + "\n" + test_source
            expected_plot = Question2B.produce_expected(test[2], test[3], test[4])
            plt.close("all")
            plt.figure()
            
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('histplot')

            x.grading_anl588_seaborn_histplot((actual_plot, expected_plot))
            plt.close('all')
        
Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C
)