from learntools.core import *
from suss.dev import x

class Question4(FunctionProblem):
    _var="HSBCMovieCard"
    _test_cases = [
        ('John', 70, 12, 3, 5, 4, """Name: John Ticket price: $70, tickets remaining: 11""", """Name: John Ticket price: $70, tickets remaining: 8""", """Name: John Ticket price: $70, tickets remaining: 0"""),
        ('Jane', 100, 17, 3, 5, 4, """Name: Jane Ticket price: $100, tickets remaining: 16""", """Name: Jane Ticket price: $100, tickets remaining: 13""", """Name: Jane Ticket price: $100, tickets remaining: 1""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            m = fn(test[0], test[1])
            if m.tickets == None:
                x.justfail("NoneType", f"`m.tickets` is {m.tickets}. Please attempt the question and run the question again.")
            else:
                x.determine_the_grading_method(((test[0], test[1]), test[2], m.tickets))
                m.redeemTicket()
                x.determine_the_grading_method(((test[0], test[1]), test[6], m.__str__))
                m.redeemTicket(test[3])
                x.determine_the_grading_method(((test[0], test[1]), test[7], m.__str__)) 

                for i in range(test[4]):
                    m.redeemTicket(test[5])
                
                x.determine_the_grading_method(((test[0],test[1]), test[8], m.__str__))
                
    def check(self, fn):
        self.check_testbook(fn)       

