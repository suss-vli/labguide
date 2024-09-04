from learntools.core import *
from suss.dev import x
from datetime import datetime
  
class Question6(FunctionProblem):
    _var ="question6"
    today = datetime.now()
    _test_cases = [
        (['PP1', 'John', 1962], ['PP2', 'Jane', 2000], ['SQ1', 'LA', 2000, datetime(2022, 12, 25, 4, 15)], ['SQ52', 'KL', 1000, datetime(2022, 4, 3, 12, 35)], 'SUSS', ['name', 'ppNo', 'yearBorn'], ['departureDate', 'destination', 'fare', 'flightNo'], ['_discount', 'bookingDate', 'bookingId', 'flight', 'getNextBookingId', 'passenger', 'ticketPrice'], ['_company', '_discount', 'bookingDate', 'bookingId', 'flight', 'getNextBookingId', 'passenger', 'ticketPrice'], f"""Booking id: 1 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $400.0
Passport No: PP1 Name: John Year Born:1962
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15 Fare: $2000.00
Booking id: 2 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $1000
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00
Company: SUSS Booking id: 3 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $500.0
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00\n""", f"""Booking id: 4 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $400.0
Passport No: PP1 Name: John Year Born:1962
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15 Fare: $2000.00
Booking id: 5 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $1000
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00
Company: SUSS Booking id: 6 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $500.0
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00\n""", f"""Booking id: 4 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $400.0
Passport No: PP1 Name: John Year Born:1962
Flight: SQ1
Destination: LA
Departure Date: 25/12/2022 04:15 Fare: $2000.00""", f"""Booking id: 5 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $1000
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00""", f"""Company: SUSS Booking id: 6 Booking Date: {datetime(today.year, today.month, today.day).strftime("%d %B %Y")}
Ticket Price: $500.0
Passport No: PP2 Name: Jane Year Born:2000
Flight: SQ52
Destination: KL
Departure Date: 03/04/2022 12:35 Fare: $1000.00""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            out, actual = x.compare_printout(fn)
            
            if actual is None:
                x.justfail("None", f"{self._var}() is {actual}. Please attempt the question and run the question again.")
            else:
                for idx, obj in enumerate(actual):
                    if idx < 2:
                        test_list = test[5]
                    elif 1 < idx < 4:
                        test_list = test[6]
                    elif 3 < idx < 6:
                        test_list = test[7]
                    elif idx == 6:
                        test_list = test[8]

                    for item in test_list:
                        if item in dir(obj):
                            x.justpass()
                        else:
                            x.justfail((item, obj.__class__.__name__))

            source_code = x.get_source_code("lab3", 54,"Flight, Passenger, Booking, IndividualBooking, CorporateBooking")
            x.test_for_none_162(source_code, "lab3", "54",  ["Flight", "Passenger", "Booking", "IndividualBooking", "CorporateBooking"])
            data = x.create_many_objects_from_source_code(source_code, ["Flight", "Passenger", "Booking", "IndividualBooking", "CorporateBooking"])
            Flight = data["Flight"]
            Passenger = data["Passenger"]
            
            # creating passengers 1 and 2
            pp1 = Passenger(*test[0])
            pp2 = Passenger(*test[1])
            # creating flights 1 and 2
            fl1 = Flight(*test[2])
            fl2 = Flight(*test[3])


            ib = data["IndividualBooking"]
            cb = data["CorporateBooking"]

            # creating bookings
            b1 = ib(pp1, fl1)
            b2 = ib(pp2, fl2)
            b3 = cb(pp2, fl2, test[4])

            # asserting p1
            x.determine_the_grading_method(("question6()", pp1.__str__(), actual[0].__str__))
            # asserting p2
            x.determine_the_grading_method(("question6()", pp2.__str__(), actual[1].__str__))
            # asserting f1
            x.determine_the_grading_method(("question6()", fl1.__str__(), actual[2].__str__))
            # asserting f2
            x.determine_the_grading_method(("question6()", fl2.__str__(), actual[3].__str__))
            # # asserting b1 # TODO: somehow booking numbers for b1, b2, are not 4 and 5 instead of 1 and 2
            # x.grading(("question6()", b1.__str__(), actual[4].__str__()))
            # # asserting b2
            # x.grading(("question6()", b2.__str__(), actual[5].__str__()))
            # # asserting b3 # TODO: below is not working. booking number differs.
            # x.grading(("question6()", b3.__str__(), actual[6].__str__()))

            # asserting b1
            if b1.__str__() == actual[4].__str__():
                x.determine_the_grading_method(("question6()", b1.__str__(), actual[4].__str__))
            else:
                x.determine_the_grading_method(("question6()", test[11], actual[4].__str__))
            # asserting b2
            if b2.__str__() == actual[5].__str__():
                x.determine_the_grading_method(("question6()", b2.__str__(), actual[5].__str__()))
            else:
                x.determine_the_grading_method(("question6()", test[12], actual[5].__str__()))
            # asserting b3
            if b3.__str__() == actual[6].__str__():
                x.determine_the_grading_method(("question6()", b3.__str__(), actual[6].__str__()))
            else:
                x.determine_the_grading_method(("question6()", test[13], actual[6].__str__()))
                        
            # Test below is to assert the whole printout to check the method and exception messages
            # x.determine_the_grading_method(("question6()", test[9], out))
            # asserting printout
            
            # these code are correct. #TODO however we note that this may not be the best way to do it.
            # We are allowing both test[9] and test[10] to be correct here.
            if out == test[9]:
                x.determine_the_grading_method(("question6()", test[9], out))
            else:
                x.determine_the_grading_method(("question6()", test[10], out))

            x.grading_check_setter("`fl1.flightNo = 'MY2'`", 'MY2', fl1, "flightNo", fl1._flightNo, "@flightNo.setter")
            x.grading_check_setter("`fl1.departureDate = datetime(2023, 5, 13, 10, 35)`", datetime(2023, 5, 13, 10, 35), fl1, "departureDate", fl1._departureDate, "@departureDate.setter")
            x.grading_check_setter("`b1.flight = Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15))`", Flight('MY2', 'NY', 2500, datetime(2022, 10, 21, 2, 15)), b1, "flight", b1._flight, "@flight.setter")

    def check(self, fn):
        self.check_testbook(fn)      
                