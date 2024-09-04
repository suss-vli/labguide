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
# Step 1: assign global_df
global_df = []
class Question1A(EqualityCheckProblem):
    def produce_expected(file_name):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + file_name # change name of file to make it clear its our copy
        df = pd.read_csv(expected_file)
        df_expected = df.replace('\'','', regex=True)
        return df_expected

    _var="df"
    # _expected = produce_expected()
    
    _test_cases = [
        ('test_dataset_2013.txt'),
        ('test_case_dataset_2009.txt')]

    def check(self, *args):
        for test in self._test_cases:
        # super().check(*args)
        # for arg in args:
        #     df_actual = arg
          #getting all source code cells for q1a
            cell_numbers = [4,5]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab3", item)
                previous = previous + "\n" + current
            
            # update datafile
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test
            update_df = x.update_csv_in_code(previous, new_csv, "df") # need to specify df in the question
            
            lines = update_df.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('print')]
            updated_source = '\n'.join(filtered_lines)        
            
            variables = {}
            exec(updated_source, globals(), variables)

            df_actual =  variables.get('df')      
            global global_df
            global_df.append(variables.get('df'))
            
            expected_df = Question1A.produce_expected(test)
        
            x.determine_the_grading_method(("df", expected_df, df_actual))

            x.determine_the_grading_method(("df.head()", expected_df.head(), df_actual.head()))
            # x.determine_the_grading_method(("df.info()", expected_df.info(), df_actual.info()))
            
        

class Question1B(CodingProblem):

    def produce_expected(test_case):
        plt.ioff()
        expected_fig = plt.figure()
        expected_axes1 = expected_fig.add_subplot(1,1,1)
        # scatterplot
        expected_axes1.scatter(test_case['FMR'],test_case['LMED']) # change question1a to test
        expected_axes1.set_title('Scatterplot of FMR VS LMED')
        expected_axes1.set_xlabel('FMR')
        expected_axes1.set_ylabel('LMED')
        
        return expected_fig
    
    _var="fig"
    _test_cases = [
        (global_df)
        ]

    def check(self, *args):
        print(global_df)
        for df in global_df:# change to enumerate

            source = x.get_source_code("lab3", 9)
            
            lines = source.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('%')]
            updated_source = '\n'.join(filtered_lines)
            
            source_code = "df = " + str(df) + "\n" + updated_source
            
            variables = {}
            exec(source_code, globals(), variables)
            
            actual_fig = variables.get('fig')
            
                        
            expected_fig = Question1B.produce_expected(df)
            
            # for arg in args:
                
                # print("---arg below---")
                # print(arg)
                # print(type(arg))
                # print(arg.axes)
                # print(f"this is get_axes : {arg.get_axes()}")
                # print(f"this is get_axes[0] : {arg.get_axes()[0]}")
                # print(f"this is get_axes[0].get_title() : {arg.get_axes()[0].get_title()}")
                # print(f"this is get_axes[0].get_xlabel() : {arg.get_axes()[0].get_xlabel()}")
                # print(f"this is get_axes[0].get_ylabel() : {arg.get_axes()[0].get_ylabel()}")
                # print(f"this is get_figure : {arg.get_figure()}")
                # print(f"this is get_figwidth : {arg.get_figwidth()}")
                # print(f"this is get_figheight : {arg.get_figheight()}")
                # print(f"this is get_label : {arg.get_label()}")
                # print(f"this is get_sketch_params : {arg.get_sketch_params()}")
                # print(f"this is get_linewidth : {arg.get_linewidth()}")
                # print(f"this is get_children : {arg.get_children()}")
                # print(f"this is get_gid : {arg.get_gid()}")
                # print(f"this is get_dpi : {arg.get_dpi()}")
                # print(f"this is get_tight_layout : {arg.get_tight_layout()}")
                # print(f"this is get_constrained_layout : {arg.get_constrained_layout()}")
                # print(f"this is get_frameon : {arg.get_frameon()}")
                # print(f"this is get_snap : {arg.get_snap()}")
                # print(f"this is get_facecolor : {arg.get_facecolor()}")
                # print(f"this is get_edgecolor : {arg.get_edgecolor()}")
                # print(f"this is get_alpha : {arg.get_alpha()}")
                # print("-----------expected----------")
                # print(expected_fig)
                # print(type(expected_fig))
                # print(expected_fig.axes)
                # print(f"this is get_axes : {expected_fig.get_axes()}")
                # print(f"this is get_axes[0] : {expected_fig.get_axes()[0]}")
                # print(f"this is get_axes[0].get_title() : {expected_fig.get_axes()[0].get_title()}")
                # print(f"this is get_axes[0].get_xlabel() : {expected_fig.get_axes()[0].get_xlabel()}")
                # print(f"this is get_axes[0].get_ylabel() : {expected_fig.get_axes()[0].get_ylabel()}")
                # print(f"this is get_figwidth : {expected_fig.get_figwidth()}")
                # print(f"this is get_figheight : {expected_fig.get_figheight()}")
                # print(f"this is get_label : {expected_fig.get_label()}")
                # print(f"this is get_sketch_params : {expected_fig.get_sketch_params()}")
                # print(f"this is get_linewidth : {expected_fig.get_linewidth()}")
                # print(f"this is get_children : {expected_fig.get_children()}")
                # print(f"this is get_gid : {expected_fig.get_gid()}")
                # print(f"this is get_dpi : {expected_fig.get_dpi()}")
                # print(f"this is get_tight_layout : {expected_fig.get_tight_layout()}")
                # print(f"this is get_constrained_layout : {expected_fig.get_constrained_layout()}")
                # print(f"this is get_frameon : {expected_fig.get_frameon()}")
                # print(f"this is get_snap : {expected_fig.get_snap()}")
                # print(f"this is get_facecolor : {expected_fig.get_facecolor()}")
                # print(f"this is get_edgecolor : {expected_fig.get_edgecolor()}")
                # print(f"this is get_alpha : {expected_fig.get_alpha()}")

            # gettting the x and y data from the actual and expected figure
            actual_x_data, actual_y_data = x.get_x_y_data_from_plt(actual_fig)
            expected_x_data, expected_y_data = x.get_x_y_data_from_plt(expected_fig)
    
            # for a,b in zip(actual_x_data, expected_x_data):
            #     assert a == b, "The x data is not the same. Expected `{}` but got `{}`.".format(b, a)
            # for a,b in zip(actual_y_data, expected_y_data):
            #     assert a == b, "The y data is not the same. Expected `{}` but got `{}`.".format(b, a)
            
            # Compare x data
            assert all(a == b for a, b in zip(actual_x_data, expected_x_data)), "The X data is incorrect."

            # Compare y data
            assert all(a == b for a, b in zip(actual_y_data, expected_y_data)), "The Y data is incorrect."

            # grading the figure - axes, title, xlabel, ylabel
            x.grading_plt_figure(actual_fig, expected_fig)
        
        
        
    def solution_plot(self):
        # self._view.solution() # this will show the solution code, uncomment when solution is ready
        plt.ioff()
        plt.close('all')
        expected_fig = plt.figure()
        expected_axes1 = expected_fig.add_subplot(1,1,1)
        # scatterplot
        expected_axes1.scatter(global_df[0]['FMR'],global_df[0]['LMED'])
        expected_axes1.set_title('Scatterplot of FMR VS LMED')
        expected_axes1.set_xlabel('FMR')
        expected_axes1.set_ylabel('LMED')
        plt.show()
    

Question1 = MultipartProblem(
    Question1A,
    Question1B,
)   