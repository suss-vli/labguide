from learntools.core import *
from ...dev import x
import pandas as pd

class Question3A(EqualityCheckProblem):

    def produce_expected():
        s1 = pd.Series([75, 56, 64, 82, 89])
        s2 = pd.Series([84, 47, 61, 72, 80])
        
        return s1, s2

    _vars = ['s1', 's2']
    _expected = produce_expected()

    _test_cases = [
        ([75, 56, 64, 82, 89], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], pd.Series([0, 0, 0, 0, 0]), [84, 47, 61, 72, 80], pd.Series([84, 47, 61, 72, 80])),
        ([84, 47, 61, 72, 80], [0, 0, 0, 0, 0], [75, 56, 64, 82, 89], pd.Series([75, 56, 64, 82, 89]), [0, 0, 0, 0, 0], pd.Series([0, 0, 0, 0, 0]))
    ]

    def check(self, *args):
        # testing actual value of s1
        x.grading_df_series(("s1", Question3A._expected[0], args[0]))

        # testing actual value of s2
        x.grading_df_series(("s2", Question3A._expected[1], args[1]))

        for test in self._test_cases:
            #replacing s1 / s2
            source = x.get_source_code("lab2b", 92)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 92, test[0], test[1], f"pd.Series({test[0]})", var="list")
            test_source = x.update_list_in_code(source, test[0], test[1])
            # print("----test_source----")
            # print(test_source)

            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_s1 = local_vars.get('s1')
            executed_s2 = local_vars.get('s2')

            x.grading_df_series((f"s1 = pd.Series({test[2]})", "s1", test[3], executed_s1), var="test")
            x.grading_df_series((f"s2 = pd.Series({test[4]})", "s2", test[5], executed_s2), var="test")

class Question3B(EqualityCheckProblem):

    def produce_expected():
        
        name_id = pd.Series(["Abe", "Ben", "Carl", "Dee", "Eun"])
        subject_id = pd.Series(["Stat","Math"])
        
        return name_id, subject_id

    _vars = ['name_id', 'subject_id']
    _expected = produce_expected()

    _test_cases = [
        (["Abe", "Ben", "Carl", "Dee", "Eun"], ["Z", "Y", "X", "W", "V"], ["Z", "Y", "X", "W", "V"], pd.Series(["Z", "Y", "X", "W", "V"]), ["Stat","Math"], pd.Series(["Stat","Math"])),
        (["Stat","Math"], ["Data","science"], ["Abe", "Ben", "Carl", "Dee", "Eun"], pd.Series(["Abe", "Ben", "Carl", "Dee", "Eun"]), ["Data","science"], pd.Series(["Data","science"]))
    ]

    def check(self, *args):
        # testing actual value of name_id
        x.grading_df_series(("name_id", Question3B._expected[0], args[0]))

        # testing actual value of subject_id
        x.grading_df_series(("subject_id", Question3B._expected[1], args[1]))

        for test in self._test_cases:
            source = x.get_source_code("lab2b", 95)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 95, test[0], test[1], f"pd.Series({test[0]})", var="list")
            test_source = x.update_list_in_code(source, test[0], test[1])
            # print("----test_source----")
            # print(test_source)
    
            updated_source = x.filter_source(test_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_nameid = local_vars.get('name_id')
            executed_subjectid = local_vars.get('subject_id')

            x.grading_df_series((f"name_id = pd.Series({test[2]})", "name_id", test[3], executed_nameid), var="test")
            x.grading_df_series((f"subject_id = pd.Series({test[4]})", "subject_id", test[5], executed_subjectid), var="test")

class Question3C(EqualityCheckProblem):

    def produce_expected():
        s1 = pd.Series([75, 56, 64, 82, 89])
        s2 = pd.Series([84, 47, 61, 72, 80])
        name_id = pd.Series(["Abe", "Ben", "Carl", "Dee", "Eun"])
        subject_id = pd.Series(["Stat","Math"])
        scores = pd.concat([s1, s2], axis = 1)
        scores.index = name_id
        scores.columns = subject_id 

        return scores

    _var = 'scores'
    _expected = produce_expected()

    _test_cases = [
        ("s1", "pd.Series([0, 0, 0, 0, 0])", pd.DataFrame({'Stat': [0, 0, 0, 0, 0], 'Math': [84, 47, 61, 72, 80]}, index=['Abe', 'Ben', 'Carl', 'Dee', 'Eun'])),
        ("s2", "pd.Series([0, 0, 0, 0, 0])", pd.DataFrame({'Stat': [75, 56, 64, 82, 89], 'Math': [0, 0, 0, 0, 0]}, index=['Abe', 'Ben', 'Carl', 'Dee', 'Eun'])),
    ]

    def check(self, *args):
        # testing actual value of scores
        x.determine_the_grading_method(("scores", Question3C.produce_expected(), args[0]))
        #testing actual value of scores.index and scores.column
        x.grading_df_series(("scores.index", Question3C.produce_expected().index, args[0].index))
        x.grading_df_series(("scores.columns", Question3C.produce_expected().columns, args[0].columns))

        source = x.get_source_code("lab2b", 98)
        if "pd.concat(" in source:
            x.justpass()
        else:
            x.justfail("pd.concat", "`pd.concat` is not used. Please use `pd.concat` to combine the pandas series into the dataframe.")
        if "axis=1" or "axis= 1" or "axis =1" or "axis = 1" in source:
            x.justpass()
        else:
            x.justfail("axis=1", "`axis=1` option is not used. Please use the option for your `pd.concat()`.")


        for test in self._test_cases:
            
            #replacing name_id/ subject_id
            source = x.get_source_code("lab2b", 98)
            # # print("----source----")
            # # print(source)

            x.test_for_none_588(source, "lab2b", 98, test[0], test[1], f"{test[0]}")
            test_source = x.update_x_in_code(source, test[0], test[1])
   
            source2 = x.get_multiple_cell_source("lab2b", [92, 95])

            combined_source = source2 + "\n" + test_source
            updated_source = x.filter_source(combined_source, 'print')

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(updated_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_scores = local_vars.get('scores')

            x.determine_the_grading_method((test[1], test[2], executed_scores))

Question3 = MultipartProblem(
    Question3A,
    Question3B,
    Question3C
)    