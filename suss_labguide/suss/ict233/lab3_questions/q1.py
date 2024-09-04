import re
import requests
from ...dev import x
from learntools.core import *
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Todo
# check the prescence of seminar2_activity2.db
# check the presence of csv
# check the validity of seminar2_activity2.db by calling it and running some function through it
# check the validity of csv by looping through it 

# checking easy_way function as functionalCheck

class Question1(EqualityCheckProblem):
    def produce_expected_df(file_name):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file_name # change name of file to make it clear its our copy
        df = pd.read_csv(expected_file)
        df_expected = df.replace('\'','', regex=True)
        return df_expected
        
    def produce_expected_fig(file_name):
        # plt.ioff()
        expected_fig = plt.figure()
        expected_axes1 = expected_fig.add_subplot(1,1,1)
        # scatterplot
        expected_axes1.scatter(Question1.produce_expected_df(file_name)['FMR'],Question1.produce_expected_df(file_name)['LMED'])
        expected_axes1.set_title('Scatterplot of FMR VS LMED')
        expected_axes1.set_xlabel('FMR')
        expected_axes1.set_ylabel('LMED')
        # plt.close(expected_fig)
        return expected_fig

    _vars=["df", "fig"]
    # _expected = [produce_expected_df(), produce_expected_fig()]

    _test_cases = [
        ('test_dataset_2013.txt'),
        ('test_case_dataset_2009.txt')]

    def check(self, *args):
        for test in self._test_cases:
            # super().check(*args)
            plt.ioff()
            
            #getting all source code cells for q1a
            cell_numbers = [4,5,9]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab3", item)
                previous = previous + "\n" + current
            
            # adding in plt cell
            previous = previous + "\n" + "plt.ioff()" + "\n" + x.get_source_code("lab3", 9)
            
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test
            update_df = x.update_csv_in_code(previous, new_csv, "df") # need to specify df in the question

            lines = update_df.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('%')]
            filtered_lines = [line for line in filtered_lines if not line.lstrip().startswith('print')]
            updated_source = '\n'.join(filtered_lines)        
            
            # print(updated_source)

            variables = {}
            exec(updated_source, globals(), variables)
            
            df_actual =  variables.get('df')      
            expected_df = Question1.produce_expected_df(test)
        
            x.determine_the_grading_method(("df", expected_df, df_actual))

            x.determine_the_grading_method(("df.head()", expected_df.head(), df_actual.head()))
            # x.determine_the_grading_method(("df.info()", expected_df.info(), df_actual.info()))
            

            actual_fig = variables.get('fig')
            expected_fig = Question1.produce_expected_fig(test)
        
            # gettting the x and y data from the actual and expected figure
            actual_x_data, actual_y_data = x.get_x_y_data_from_plt(actual_fig)
            expected_x_data, expected_y_data = x.get_x_y_data_from_plt(expected_fig)
            
            # Compare x data
            assert all(a == b for a, b in zip(actual_x_data, expected_x_data)), "The X data is incorrect."

            # Compare y data
            assert all(a == b for a, b in zip(actual_y_data, expected_y_data)), "The Y data is incorrect."

            # grading the figure - axes, title, xlabel, ylabel
            x.grading_plt_figure(actual_fig, expected_fig) 

            plt.close('all')      
        
        
    def solution_plot(self):
        self._view.solution() # this will show the solution code, uncomment when solution is ready
        # TODO 2024: need to change solution_plot so it will coincide with .solution() - only display after a few tries
        file_name = 'test_dataset_2013.txt'
        plt.ioff()
        plt.close('all')
        expected_fig = plt.figure()
        expected_axes1 = expected_fig.add_subplot(1,1,1)
        # scatterplot
        expected_axes1.scatter(Question1.produce_expected_df(file_name)['FMR'],Question1.produce_expected_df(file_name)['LMED'])
        expected_axes1.set_title('Scatterplot of FMR VS LMED')
        expected_axes1.set_xlabel('FMR')
        expected_axes1.set_ylabel('LMED')
        plt.show()
