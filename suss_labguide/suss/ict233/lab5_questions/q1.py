import re
import requests
from ...dev import x
from learntools.core import *
import os
import pandas as pd

    
class Question1A(CodingProblem):

    # def produce_expected():
    #     expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + 'test_phone_data.csv'
    #     phone_data =pd.read_csv(expected_file)

    #     expected_df = phone_data.groupby(['network','item']).agg({
    # 'duration':['sum',min,max, 'describe']}).reset_index()
        
    #     return expected_df

    _test_cases = [
        ("""      network  item  duration                                           \\
                          sum      min        max describe               
                     duration duration   duration    count        mean   
0      Meteor  call   7200.00    1.000   1090.000     54.0  133.333333   
1      Meteor   sms     33.00    1.000      1.000     33.0    1.000000   
2       Tesco  call  13828.00    3.000   1234.000     71.0  194.760563   
3       Tesco   sms     13.00    1.000      1.000     13.0    1.000000   
4       Three  call  36464.00    2.000   2328.000    128.0  284.875000   
5       Three   sms     87.00    1.000      1.000     87.0    1.000000   
6    Vodafone  call  14621.00    2.000   1859.000     66.0  221.530303   
7    Vodafone   sms    149.00    1.000      1.000    149.0    1.000000   
8        data  data   5164.35   34.429     34.429    150.0   34.429000   
9    landline  call  18433.00    3.000  10528.000     42.0  438.880952   
10    special   sms      3.00    1.000      1.000      3.0    1.000000   
11  voicemail  call   1775.00    1.000    174.000     27.0   65.740741   
12      world   sms      7.00    1.000      1.000      7.0    1.000000   

                                                              
                                                              
            std     min     25%      50%      75%        max  
0    199.889403   1.000   8.250   51.500  191.750   1090.000  
1      0.000000   1.000   1.000    1.000    1.000      1.000  
2    235.498527   3.000  33.500  117.000  244.500   1234.000  
3      0.000000   1.000   1.000    1.000    1.000      1.000  
4    442.397833   2.000  10.750   69.500  428.000   2328.000  
5      0.000000   1.000   1.000    1.000    1.000      1.000  
6    379.194580   2.000   7.000   46.500  173.000   1859.000  
7      0.000000   1.000   1.000    1.000    1.000      1.000  
8      0.000000  34.429  34.429   34.429   34.429     34.429  
9   1631.415609   3.000  15.750   75.000  200.750  10528.000  
10     0.000000   1.000   1.000    1.000    1.000      1.000  
11    44.294984   1.000  28.000   63.000   97.000    174.000  
12     0.000000   1.000   1.000    1.000    1.000      1.000  \n""", 'test_phone_data_year_2021.csv', """      network  item duration                                           \\
                         sum      min        max describe               
                    duration duration   duration    count        mean   
0      Meteor  call  14400.0    2.000   2180.000     54.0  266.666667   
1      Meteor   sms     66.0    2.000      2.000     33.0    2.000000   
2       Tesco  call  27656.0    6.000   2468.000     71.0  389.521127   
3       Tesco   sms     26.0    2.000      2.000     13.0    2.000000   
4       Three  call  72928.0    4.000   4656.000    128.0  569.750000   
5       Three   sms    174.0    2.000      2.000     87.0    2.000000   
6    Vodafone  call  29242.0    4.000   3718.000     66.0  443.060606   
7    Vodafone   sms    298.0    2.000      2.000    149.0    2.000000   
8        data  data  10328.7   68.858     68.858    150.0   68.858000   
9    landline  call  36866.0    6.000  21056.000     42.0  877.761905   
10    special   sms      6.0    2.000      2.000      3.0    2.000000   
11  voicemail  call   3550.0    2.000    348.000     27.0  131.481481   
12      world   sms     14.0    2.000      2.000      7.0    2.000000   

                                                              
                                                              
            std     min     25%      50%      75%        max  
0    399.778807   2.000  16.500  103.000  383.500   2180.000  
1      0.000000   2.000   2.000    2.000    2.000      2.000  
2    470.997054   6.000  67.000  234.000  489.000   2468.000  
3      0.000000   2.000   2.000    2.000    2.000      2.000  
4    884.795666   4.000  21.500  139.000  856.000   4656.000  
5      0.000000   2.000   2.000    2.000    2.000      2.000  
6    758.389161   4.000  14.000   93.000  346.000   3718.000  
7      0.000000   2.000   2.000    2.000    2.000      2.000  
8      0.000000  68.858  68.858   68.858   68.858     68.858  
9   3262.831217   6.000  31.500  150.000  401.500  21056.000  
10     0.000000   2.000   2.000    2.000    2.000      2.000  
11    88.589967   2.000  56.000  126.000  194.000    348.000  
12     0.000000   2.000   2.000    2.000    2.000      2.000  \n""")
    ]

    def check(self):
        for test in self._test_cases:
        # expected_df = str(Question1A.produce_expected())
        
            phone_data = x.get_source_code("lab5", 6)
            source = x.get_source_code("lab5", 14)

            combined_source = phone_data + "\n" + source

            # line 98 - 101 : remove comments and pass + fix indentation in source code
            lines = combined_source.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('#')]
            filtered_lines2 = [line for line in filtered_lines if not line.lstrip().startswith('pass')]
            updated_source = '\n'.join(['    ' + line for line in filtered_lines2]) 

            fn_name = "fn"
            fn_source = f"import pandas as pd\ndef fn():\n{updated_source}"
            # Execute the function definition
            exec(fn_source, globals())
            
            # Access the dynamically created function by its name
            fn = globals()[fn_name]
        
            out, actual = x.compare_printout(fn)

            x.determine_the_grading_method(("phone_data.csv", test[0], out))
            
            # for test case
            cell_numbers = [6,14]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab5", item)
                previous = previous + "\n    " + current
            
            # update phone data csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            x.test_for_none_233(previous, "lab5", 6, new_csv, "phone_data")
            updated_source = x.update_csv_in_code(previous, new_csv, "phone_data")

            # line 127 - 130 : remove comments and pass + fix indentation in source code
            lines = updated_source.split('\n')
            filtered_lines = [line for line in lines if not line.lstrip().startswith('#')]
            filtered_lines2 = [line for line in filtered_lines if not line.lstrip().startswith('pass')]
            final_source = '\n'.join(['    ' + line for line in filtered_lines2]) 

            test_fn_name = "test_fn"
            test_fn_source = f"import pandas as pd\ndef test_fn():\n{final_source}"

            # Execute the function definition
            exec(test_fn_source, globals())
            
            # Access the dynamically created function by its name
            test_fn = globals()[test_fn_name]
        
            out_test, actual_test = x.compare_printout(test_fn)
            x.determine_the_grading_method(("phone_data_year_2021.csv", test[2], out_test))
            
