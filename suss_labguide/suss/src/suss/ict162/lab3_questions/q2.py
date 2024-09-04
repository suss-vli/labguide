from learntools.core import *
from suss.dev import x
        

class Question2A(FunctionProblem):
    _var="BankAccount"    
    _test_cases = [
        (['_interestRate', 'accountId', 'accumulateInterest', 'balance', 'deposit', 'transfer', 'withdraw'], '002', 50, 10, 40, '002 40.00', '002 20.00', '002 60.00', '002 80.00', '002 82.40'),
        (['_interestRate', 'accountId', 'accumulateInterest', 'balance', 'deposit', 'transfer', 'withdraw'], '001', 100, 30, 50, '001 70.00', '001 50.00', '001 100.00', '001 120.00', '001 123.60')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            for item in test[0]:
                if item in dir(fn):
                    x.justpass()
                else:
                    x.justfail((item, fn.__class__.__name__))

            ba1 = fn(test[1], test[2])

            ba1.withdraw(test[3])
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[5], ba1.__str__))
            ba1.withdraw()
            x.determine_the_grading_method(('no amount', test[6], ba1.__str__))

            ba1.deposit(test[4])
            x.determine_the_grading_method(((test[1], test[2], test[4]), test[7], ba1.__str__))
            ba1.deposit()
            x.determine_the_grading_method(('no amount', test[8], ba1.__str__))
            ba1.accumulateInterest()
            x.determine_the_grading_method(((test[8]), test[9], ba1.__str__))

            x.grading_check_setter("`ba1.balance = 1.00`", 1.00, ba1, "balance", ba1._balance, "@balance.setter")         

    def check(self, fn):
        self.check_testbook(fn)       

class Question2B(FunctionProblem):
    _var="JuniorAccount"
    _test_cases = [
        ('002', 200, 'Jane', 40, 70, 'Guardian: Jane 002 160.00', 'Guardian: Jane 002 90.00'),
        ('001', 100, 'John', 30, 60, 'Guardian: John 001 70.00', 'Guardian: John 001 10.00')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            ja1 = fn(test[0], test[1], test[2])
            #TODO Do we need to test for a `False` case?
            ja1.withdraw(test[3])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[5], ja1.__str__))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), False, ja1.withdraw(test[4]))) 

            ja1.withdraw(test[4], test[2])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[6], ja1.__str__))

    def check(self, fn):
        self.check_testbook(fn)       

class Question2C(FunctionProblem):
    _var="JuniorAccount"
    _test_cases = [
        ('002', 200, 'Jane', 150, ['001', 100], 'Guardian: Jane 002 50.00', '001 250.00'),
        ('001', 100, 'John', 30, ['002', 10], 'Guardian: John 001 70.00', '002 40.00')
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            ba = x.get_object_from_lab("lab3", 17, "BankAccount")
            ba1 = ba(*test[4])
            ja1 = fn(test[0], test[1], test[2])
            ja1.transfer(ba1, test[3], test[2])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[5], ja1.__str__))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[6], ba1.__str__))
            
    def check(self, fn):
        self.check_testbook(fn)       

Question2 = MultipartProblem(
    Question2A,
    Question2B,
    Question2C
)    