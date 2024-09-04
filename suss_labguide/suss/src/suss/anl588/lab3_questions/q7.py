from learntools.core import *
from ...dev import x
from sklearn.linear_model import LinearRegression

class Question7(EqualityCheckProblem):

    def produce_expected():
        model = LinearRegression()
        
        return model

    _var = "model"
    _expected = produce_expected()

    # _test_cases = [ 
    #     ('0.3', '0.1', 'test_size', produce_expected(0.1, 101)),
    #     ('101', '100', 'random_state', produce_expected(0.3, 100))
    # ]

    def check(self, *args):
        # testing actual model
           
        source = x.get_source_code("lab3", 53)
        actual_source = x.filter_source(source, '#')    
        
        x.determine_the_grading_method(("model", f"model = {Question7._expected}", str(actual_source)))
          
