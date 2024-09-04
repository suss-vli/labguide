from learntools.core import *
from suss.dev import x

class Question4(FunctionProblem):
    _var="BankAccount"
    _test_cases = [
        (['accountId', 'balance', 'changePin', 'deposit', 'pin', 'transfer', 'withdraw'], "B1", 111, 100.00, "B2", 222, 100.00, 'B1 $200.00', 'B1 $160.00', 'B2 $120.00') 
    ]

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)

            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                if item == "accountId":
                    if isinstance(fn.accountId, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`accountId` should be a property.")
                elif item == "pin":
                    if isinstance(fn.pin, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`pin` should be a property.")
                elif item == "balance":
                    if isinstance(fn.balance, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`balance` should be a property.")


            b1 = fn(test[1], test[2], test[3])
            b2 = fn(test[4], test[5], test[6])
            b1.deposit(100)
            
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), test[7], b1.__str__))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), False, b1.changePin(100, 123)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), True, b1.changePin(111, 123)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), False, b2.withdraw(200)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), True, b1.withdraw(20)))
            x.determine_the_grading_method(((test[1], test[2], test[3], test[4], test[5], test[6]), True, b1.transfer(b2, 20)))
            x.determine_the_grading_method((('b1.withdraw(20)', 'b1.transfer(b2, 20)'), test[8], b1.__str__))
            x.determine_the_grading_method((('b1.withdraw(20)', 'b1.transfer(b2, 20)'), test[9], b2.__str__))

            x.grading_check_setter("`b1.balance = 1.00`", 1.00, b1, "balance", b1._balance, "@balance.setter")         
            
    def check(self, fn):
        self.check_testbook(fn)       
