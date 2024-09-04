from learntools.core import *
from ...dev import x
from sklearn.linear_model import LinearRegression
from ..lab3_questions.q5 import Question5
import seaborn as sns
import matplotlib.pyplot as plt

class Question9A(EqualityCheckProblem):
    
    X_train, X_test, y_train, y_test = Question5._expected
    
    def produce_expected(data):
        X_train, X_test, y_train, y_test = Question5._expected
        model = LinearRegression()
        model.fit(X_train, y_train)
        test_pred = model.predict(data)
        
        return test_pred

    _var = "test_pred"
    _expected = produce_expected(X_test)

    _test_cases = [ 
        ('X_test', 'X_train', produce_expected(X_train))
    ]

    def check(self, *args):
        # testing actual test_pred
           
        source = x.get_source_code("lab3", 61)
        actual_source = x.filter_source(source, '#')
  
        previous = x.get_multiple_cell_source("lab3", [10, 31, 34, 39, 43, 44, 53, 57])
        filtered_source = x.filter_source(previous, '#')
        
        combined_source = "import pandas as pd\n" + filtered_source + "\n" + actual_source
        
        # Create a dictionary to capture the local variables and assessment results
        local_vars = {}
        
        # Execute the code in test_source within the local_vars context
        try:
            exec(combined_source, None, local_vars)
        except Exception as e:
            print(f"Error executing code: {e}")
            raise e
        
        executed_test_pred = local_vars.get('test_pred')
        
        x.grading_nparray2(("test_pred", Question9A._expected, executed_test_pred))
        
        for test in self._test_cases:
            x.test_for_none_588(actual_source, "lab3", 61, test[0], test[1], "test_pred")
            test_source = x.update_x_in_code(actual_source, test[0], test[1])
            combined_source2 = "import pandas as pd\n" + filtered_source + "\n" + test_source
            
            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(combined_source2, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
            
            executed_test_pred2 = local_vars.get('test_pred')
            
            x.grading_nparray2((f"{test_source}", "test_pred", test[2], executed_test_pred2), var="test")

class Question9B(EqualityCheckProblem):
    X_train, X_test, y_train, y_test = Question5._expected
    test_pred = Question9A.produce_expected(X_test)

    def produce_expected(x_data, y_data):
        plt.close("all")
        scatterplot = sns.scatterplot(x = x_data, y = y_data, size = 3, alpha = 0.5, color = "orange");
        plt.xlabel("Actual Target Values")
        plt.ylabel("Predicted Target Values")
        plt.xticks(list(range(0,30,5))) ;
        plt.yticks(list(range(0,30,5))) ;
        plt.xlim([0,20]);
        plt.ylim([0,20]);
        
        return scatterplot

    # _var = "test_pred"
    # _expected = produce_expected(y_test, test_pred)

    _test_cases = [ 
        ('test_pred', 'y_test', y_test, y_test)
    ]

    def check(self, *args):
        # actual test
        plt.ioff()
        source = x.get_source_code("lab3", 64)
        filtered_source = x.filter_source(source, '#')

        # assert seaborn used
        if "sns.scatterplot" in filtered_source:
            x.justpass()
        else:
            x.justfail("sns.scatterplot", "`sns.scatterplot` is not used. Please use `sns.scatterplot` to construct a scatterplot.")

        # we want to return the pairplot to retrieve the actual pairplot object details
        lines = filtered_source.split('\n')
        filtered_lines = []
        sns_scatterplot_line = None
        
        for line in lines:
            if line.lstrip().startswith('sns.scatterplot'):
                sns_scatterplot_line = 'scatterplot = ' + line.rstrip(';')  # Store the line starting with 'sns.scatterplot'
            else:
                filtered_lines.append(line) # Store the rest into filtered lines

        updated_source = '\n'.join(filtered_lines)
        
        previous = x.get_multiple_cell_source("lab3", [10, 31, 34, 39, 43, 44, 53, 57, 61])
        filtered_source2 = x.filter_source(previous, '#')

        updated_source2 = "import pandas as pd\n" + filtered_source2 + "\n" + sns_scatterplot_line + "\n" + updated_source

        variables = {}
        exec(updated_source2, globals(), variables)

    
        expected_plot = Question9B.produce_expected(Question9B.y_test, Question9B.test_pred) 
        plt.close("all")
        plt.figure()  
        actual_plot = variables.get("scatterplot")

        x.grading_anl588_seaborn_scatterplot(actual_plot, expected_plot)

        for test in self._test_cases:
            print("Testing test cases...")
            x.test_for_none_588(sns_scatterplot_line, "lab3", 64, test[0], test[1], "sns.scatterplot")
            test_source = x.update_x_in_code(sns_scatterplot_line, test[0], test[1])
            test_source =  "import pandas as pd\n" + filtered_source2 + "\n" + test_source + "\n" + updated_source
            expected_plot = Question9B.produce_expected(test[2], test[3])
            plt.close("all")
            plt.figure()
            
            variables = {}
            exec(test_source, globals(), variables)
            actual_plot = variables.get('scatterplot')

            x.grading_anl588_seaborn_scatterplot(actual_plot, expected_plot)
            plt.close('all')

Question9 = MultipartProblem(
    Question9A,
    Question9B
)    