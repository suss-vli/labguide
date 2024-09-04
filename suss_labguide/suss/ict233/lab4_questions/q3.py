from ...dev import x
from learntools.core import *
import os
import pandas as pd
from .q2 import Question2

class Question3(CodingProblem):

    def produce_expected(self, employment_rate_file, labour_rate_file):

        expected_combine_both = Question2.produce_expected(self, employment_rate_file, labour_rate_file)
        expected_combine_both['employment_rate_percent'].fillna('Unknown', inplace=True)

        return expected_combine_both

    _var= "combine_both" # need to specify these variables in the question - TODO: possible namespace confusion with q2

    _test_cases = [
        ('employment_rate_test.csv', 'labour_force_participation_test.csv', 'test_females_aged_15plus_employment_rate_percent.csv', 'test_females_aged_15plus_labour_force_participation_rate_percent.csv')
    ]

    def check(self, *args):
        for test in self._test_cases:
            actual_combine_both = args[0]

            expected_combine_both = self.produce_expected(test[0], test[1])
            x.determine_the_grading_method(("combine_both", expected_combine_both, actual_combine_both))

            # for test cases:
            
            #getting all source code cells for q3
            cell_numbers = [4,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,48,49,50,51,52]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab4", item)
                previous = previous + "\n" + current
            
            # update employment rate csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[2]
            updated_employment_rate_source = x.update_csv_in_code(previous, new_csv, "aged_15plus_employment_rate_percent")
            
            
            # # update labour rate csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[3]
            updated_source = x.update_csv_in_code(updated_employment_rate_source, new_csv, "aged_15plus_labour_force_participation_rate_percent")
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_test_combine_both =  variables.get('combine_both')
            expected_test_combine_both = self.produce_expected(test[2], test[3])
            x.determine_the_grading_method(("combine_both", expected_test_combine_both, actual_test_combine_both))