from ...dev import x
import sys
from learntools.core import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

   
            
class Question2(FunctionProblem):


    _var="Subscription"

    _test_cases = [
        ('3G', 'post-paid', '01', '2016', 'Result of calculate_total query: 1124100\n'),
        ('4G', 'post-paid', '01', '2016', 'Result of calculate_total query: 3690100\n'),
        ( '4G', 'post-paid', '01', '2015', 'Result of calculate_total query: 2991300\n')
    ]

    def check(self, fn):
        for test in self._test_cases:

            #checking for the correct library imported/used
            source = x.get_source_code("lab2", 11)
            
            if "sqlalchemy" in source and "sqlite3" not in source:
                x.justpass()
            else:
                x.justfail("sqlachemy", "Please use the correct library: `sqlalchemy` for all parts of this question.")
                
            # checking subscription(base) < parent class
            check_parent_class = fn.__bases__.__str__()
            if 'sqlalchemy.orm.decl_api.Base' in check_parent_class:
                x.justpass()
            else: 
                assert check_parent_class == 'sqlalchemy.orm.decl_api.Base', (f"""The parent class of {fn.__name__} should be a `Base` class from `sqlalchemy`.""")
            
            # testing subscription
            engine = create_engine('sqlite:///seminar2_activity2.db', echo= False)
            Session = sessionmaker(bind=engine)
            session = Session()

            # testing chatgpt

            # Capture the print output
            output_buffer = x.capture_print_output()

            # Call the method that produces print statements
            fn().calculate_total(session, test[0], test[1], test[2], test[3])

            # Restore sys.stdout to its original value
            sys.stdout = sys.__stdout__

            # Retrieve the captured content
            captured_output = output_buffer.getvalue()

            x.determine_the_grading_method((f"Subscription.calculate_total(session, {test[0]}, {test[1]}, {test[2]}, {test[3]})", test[4], captured_output))


