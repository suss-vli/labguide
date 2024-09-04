from learntools.core import *
from ...dev import x
import os
import sys
import io
import pandas as pd
from ..lab6_questions.q2 import Question2C
from mlxtend.frequent_patterns import apriori, association_rules
# from apyori import apriori
import numpy as np


class Question3A(EqualityCheckProblem):

    def produce_expected(input1, input2):
        dfa = Question2C.produce_expected('category')
        dfa = pd.get_dummies(dfa)
        dfa = dfa.astype(int)
        results = apriori(dfa.astype('bool'), 
                  min_support = 0.1, 
                  use_colnames = True, 
                  verbose = 1,)
        rules = association_rules(results, metric ="lift", min_threshold = 1)
        rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
        rules_fail = rules[rules[input1] == {input2}].head(10)

        return rules_fail
    
    _var = 'rules_fail'
    _expected = produce_expected('consequents', 'OUTCOME_out_fail')

    _test_cases = [
        ('OUTCOME_out_fail', 'AGE_old', produce_expected('consequents', 'AGE_old')),
        ('OUTCOME_out_fail', 'WILLPOWR_will_no', produce_expected('consequents', 'WILLPOWR_will_no')),
        ('consequents', 'antecedents', produce_expected('antecedents', 'OUTCOME_out_fail')),
    ]

    def check(self, *args):
        # testing actual value of dfa
        actual_source = x.get_source_code("lab6", 40)
        filtered_actual = x.filter_source(actual_source, '#')

        # if "consequents" in filtered_actual:
        #     x.justpass()
        # else:
        #     x.justfail("consequents", "`consequents` is not found. Please use `consequents` to choose the fail outcome to focus.")
        
        # if "OUTCOME_out_fail" in filtered_actual:
        #     x.justpass()
        # else:
        #     x.justfail("OUTCOME_out_fail", "`OUTCOME_out_fail` is not found. Please use `OUTCOME_out_fail` as the outcome to focus.")
        
        if ".head" in filtered_actual:
            x.justpass()
        else:
            x.justfail(".head()", "`.head()` is not used. Please use `.head(10)` to report the top 10 results.")
        

        x.grading_df_series(("rules_fail", Question3A._expected, args[0]))

        for test in self._test_cases:

            x.test_for_none_588(filtered_actual, "lab6", 40, test[0], test[1], "rules[rules['consequents'] == {'OUTCOME_out_fail'}].head(10)")
            updated_source = x.update_x_in_code(filtered_actual, test[0], test[1])

            source = x.get_multiple_cell_source("lab6", [4, 6, 16, 19, 24, 31, 33, 35])
            filtered_source = x.filter_source(source, '#')
            filtered_source = x.filter_source(filtered_source, '%')

            combined_source = "import pandas as pd\n" + filtered_source + "\n" + updated_source

            variables = {}
            exec(combined_source, globals(), variables)
            actual_rules_fail = variables.get('rules_fail')

            x.grading_df_series((test[1], "rules_fail", test[2], actual_rules_fail), var="test")


class Question3B(EqualityCheckProblem):

    def produce_expected():
      failed_attr = ["AGE_old", "WILLPOWR_will_no"]
      
      return failed_attr

    _var = 'failed_attr'
    _expected = produce_expected()
    
    _test_cases = [
        ('AGE_old', 'AGE_young', ['AGE_young', 'WILLPOWR_will_no']),
        ('AGE_old', 'RACE_chinese', ['RACE_chinese', 'WILLPOWR_will_no']),
        ('WILLPOWR_will_no', 'WILLPOWR_will_yes', ['AGE_old', 'WILLPOWR_will_yes']),
        ('WILLPOWR_will_no', 'EDUCATN_alevel', ['AGE_old', 'EDUCATN_alevel'])
]

    def check(self, *args):
        x.grading_equal(("failed_attr", Question3B._expected, args[0]))

        for test in self._test_cases:

            actual_source = x.get_source_code("lab6", 43)
            filtered_actual = x.filter_source(actual_source, '#')

            x.test_for_none_588(filtered_actual, "lab6", 43, test[0], test[1], "failed_attr")
            updated_source = x.update_x_in_code(filtered_actual, test[0], test[1])

            variables = {}
            exec(updated_source, globals(), variables)
            
            executed_failed_attr =  variables.get('failed_attr')

            x.grading_equal((test[1], "failed_attr", test[2], executed_failed_attr), var="test")


Question3 = MultipartProblem(
    Question3A, 
    Question3B
)
