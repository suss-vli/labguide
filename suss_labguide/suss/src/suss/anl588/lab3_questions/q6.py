from learntools.core import *
from ...dev import x

class Question6(EqualityCheckProblem):

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
  
        source = x.get_source_code("lab3", 49)
        updated_source = x.filter_source(source, '#')
        
        if "from sklearn.linear_model import LinearRegression" in updated_source:
            x.justpass()
        else:
            x.justfail("from sklearn.linear_model import LinearRegression", "`from sklearn.linear_model import LinearRegression` is not found. Please import LinearRegression from sklearn.linear_model.")
