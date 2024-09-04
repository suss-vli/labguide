from learntools.core import *
from ...dev import x
import matplotlib.pyplot as plt

class Question1A(CodingProblem):

    def produce_expected():
        from sklearn.datasets import fetch_california_housing
        housedata = fetch_california_housing(as_frame=True)
        df1 = housedata.data

        return df1

    _var = "df1"
    _expected = produce_expected()

    _test_cases = [
        ("a", "d", ['d', 'b', 'c', 0, 1, 2, 3]),
        (2, 4, ['a', 'b', 'c', 0, 1, 4, 3])
    ]

    def check(self, *args):

        #checking for the correct library imported/used
        source = x.get_source_code("lab2a", 31)
        
        if "sklearn.datasets" and "fetch_california_housing" in source:
            x.justpass()
        elif "sklearn.datasets" not in source:
            x.justfail("sklearn.datasets", "Please use the correct library: `sklearn.datasets`.")
        elif "fetch_california_housing" not in source:
            x.justfail("fetch_california_housing", "Please use the correct library: `fetch_california_housing`.")

        lines = source.split('\n')
        filtered_lines = [line for line in lines if not line.lstrip().endswith('info()')]
        filtered_lines = [line for line in filtered_lines if not line.lstrip().startswith('print')]
        updated_source = '\n'.join(filtered_lines)       
        
        variables = {}
        exec(updated_source, globals(), variables)
        
        df_actual =  variables.get('df1')      
        expected_df = Question1A.produce_expected()

        x.grading_df_series(("df1", expected_df, df_actual))
        x.determine_the_grading_method(("df1.info()", expected_df.info(), df_actual.info()))

class Question1B(EqualityCheckProblem):

    def produce_expected():
        plt.ioff()
        df1 = Question1A.produce_expected()
        expected_fig, expected_ax1 = plt.subplots()
        expected_ax1.hist(df1['MedInc'], color = 'aqua', ec = 'black');
        expected_ax1.set_ylabel("Medium Income in California")
        plt.close('all')

        return expected_fig

    _vars = ['fig', 'ax1']
    # _expected = ['<Figure size 640x480 with 1 Axes>', '<Axes: ylabel='Medium Income in California'>']
    _test_cases = [
        ('HouseAge'),
        ('AveRooms')]

    def check(self, *args):
        # print("args", args)
        # print(type(args))
        # print(Question1B.produce_expected())
        # print(Question1B.produce_expected().axes[0])
        # super().check(*args)

        for test in self._test_cases:
            # super().check(*args)
            plt.ioff()
            
            source = x.get_source_code("lab2a", 31) + "\n" + "plt.ioff()" + "\n" + x.get_source_code("lab2a", 34)
            
            # # update datafile
            # new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test
            # update_df = x.update_csv_in_code(previous, new_csv, "df") # need to specify df in the question

            # lines = update_df.split('\n')
            # filtered_lines = [line for line in lines if not line.lstrip().startswith('%')]
            # filtered_lines = [line for line in filtered_lines if not line.lstrip().startswith('print')]
            # updated_source = '\n'.join(filtered_lines)        
            
            # print(source)

            variables = {}
            exec(source, globals(), variables)            

            actual_fig = variables.get('fig')
            expected_fig = Question1B.produce_expected()

            # # Access color, edge color, and label of each patch
            # for i, patch in enumerate(patches):
            #     # Access the height (count) of the bar
            #     count = patch.get_height()

            #     # Access color, edge color, and label of the patch
            #     color_used = patch.get_facecolor()
            #     edge_color_used = patch.get_edgecolor()
            #     label_used = patch.get_label()

            #     print(f"Bar {i + 1}:")
            #     print("  Count:", count)
            #     print("  Color Used:", color_used)
            #     print("  Edge Color Used:", edge_color_used)
            #     print("  Label Used:", label_used)
                
            # # Access the patches of the expected figure
            # print("--------expected--------")
            # expected_patches = expected_fig.axes[0].patches

            # # Access color, edge color, and label of each patch
            # for i, patch in enumerate(expected_patches):
            #     # Access the height (count) of the bar
            #     count = patch.get_height()

            #     # Access color, edge color, and label of the patch
            #     color_used = patch.get_facecolor()
            #     edge_color_used = patch.get_edgecolor()
            #     label_used = patch.get_label()

            #     print(f"Bar {i + 1}:")
            #     print("  Count:", count)
            #     print("  Color Used:", color_used)
            #     print("  Edge Color Used:", edge_color_used)
            #     print("  Label Used:", label_used)

            # Access the patches of the actual figure
            actual_patches = actual_fig.axes[0].patches

            # Access the patches of the expected figure
            expected_patches = expected_fig.axes[0].patches

            # Ensure the number of patches is the same for both figures
            assert len(actual_patches) == len(expected_patches), ("""
The number of bars is incorrect. Expected the number of bars to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(len(expected_patches)), str(len(actual_patches)), x.get_edits_string(str(len(expected_patches)), str(len(actual_patches))))
            
            
            # Compare attributes for each patch/bar
            for i, (actual_patch, expected_patch) in enumerate(zip(actual_patches, expected_patches)):
                # Access the height (count) of the bar
                assert actual_patch.get_height() == expected_patch.get_height(), ("""
The data is incorrect. Expected the data of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_height()), str(actual_patch.get_height()), x.get_edits_string(str(expected_patch.get_height()), str(actual_patch.get_height())))

                # Access color, edge color, and label of the patch
                assert actual_patch.get_facecolor() == expected_patch.get_facecolor(), ("""
Expected the face color of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_facecolor()), str(actual_patch.get_facecolor()), x.get_edits_string(str(expected_patch.get_facecolor()), str(actual_patch.get_facecolor())))

                assert actual_patch.get_edgecolor() == expected_patch.get_edgecolor(), ("""
Expected the edge color of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_edgecolor()), str(actual_patch.get_edgecolor()), x.get_edits_string(str(expected_patch.get_edgecolor()), str(actual_patch.get_edgecolor())))

                assert actual_patch.get_label() == expected_patch.get_label(), ("""
Expected the label of `Bar {}` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(i), str(expected_patch.get_label()), str(actual_patch.get_label()), x.get_edits_string(str(expected_patch.get_label()), str(actual_patch.get_label())))

            
             # check y label - this is checked in grading_plt_figure < but this function is specific to scatterplot
            actual_ylabel = actual_fig.axes[0].get_ylabel()
            expected_ylabel = expected_fig.axes[0].get_ylabel()

            assert actual_ylabel == expected_ylabel, ("""
The y-axis title is incorrect. Expected the y-axis title to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_ylabel), str(actual_ylabel), x.get_edits_string(str(expected_ylabel), str(actual_ylabel)))

                
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


Question1 = MultipartProblem(
    Question1A,
    Question1B
)    