from learntools.core import *
from ...dev import x
from datetime import datetime

class Question1A(FunctionProblem):
    _var="Passenger"
    _test_cases = [
            (['flight', 'getDepartureDate', 'name', 'ppNo'], 'S1112', 'John', 'S1112', datetime(2011, 12, 25, 4, 15), ['SQ1', 'LA', datetime(2011, 12, 25, 4, 15)], """Passport No: S1112 Name: John Flight: SQ1 Destination: LA Departure Date: 25/12/2011 04:15 """),
            (['flight', 'getDepartureDate', 'name', 'ppNo'], 'S01234', 'Jane', 'S01234', datetime(2011, 12, 26, 3, 45), ['SQ1', 'LA', datetime(2011, 12, 26, 3, 45)], """Passport No: S01234 Name: Jane Flight: SQ1 Destination: LA Departure Date: 26/12/2011 03:45 """)
        ]

    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            Flight = x.get_object_from_lab("lab2", 4, "Flight")
            f1 = Flight(*test[5])
            p1 = fn(test[1], test[2], f1)
            
            answer = dir(fn)
            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                    
                if item == "ppNo":
                    if isinstance(fn.ppNo, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`ppNo` should be a property.")
                elif item == "flight":
                    if isinstance(fn.flight, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`flight` should be a property.")
                elif item == "name":
                    if isinstance(fn.name, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`name` should be a property.")

            
            x.determine_the_grading_method(((test[1], test[2], f1), test[4], p1.getDepartureDate))
            x.determine_the_grading_method(((test[1], test[2], f1), test[4], p1.flight.departureDate))
            x.determine_the_grading_method(((test[1], test[2], f1), test[6], p1.__str__))
            
            x.grading_check_setter("`p1.flight = Flight('SQ2', 'NY', datetime(2022, 10, 21, 2, 15))`", Flight('SQ2', 'NY', datetime(2022, 10, 21, 2, 15)), p1, "flight", p1._flight, "@flight.setter")

    def check(self, fn):
        self.check_testbook(fn)

class Question1B(FunctionProblem):
    _var="question1b"
    _test_cases = [
            ("""2021-12-25 04:15:00
Passport No: PP1 Name: John Flight: SQ1 Destination: LA Departure Date: 25/12/2021 04:15 
Passport No: PP2 Name: Jane Flight: SQ1 Destination: LA Departure Date: 25/12/2021 04:15 
Passport No: PP1 Name: John Flight: SQ1 Destination: LA Departure Date: 26/12/2021 15:25 
Passport No: PP2 Name: Jane Flight: SQ1 Destination: LA Departure Date: 26/12/2021 15:25 \n""", ['SQ1', 'LA', datetime(2021, 12, 26, 15, 25)], ['PP1', 'John'], ['PP2', 'Jane'], ['flightNo', 'destination', 'departureDate'], ['ppNo', 'name', 'flight', 'getDepartureDate'])
        ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:           
            actual = fn()
            Flight = x.get_object_from_lab("lab2", 4, "Flight")
            Passenger = x.get_object_from_lab("lab2", 7, "Passenger")
            
            fl1 = Flight(*test[1])
            pp1 = Passenger(*test[2], fl1)
            pp2 = Passenger(*test[3], fl1)

            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx == 0:
                        test_list = test[4]
                    elif idx == 1:
                        test_list = test[5]
                    elif idx == 2:
                        test_list = test[5]

                for item in test_list:
                    if item in dir(obj):
                        x.justpass()
                    else:
                        x.justfail((item, obj.__class__.__name__))

            # Test below is to assert f1
            x.determine_the_grading_method(("question1b()", fl1.__str__(), actual[0].__str__))
            # Test below is to assert p1
            x.determine_the_grading_method(("question1b()", pp1.__str__(), actual[1].__str__))
            # Test below is to assert p2
            x.determine_the_grading_method(("question1b()", pp2.__str__(), actual[2].__str__))

            # Test below is to assert the whole printout
            out, atl = x.compare_printout(fn)
            x.determine_the_grading_method(("question1b()", test[0], out))

    def check(self, fn):
        self.check_testbook(fn)

Question1 = MultipartProblem(
    Question1A,
    Question1B,
)    
