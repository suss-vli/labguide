from learntools.core import *
from ...dev import x
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib import collections as mc # NEW

class Question2(EqualityCheckProblem):

    def produce_expected(dataset):
        plt.ioff()
        from sklearn.datasets import fetch_california_housing
        housedata = fetch_california_housing(as_frame=True)
        df1 = housedata.data
        sns.kdeplot(df1[f"{dataset}"], color = "cyan",  fill = True)
        sns.despine()
        plt.title(f"{dataset} Distribution in California")
        fig1 = plt.gcf()
        ax1 = plt.gca()
        
        plt.close('all')

        # return fig1
        return fig1, ax1

    # _vars = ['fig', 'ax1']
    # _expected = ['<Figure size 640x480 with 1 Axes>', '<Axes: ylabel='Medium Income in California'>']
    _test_cases = [
        ('HouseAge'),
        ('AveRooms')]

    def check(self, *args):
        # actual testing
        plt.ioff()

        source = x.get_source_code("lab2a", 31) + "\n" + x.get_source_code("lab2a", 59) + "\n" + "fig1 = plt.gcf()" + "\n" + "ax1 = plt.gca()"

        # assert seaborn used
        if "sns.kdeplot" in source:
            x.justpass()
        else:
            x.justfail("sns.kdeplot", "`sns.kdeplot` is not used. Please use `sns.kdeplot` to construct a kernel density plot.")

        variables = {}
        exec(source, globals(), variables)
        
        # Check actual fill color
        actual_ax = variables.get('ax1')
        plt.figure()
        expected_fig, expected_ax = Question2.produce_expected("Population")
        x.grading_anl588_seaborn_kdeplot((actual_ax, expected_ax))
            
            # testing test cases
        for test in self._test_cases:

            x.test_for_none_588(source, "lab2a", 31, "Population", test, "Population")
            updated_source = x.update_x_in_code(source, "Population", test)
            variables = {}
            exec(updated_source, globals(), variables)
            actual_ax = variables.get('ax1')
            plt.figure()
            expected_fig, expected_ax = Question2.produce_expected(test)
            x.grading_anl588_seaborn_kdeplot((actual_ax, expected_ax))

    #TODO: do we want to display the plot in the solution?
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
        


