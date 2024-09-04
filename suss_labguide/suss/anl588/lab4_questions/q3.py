from learntools.core import *
from ...dev import x
import matplotlib.pyplot as plt
from ..lab4_questions.q2 import Question2E
import seaborn as sns
import pandas as pd

class Question3A(EqualityCheckProblem):
    df = Question2E._expected

    def produce_expected(xlabel, kind, data1, hue1, alpha1):
        plt.close('all')
        df = Question2E._expected
        catplot = sns.catplot(x=xlabel, kind = kind, data=data1, hue=hue1, alpha = alpha1);
        return catplot

    # _var = "df1"
    # _expected = produce_expected()

    _test_cases = [
        ("df", "pd.DataFrame({'DEFAULT': [0, 0, 0, 0, 0, 0],'SEX': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']})", "DEFAULT", "count", pd.DataFrame({'DEFAULT': [0, 0, 0, 0, 0, 0],'SEX': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']}), "SEX", 0.5),
        ("DEFAULT", "AGE", "AGE", "count", df, "SEX", 0.5),
        ("count", "violin", "DEFAULT", "violin", df, "SEX", 0.5),
        ("SEX", "EDUCATION", "DEFAULT", "count", df, "EDUCATION", 0.5),
        ("0.5", "0", "DEFAULT", "count", df, "SEX", 0)
]

    def check(self, *args):

        plt.ioff()
        source = x.get_source_code("lab4", 31)
        
        filtered_source = x.filter_source(source, '#')
        # assert seaborn used
        if "sns.catplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.catplot", "`sns.catplot` is not used. Please use `sns.catplot` to construct a frequency plot.")

        lines = filtered_source.split('\n')
        sns_catplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.catplot'):
                sns_catplot_line = 'catplot = ' + line.rstrip(';') 

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25])
        combined_source = "import pandas as pd\n" + previous + "\n" + sns_catplot_line

        expected_plot = Question3A.produce_expected("DEFAULT", "count", Question3A.df, "SEX", 0.5)
        
        # Clear any previous (expected_plot) figures
        plt.close("all")
        plt.figure()

        variables = {}
        exec(combined_source, globals(), variables)
        actual_plot = variables.get("catplot")
        x.grading_anl588_seaborn_catplot((actual_plot, expected_plot), "alpha")

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_catplot_line, "lab4", 31, test[0], test[1], "sns.catplot")
            test_source = x.update_x_in_code(sns_catplot_line, test[0], test[1])
            test_source = "import pandas as pd\n" + previous + "\n" + test_source
            expected_plot = Question3A.produce_expected(test[2], test[3], test[4], test[5], test[6])
            plt.close("all")
            plt.figure()
            
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('catplot')

            x.grading_anl588_seaborn_catplot((actual_plot, expected_plot), "alpha")
            plt.close('all')
            

class Question3B(EqualityCheckProblem):
    df = Question2E._expected

    def produce_expected(xlabel, ylabel, kind, data1, hue1, palette1):
        plt.close('all')
        df = Question2E._expected
        catplot = sns.catplot(x = xlabel, y=ylabel, kind = kind, data=data1, hue=hue1, palette=palette1);
        return catplot

    # _var = "df1"
    # _expected = produce_expected()

    _test_cases = [
        ("df", "pd.DataFrame({'DEFAULT': [0, 0, 0, 0, 0, 0], 'LIMIT_BAL': [0, 0, 0, 0, 0, 0], 'SEX': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']})", "DEFAULT", "LIMIT_BAL", "box", pd.DataFrame({'DEFAULT': [0, 0, 0, 0, 0, 0],'LIMIT_BAL': [0, 0, 0, 0, 0, 0], 'SEX': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female']}), "SEX", "Dark2"),
        ("DEFAULT", "AGE", "AGE", "LIMIT_BAL", "box", df, "SEX", "Dark2"),
        ("LIMIT_BAL", "AGE", "DEFAULT", "AGE", "box", df, "SEX", "Dark2"),
        ("box", "violin", "DEFAULT", "LIMIT_BAL", "violin", df, "SEX", "Dark2"),
        ("SEX", "EDUCATION", "DEFAULT", "LIMIT_BAL", "box", df, "EDUCATION", "Dark2"),
        ("Dark2", "Paired", "DEFAULT", "LIMIT_BAL", "box", df, "SEX", "Paired")
]

    def check(self, *args):

        plt.ioff()
        source = x.get_source_code("lab4", 34)        
        filtered_source = x.filter_source(source, '#')
        # assert seaborn used
        if "sns.catplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.catplot", "`sns.catplot` is not used. Please use `sns.catplot` to construct a frequency plot.")

        lines = filtered_source.split('\n')
        sns_catplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.catplot'):
                sns_catplot_line = 'catplot = ' + line.rstrip(';') 

        previous = x.get_multiple_cell_source("lab4", [7, 22, 25])
        combined_source = "import pandas as pd\n" + previous + "\n" + sns_catplot_line

        expected_plot = Question3B.produce_expected("DEFAULT", "LIMIT_BAL", "box", Question3B.df, "SEX", "Dark2")
        
        # Clear any previous (expected_plot) figures
        plt.close("all")
        plt.figure()

        variables = {}
        exec(combined_source, globals(), variables)
        actual_plot = variables.get("catplot")
        actual_axes = actual_plot.ax
        expected_axes = expected_plot.ax 
        # Get the y-axis label
        actual_y_label = actual_axes.get_ylabel() if actual_axes.get_ylabel() else x.justfail("ylabel", "The `y-axis` label is not used. Please use the `y` parameter in the catplot function.")
        expected_y_label = expected_axes.get_ylabel()

        assert actual_y_label == expected_y_label, ("""
The `y-axis` label is incorrect. Expected the `y-axis` label to be:                                     
<pre>`{}`</pre>
                                                    
but got the following instead:
<pre>`{}`</pre>
                                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_y_label), str(actual_y_label), x.get_edits_string(str(expected_y_label), str(actual_y_label)))

        x.grading_anl588_seaborn_catplot((actual_plot, expected_plot), "palette")

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_catplot_line, "lab4", 34, test[0], test[1], "sns.catplot")
            test_source = x.update_x_in_code(sns_catplot_line, test[0], test[1])
            test_source = "import pandas as pd\n" + previous + "\n" + test_source
            expected_plot = Question3B.produce_expected(test[2], test[3], test[4], test[5], test[6], test[7])
            plt.close("all")
            plt.figure()
            
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('catplot')

            x.grading_anl588_seaborn_catplot((actual_plot, expected_plot), "palette")
            plt.close('all')

Question3 = MultipartProblem(
    Question3A,
    Question3B
)    