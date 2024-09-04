from learntools.core import *
from suss.dev import x

class Question3(FunctionProblem):
    _var="MovieCard"
    _test_cases = [
        (70, 10, 3, 5, 2, """Ticket price: $70, tickets remaining: 9""", """Ticket price: $70, tickets remaining: 1""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            m = fn(test[0])
            if m.tickets == None:
                x.justfail("NoneType", f"`m.tickets` is {m.tickets}. Please attempt the question and run the question again.")
            else:
                x.determine_the_grading_method((test[0], test[1], m.tickets))

            m.redeemTicket()
            x.determine_the_grading_method((test[0], test[5], m.__str__))

            m.redeemTicket(test[2])
            x.determine_the_grading_method((test[0], test[5], m.__str__)) 

            for i in range(test[3]):
                m.redeemTicket(test[4])
              
            x.determine_the_grading_method((test[0], test[6], m.__str__))

            x.grading_check_setter("`m.tickets = 1`", 1, m, "tickets", m._tickets, "@tickets.setter")

    def check(self, fn):
        self.check_testbook(fn)       
