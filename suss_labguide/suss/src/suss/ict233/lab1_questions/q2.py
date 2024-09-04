from learntools.core import *
import requests
import re
import os
import csv
from ...dev import x

class Question2(EqualityCheckProblem):

    def produce_expected():
        url = 'https://api.data.gov.sg/v1/environment/24-hour-weather-forecast'
        params = dict(
            date='2023-02-04',
        )
        data_answer = requests.get(url, params=params).json()

        return data_answer

    _var="data"
    _expected = produce_expected()


    _test_cases = [
        ('2023-02-02', 'forecast.csv', ['start', 'end', 'west', 'east', 'central', 'south', 'north'], 'forecast_2023-02-02.csv', 'https://gist.githubusercontent.com/ytbryan/045a6558d6dcd90c1aa28a2392d10edf/raw/e0e7cc61110da58df7451c0d3c7e900f874b4dd0/gistfile1.txt', 'forecast_gist.csv', {'items': [{'update_timestamp': '2023-09-12T13:51:18+08:00', 'timestamp': '2023-09-12T13:34:00+08:00', 'valid_period': {'start': '2023-09-12T12:00:00+08:00', 'end': '2023-09-13T12:00:00+08:00'}, 'general': {'forecast': 'Thundery Showers', 'relative_humidity': {'low': 60, 'high': 95}, 'temperature': {'low': 25, 'high': 33}, 'wind': {'speed': {'low': 15, 'high': 30}, 'direction': 'SSE'}}, 'periods': [{'time': {'start': '2023-09-12T12:00:00+08:00', 'end': '2023-09-12T18:00:00+08:00'}, 'regions': {'west': 'Cloudy', 'east': 'Thundery Showers', 'central': 'Thundery Showers', 'south': 'Cloudy', 'north': 'Thundery Showers'}}, {'time': {'start': '2023-09-12T18:00:00+08:00', 'end': '2023-09-13T06:00:00+08:00'}, 'regions': {'west': 'Partly Cloudy (Night)', 'east': 'Partly Cloudy (Night)', 'central': 'Partly Cloudy (Night)', 'south': 'Partly Cloudy (Night)', 'north': 'Partly Cloudy (Night)'}}, {'time': {'start': '2023-09-13T06:00:00+08:00', 'end': '2023-09-13T12:00:00+08:00'}, 'regions': {'west': 'Partly Cloudy (Day)', 'east': 'Partly Cloudy (Day)', 'central': 'Partly Cloudy (Day)', 'south': 'Partly Cloudy (Day)', 'north': 'Partly Cloudy (Day)'}}]}], 'api_info': {'status': 'unhealthy'}})
    ]

    def check(self, *args):

        super().check(*args)

        for test in self._test_cases:
            source = x.get_source_code("lab1", 8)
            x.test_for_none_233(source, "lab1", 8, test[4], "url")
            test_source = x.update_url_in_code(source, test[4], "url", None)

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(test_source, None, local_vars)

            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_data = local_vars.get('data')

            x.determine_the_grading_method((test[0], test[6], executed_data))

            path = self._test_cases[0][1]
            assert_file_exists(path)

            full_path = os.path.abspath(path)
            expected_path = os.path.dirname(os.path.abspath(__file__)) + "/" + 'forecast_2023-02-04.csv'

            x.grading_csv(path, full_path,expected_path, self._test_cases[0][2])

            for test in self._test_cases:
                # testing test case for replacing of `param`
                source = x.get_source_code("lab1", 8)
                x.test_for_none_233(source, "lab1", 8, test[0], "date")
                expected_path = os.path.dirname(os.path.abspath(__file__)) + "/" + test[3]
                updated_source = x.update_date_in_code(source, test[0])

                cell_numbers = [12,13]
                previous = ""
                # loop throu array and get_source_code
                for item in cell_numbers: 
                    current = x.get_source_code("lab1", item)
                    previous = previous + "\n" + current
                
                combined_source = updated_source + "\n" + previous

                lines = combined_source.split('\n')
                filtered_lines = [line for line in lines if not line.lstrip().startswith('print')]
                updated_source = '\n'.join(filtered_lines) 
                
                #generate forecast.csv for test case
                exec(updated_source)
                # checking the csv
                x.grading_csv(test[1], path, expected_path, test[2])

                # testing test case for replace `url`
                source = x.get_source_code("lab1", 8)
                x.test_for_none_233(source, "lab1", 8, test[4], "url")
                expected_path = os.path.dirname(os.path.abspath(__file__)) + "/" + test[5]
                updated_source = x.update_url_in_code(source, test[4], "url", None) # test[4]

                cell_numbers = [12,13]
                previous = ""
                # loop throu array and get_source_code
                for item in cell_numbers: 
                    current = x.get_source_code("lab1", item)
                    previous = previous + "\n" + current

                combined_source = updated_source + "\n" + previous
                
                lines = combined_source.split('\n')
                filtered_lines = [line for line in lines if not line.lstrip().startswith('print')]
                updated_source = '\n'.join(filtered_lines) 
                
                #generate forecast.csv for test case
                exec(updated_source)
                # checking the csv
                x.grading_csv(test[1], path, expected_path, test[2])