class Question1B(CodingProblem):

    def produce_expected_df_inner(self, phone_data_file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + phone_data_file
        phone_data =pd.read_csv(expected_file)

        duration_transform = phone_data.groupby(['network','item']).duration.transform(lambda x: x.mean())
        phone_data["duration_mean"] = duration_transform
        phone_data["duration_differences"] = phone_data["duration"] - phone_data["duration_mean"]
        duration_agg = phone_data.groupby(['network','item']).duration.agg(lambda x: x.mean()).reset_index()
        df_inner = phone_data.merge (duration_agg, on = ['network','item'], how = "inner")
        df_inner["dff_val"] = df_inner.duration_x - df_inner.duration_y
        
        return df_inner
    
    _test_cases = [
        ('test_phone_data.csv', 'test_phone_data_year_2021.csv')
    ]
    
    _var= "df_inner"
    

    def check(self, *args):
        for test in self._test_cases:
            expected = self.produce_expected_df_inner(test[0])
            x.determine_the_grading_method(("df_inner", expected, args[0]))
        
            # test case:
            cell_numbers = [6,18,19,20,21,22,23,24,25,26,27,28]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab5", item)
                previous = previous + "\n" + current
            
            # update phone data csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            updated_source = x.update_csv_in_code(previous, new_csv, "phone_data")
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df_inner =  variables.get('df_inner')
            
            expected_df_inner = self.produce_expected_df_inner(test[1])
            x.determine_the_grading_method(("df_inner", expected_df_inner, actual_df_inner))

class Question1C(CodingProblem):

    def produce_expected_df_right(self, phone_data_file):
        expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + phone_data_file
        phone_data =pd.read_csv(expected_file)

        duration_transform = phone_data.groupby(['network','item']).duration.transform(lambda x: x.mean())
        phone_data["duration_mean"] = duration_transform
        phone_data["duration_differences"] = phone_data["duration"] - phone_data["duration_mean"]
        duration_agg = phone_data.groupby(['network','item']).duration.agg(lambda x: x.mean()).reset_index()
        df_right = duration_agg.merge (phone_data, on = ['network','item'], how = "right")
        df_right["diff"] = df_right.duration_y - df_right.duration_x
        
        return df_right

    _var= "df_right"
    # _expected = produce_expected_df_right()
    
    _test_cases = [
        ('test_phone_data.csv', 'test_phone_data_year_2021.csv')
    ]

    def check(self, *args):
        for test in self._test_cases:
            expected = self.produce_expected_df_right(test[0])
            x.determine_the_grading_method(("df_right", expected, args[0]))
        
            # test case:
            cell_numbers = [6,18,19,20,21,22,23,24,25,26,31,32]
            previous = ""
            for item in cell_numbers: 
                current = x.get_source_code("lab5", item)
                previous = previous + "\n" + current
            
            # update phone data csv
            new_csv = os.path.dirname(os.path.abspath(__file__)) + "/" + test[1]
            updated_source = x.update_csv_in_code(previous, new_csv, "phone_data")
            
            variables = {}
            exec(updated_source, globals(), variables)
            
            actual_df_right =  variables.get('df_right')
            
            expected_df_right = self.produce_expected_df_right(test[1])
            x.determine_the_grading_method(("df_right", expected_df_right, actual_df_right))


Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C,
)   