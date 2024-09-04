from learntools.core import *
from ...dev import x
from datetime import datetime

class Question3(FunctionProblem):
    _var="question3"
    _test_cases = [
               (['SQ1', 'LA', datetime(2022, 12, 25, 4, 15)], ['SQ52', 'KL', datetime(2022, 4, 3, 12, 35)], ['SQ99', 'NY', datetime(2022, 6, 15, 15, 20)], ['PP1', 'John'], ['PP2', 'Jane'], ['PP3', 'Mary'], 'Singapore Airline', ['flightNo', 'destination', 'departureDate'], ['ppNo', 'name'], ['bookingId', 'flight', 'passenger'], ['addBooking', 'changeBooking', 'deleteBooking', 'searchBooking'],  """1
2
3
Booking id: 1
Passport No: PP1 Name: John
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15
None
Singapore Airline
Booking id: 2
Passport No: PP2 Name: Jane
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15
Booking id: 3
Passport No: PP3 Name: Mary
Flight: SQ99
Destination: NY
Departure Date: 15/06/2022 15:20\n""")
          
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            out, actual = x.compare_printout(fn)

            # get Flight class
            Flight = x.get_object_from_lab("lab2", 16, "Flight")
            # get Passenger class
            Passenger = x.get_object_from_lab("lab2", 16, "Passenger")
            # get Booking class
            Booking = x.get_object_from_lab("lab2", 21, "Booking")
            # get Airline class
            Airline = x.get_object_from_lab("lab2", 21, "Airline")

            # create Flight objects
            f1 = Flight(*test[0])
            f2 = Flight(*test[1])
            f3 = Flight(*test[2])
            # create Passenger objects
            pp1 = Passenger(*test[3])
            pp2 = Passenger(*test[4])
            pp3 = Passenger(*test[5])
            # create Booking objects
            b1 = Booking(pp1, f1)
            b2 = Booking(pp2, f2)
            b3 = Booking(pp3, f3)

            # create Airline object
            airline = Airline(test[6])

            airline.addBooking(b1)
            airline.addBooking(b2)
            airline.addBooking(b3)

            airline.changeBooking(2, f1)
            airline.deleteBooking(1)

            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx < 3:
                        test_list = test[7]
                    elif 2 < idx < 6 :
                        test_list = test[8]
                    elif 5 < idx < 9:
                        test_list = test[9]
                    else:
                        test_list = test[10]

                for item in test_list:
                    if item in dir(obj):
                        x.justpass()
                    else:
                        x.justfail((item, obj.__class__.__name__))

                # Test below is to assert f1 string
                x.determine_the_grading_method(("question3()", f1.__str__(), actual[0].__str__))
                # test below is to assert f2 string
                x.determine_the_grading_method(("question3()", f2.__str__(), actual[1].__str__))
                # Test below is to assert f3
                x.determine_the_grading_method(("question3()", f3.__str__(), actual[2].__str__))
                # Test below is to assert p1
                x.determine_the_grading_method(("question3()", pp1.__str__(), actual[3].__str__))
                # Test below is to assert p2
                x.determine_the_grading_method(("question3()", pp2.__str__(), actual[4].__str__))
                # Test below is to assert p3
                x.determine_the_grading_method(("question3()", pp3.__str__(), actual[5].__str__))
                # Test below is to assert b1
                x.determine_the_grading_method(("question3()", b1.__str__(), actual[6].__str__))
                # Test below is to assert b2
                x.determine_the_grading_method(("question3()", b2.__str__(), actual[7].__str__))
                # Test below is to assert b3
                x.determine_the_grading_method(("question3()", b3.__str__(), actual[8].__str__))
                # Test below is to assert airline
                x.determine_the_grading_method(("question3()", airline.__str__(), actual[9].__str__))


                # Test below is to assert the whole printout
                x.determine_the_grading_method(("question3()", test[11], out))

            #TODO: not adding the `check_setter` for booking's flight.setter. AttributeError will be raised when flight.setter is not defined at `out, actual = x.compare_printout(fn)`
            # x.grading_check_setter("`b1.flight = Flight('MY2', 'NY', datetime(2022, 10, 21, 2, 15))`", Flight('MY2', 'NY', datetime(2022, 10, 21, 2, 15)), b1, "flight", b1._flight, "@flight.setter")

    def check(self, fn):
        self.check_testbook(fn)   