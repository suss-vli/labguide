from learntools.core import *
import re
from urllib.request import Request, urlopen
from ...dev import x

class Question1(EqualityCheckProblem):

    def produce_expected():
        x.is_internet_down()
        req = Request('https://www.py4e.com/code3/mbox-short.txt', headers={'User-Agent': 'Mozilla/5.0'})
        file = urlopen(req)

        counter_answer = 0

        for line in file:
            decoded = line.decode().strip()
            counter_answer += re.subn('uct.ac.za', '', decoded)[1]
        
        return counter_answer

    _var = "counter"
    _expected = produce_expected()

    # print(f"_var: {_var}")
   
    _test_cases = [
        ('https://gist.githubusercontent.com/ytbryan/d2a7b366012092a00fad369b281d2673/raw/228ceec21c8d309736341d7bc83e4ccfc3cbd842/gistfile1.txt', 150),
        ('https://gist.githubusercontent.com/ytbryan/2020326e8961bcb9af1db8d721bb1575/raw/2535d9fdc5faff50aa90e79dfe723c642789b188/d',75)]

    def check(self, *args):
        # first check for default
        # print("check is called")
        # assert 1==0
        # print(self._var)

        # print(f"_var: {self._var}")
        # print(f"_expected: {self._expected}")

        super().check(*args)

        for test in self._test_cases:
            source = x.get_source_code("lab1", 4)
            x.test_for_none_233(source, "lab1", 4, test[0], "req")
            test_source = x.update_url_in_code(source, test[0], "req")

            # Create a dictionary to capture the local variables and assessment results
            local_vars = {}
            
            # Execute the code in test_source within the local_vars context
            try:
                exec(test_source, None, local_vars)
            except Exception as e:
                print(f"Error executing code: {e}")
                raise e
    
            executed_counter = local_vars.get('counter')
            x.determine_the_grading_method((test[0], test[1], executed_counter))
    
