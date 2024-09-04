from learntools.core import *
from ...dev import x
from datetime import datetime

class Question3A(FunctionProblem):
    _var="BookingException"
    _test_cases = [
        ()
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        test = fn.__bases__.__str__()
        if 'Exception' in test:
            x.justpass()
        else: 
            assert test == 'Exception', (f"""The parent class of {fn.__name__} should be an Exception""")

    def check(self, fn):
        self.check_testbook(fn)       

class Question3B (FunctionProblem):
    _var= 'question3b'
    today = datetime.now()
    _test_cases = [
        (['PP1', 'John', 1960], ['PP2', 'Jane', 2000], ['SQ1', 'LA', 2000, datetime(2024, 12, 25, 4, 15)], ['SQ52', 'KL', 1000, datetime(2022, 4, 3, 12, 35)], ['SQ99', 'NY', 2500, datetime(2024, 6, 15, 20, 10)], 'Singapore Airline', 'SUSS', ['name', 'ppNo', 'yearBorn'], ['departureDate', 'destination', 'fare', 'flightNo'], ['_discount', 'bookingDate', 'bookingId', 'flight', 'getNextBookingId', 'passenger', 'ticketPrice'], ['_bookings', '_name', 'addBooking', 'changeBooking', 'deleteBooking', 'searchBooking'], f"""Singapore Airline
No bookings yet
Singapore Airline
Booking id: 1 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $1600.0
Passport No: PP1 Name: John Year Born:1960
Flight: SQ1 Destination: LA Departure Date: 25/12/2024 04:15 Fare: $2000.00
Duplicate booking error
Singapore Airline
Booking id: 1 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $2000.0
Passport No: PP1 Name: John Year Born:1960
Flight: SQ99 Destination: NY Departure Date: 15/06/2024 20:10 Fare: $2500.00
Cannot change flight to a flight with departure date earlier than the booking date
Booking id: 1 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $2000.0
Passport No: PP1 Name: John Year Born:1960
Flight: SQ99 Destination: NY Departure Date: 15/06/2024 20:10 Fare: $2500.00
None
Cannot book a past flight!
Singapore Airline
No bookings yet
Non existing booking error\n""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:           
            out, actual = x.compare_printout(fn)                       
            Flight = x.get_object_from_lab("lab4", 39, "Flight")
            Passenger = x.get_object_from_lab("lab4", 39, "Passenger")
            # creating passengers 1 and 2
            pp1 = Passenger(*test[0])
            pp2 = Passenger(*test[1])
            # creating flights 1, 2 ,3
            fl1 = Flight(*test[2])
            fl2 = Flight(*test[3])
            fl3 = Flight(*test[4])

            # TODO: may need to use multinamespace like lab3q6
            ib = x.get_object_from_lab("lab4", 39, "IndividualBooking")
            cb = x.get_object_from_lab("lab4", 39, "CorporateBooking")
            
            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx < 2:
                        test_list = test[7]
                    elif 1 < idx < 5:
                        test_list = test[8]
                    elif idx == 5:
                        test_list = test[9]
                    elif idx == 6:
                        test_list = test[10]

                    for item in test_list:
                        if item in dir(obj):
                            x.justpass()
                        else:
                            x.justfail((item, obj.__class__.__name__))
                        
            # creating booking
            b1 = ib(pp1, fl3)

            # getting Airline from source code
            al = x.get_object_from_lab("lab4", 39, "Airline")

            # creating airline
            airline = al(test[5])

            # asserting p1
            x.determine_the_grading_method(("question3b()", pp1.__str__(), actual[0].__str__))
            # asserting p2
            x.determine_the_grading_method(("question3b()", pp2.__str__(), actual[1].__str__))
            # asserting f1
            x.determine_the_grading_method(("question3b()", fl1.__str__(), actual[2].__str__))
            # asserting f2
            x.determine_the_grading_method(("question3b()", fl2.__str__(), actual[3].__str__))
            # asserting f3
            x.determine_the_grading_method(("question3b()", fl3.__str__(), actual[4].__str__))
            # asserting b1
            x.determine_the_grading_method(("question3b()", b1.__str__(), actual[5].__str__))
            # asserting airline
            x.determine_the_grading_method(("question3b()", airline.__str__(), actual[6].__str__))

            # Test below is to assert the whole printout to check the method and exception messages
            x.determine_the_grading_method(("question3b()", test[11], out))

            x.grading_check_setter("`fl1.flightNo = 'MY2'`", 'MY2', fl1, "flightNo", fl1._flightNo, "@flightNo.setter")
            x.grading_check_setter("`fl1.departureDate = datetime(2023, 5, 13, 10, 35)`", datetime(2023, 5, 13, 10, 35), fl1, "departureDate", fl1._departureDate, "@departureDate.setter")
            
            #TODO: not adding the `check_setter` for booking's flight.setter. AttributeError will be raised when flight.setter is not defined at `out, actual = x.compare_printout(fn)`
            # x.grading_check_setter("`b1.flight = Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15))`", Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15)), b1, "flight", b1._flight, "@flight.setter")



    def check(self, fn):
        self.check_testbook(fn)

Question3 = MultipartProblem(
    Question3A,
    Question3B

)   