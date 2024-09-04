import re
import requests
from ...dev import x
from learntools.core import *
# from learntools.vli.asserts_vli impoport assert_file_exist_vli
import sqlite3
import os

# Todo
# check the prescence of seminar2_activity2.db - done
# check the presence of csv - done
# check the validity of seminar2_activity2.db by calling it and running some function through it - done
# check the validity of csv by looping through it 

# checking easy_way function as functionalCheck

class Question1(EqualityCheckProblem):

    _test_cases = [
        ('seminar2_activity2.db', 'ICT233_total-number-of-mobile-subscriptions-by-type.csv', 292600, "test_total-number-of-mobile-subscriptions-by-type.csv", ['month', 'network_access_technology', 'type_of_plan', 'number_of_subscriptions']
)
    ]

    def check(self):
        for test in self._test_cases:
            assert_file_exists(test[0]) # specify name for the db in question
            assert_file_exists(test[1]) # specify the name of the csv in question

            #checking for the correct library imported/used
            source = x.get_source_code("lab2", 4)
            
            if "sqlite3" in source:
                x.justpass()
            else:
                x.justfail("sqlite3", "sqlite3 is not imported. Please use the correct library.")


            #testing if we can connect to the db:
            conn = sqlite3.connect('seminar2_activity2.db')
            # print("connected to db")
            cur = conn.cursor()
            cur.execute('SELECT SUM(num_of_subs) from total_subscriptions WHERE access_tech = ? AND month = ?', ('2G', '2015-01'))
            result = cur.fetchone()[0]
            x.determine_the_grading_method(("", result, test[2]))
            conn.close()
            # print("db closed")

            expected_file = os.path.dirname(os.path.abspath(__file__)) + "/" + test[3]
            x.grading_csv(test[1], test[1], expected_file, test[4]) #incorrect statement is lacking a little due to if content is different inside the files, it will appear as list and not show which row or cell is incorrect in the csv
            