from learntools.core import *
from ...dev import x

class Question3A(FunctionProblem):
    _var="InvalidCustomerException"
    _test_cases = [()]
    
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

class Question3B(FunctionProblem):
    _var="Customer2"
    _test_cases = [
        (['PREVAILING_INTEREST','checkId', 'checkLoan', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan', 'name'], '123', """First character of customer id must be either V or C: 1\n""", 100000, """Loan amount $100000 exceeds credit limit: $84000.0"""),
        (['PREVAILING_INTEREST', 'checkId', 'checkLoan', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan', 'name'], 'Cat', """Second character onwards must be a digit: at\n""", 200000, """Loan amount $200000 exceeds credit limit: $84000.0""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    valued_customer = """
    
class ValuedCustomer(Customer2):
    def __init__(self, custid, name, salary, loan):
        self._salary = salary
        super().__init__(custid, name, loan)
        
    @property
    def salary(self):
        return self._salary
    
    def getCreditLimit(self):
        return self._salary * 12 * 2.5

    def getInterestOnLoan(self):
        return self._loan * (type(self).getInterestRate() + 0.01)
    
    def __str__(self):
        return f'{super().__str__()} Salary: ${self._salary}'
"""

    def check_testbook(self, fn):
        # TODO: need to change the question to define message for exception
        # TODO: lab6q3b is also passing all the test even if no answer is written in 3b. similar to lab6q1a
        for test in self._test_cases:
            answer = dir(fn)
            
            # testing __str__ 
            invalidcustomerexception_code = x.get_source_code("lab6", 22, "InvalidCustomerException")
            customer2_code = x.get_source_code("lab6", 26, "Customer2")
            text_source = invalidcustomerexception_code + customer2_code + self.valued_customer
            x.test_for_none_162(text_source, "lab6", "22,26", ["InvalidCustomerException", "Customer2", "ValuedCustomer"])
            data = x.create_many_objects_from_source_code(text_source, ["Customer2", "ValuedCustomer"])
            v = data["ValuedCustomer"]
            c1 = v('V123', 'Tom', 2800, 5000)

            # Commenting this out because Cannot test abstract class via __str__(). c1 is ValuedCustomer is not an abstract class.
            x.determine_the_grading_method((("V123","Tom", 2800, 10000), "Id: V123 Name: Tom Loan: $5000 Salary: $2800", c1.__str__()))
            
            # TODO:  This is similar to lab6q1a. Cannot test abstract class via __str__()
            for item in test[0]:
                if item in answer: 
                    x.justpass()
                else:
                    x.justfail((item, fn.__name__))
                if item == "PREVAILING_INTEREST":
                    if fn.PREVAILING_INTEREST == 0.025:
                        x.justpass()
                    else:
                        x.justfail(item, f"`PREVAILING_INTEREST` is `{fn.PREVAILING_INTEREST}`. It should be `0.0025`.")
                elif item == "id":
                    if isinstance(fn.id, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`id` should be a property.")
                elif item == "loan":
                    if isinstance(fn.loan, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`loan` should be a property.")
                elif item == "name":
                    if isinstance(fn.name, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`name` should be a property.")
                elif item == "checkId":
                    try:
                        cid = fn.checkId(test[1])   
                    except Exception as e:
                        x.determine_the_grading_method(((test[1]), test[2], e.__str__))

                elif item == "checkLoan":
                    try:
                        
                        cln = fn.checkLoan(c1, test[3])
                    except Exception as e:
                        x.determine_the_grading_method(((test[3]), test[4], e.__str__))

                    

    def check(self, fn):
        self.check_testbook(fn)    

class Question3C(FunctionProblem):
    _var="ValuedCustomer"
    _test_cases = [
        ('V123', 'Tom', 2800, 5000, """Id: V123 Name: Tom Loan: $5000 Salary: $2800""", 84000.0, 175.00000000000003, """"""),
        ('C922', 'Sally', 3000, 8000, """Id: C922 Name: Sally Loan: $8000 Salary: $3000""", 90000.0, 280.0, """"""),
        #testing exceptions below
        ('1922', 'Sally', 2800, 1000, """Id: 1922 Name: Sally Loan: $1000 Salary: $2800""", 84000.0, 35.0, """First character of customer id must be either V or C: 1\n"""),
        ('Cat', 'John', 2800, 3000, """Id: Cat Name: John Loan: $3000 Salary: $2800""", 84000.0, 105.00000000000001, """Second character onwards must be a digit: at\n"""),
        ('V123', 'Tom', 2800, 100000, """Id: V123 Name: Tom Loan: $100000 Salary: $2800""", 84000.0, 35.0, """Loan amount $100000 exceeds credit limit: $84000.0""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            try:
                c1 = fn(test[0], test[1], test[2], test[3])
                x.grading_string_comparison_with_context(((test[0], test[1], test[2], test[3]), test[4], c1.__str__))
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[5], c1.getCreditLimit))
                x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[6], c1.getInterestOnLoan))

            except Exception as e:
                if "InvalidCustomerException" in type(e).__name__:
                    x.determine_the_grading_method((test[0], test[7], e.__str__))
                else:
                    raise(e)
 
    def check(self, fn):
        self.check_testbook(fn)  

Question3 = MultipartProblem(
    Question3A,
    Question3B,
    Question3C
)