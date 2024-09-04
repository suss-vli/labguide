from learntools.core import *
from ...dev import x

class Question1A(FunctionProblem):
    _var="Customer"
    _test_cases = [(['PREVAILING_INTEREST','getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan'],'V123', 'Tom', 2800, 10000, """Id: V123 Name: Tom   Loan: $10000 Salary: $2800.00""")]
    
    # def test_cases(self):
    #     return self._test_cases

#TODO: NOTE that the indentation of such class is highly important. any syntax error will not be reflected. 
    valued_customer = """
    
class ValuedCustomer(Customer):
    def __init__(self, custid, name, salary, loan):
        super().__init__(custid, name, loan)
        self._salary = salary       
        
    @property
    def salary(self):
        return self._salary
    
    def getCreditLimit(self):
        return self._salary * 12 * 2.5

    def getInterestOnLoan(self):
        return self._loan * (type(self).getInterestRate() + 0.01)
    
    def __str__(self):
        return f'{super().__str__()} Salary: ${self._salary:.2f}'
"""

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)

            # TODO: IMPORTANT:  given the abstract class cannot be instantiated, we cannot test its __str__() due to this nature of abstract class. 
            # thus, we will only test the attributes name and methods name of the abstract class.
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
                # TODO: below is checking `id` as property. Instructor solution for `id` is @classmethod
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

            code = x.get_source_code("lab6", 5, "Customer")
            # print("=---------")
            # print(code)
            combined = code + self.valued_customer
            x.test_for_none_162(combined, "lab6", "5", ["Customer", "ValuedCustomer"])
            data = x.create_many_objects_from_source_code(combined, ["Customer", "ValuedCustomer"])
            v = data["ValuedCustomer"]
            customer1 = data["Customer"]
            c1 = v(test[1], test[2], test[3], test[4])
            # print(c1.__str__()) 
            # from customer1 import Customer, getCreditLimit
            # print(hasattr(customer1, 'getCreditLimit') and callable(customer1.getCreditLimit))
             
            # TODO: the below error is the same error faced in lab6q3b
            # TODO: the error we face from line 73 is :

#             TypeError                                 Traceback (most recent call last)
# /home/janetanjy/ilabguide/lab6.ipynb-question.ipynb Cell 7 in 5
#       1 # Uncomment to print the output of question1a()
#       2 # question1a()
#       3 
#       4 # Uncomment the next line to check your answer
# ----> 5 q1.a.check()

# File ~/ilabguide/venv/lib/python3.8/site-packages/learntools/vli/hide_solution_before_counter.py:46, in check_before_solution..wrapper(self, *args, **kwargs)
#      45 def wrapper(self, *args, **kwargs):
# ---> 46     results = method(self, *args, **kwargs)
#      47     if self._last_outcome == OutcomeType.PASS:
#      48         self._num_checks = COUNTER + 1

# File ~/ilabguide/venv/lib/python3.8/site-packages/learntools/core/problem_view.py:19, in record..wrapped(self, *args, **kwargs)
#      16 @functools.wraps(method)
#      17 def wrapped(self, *args, **kwargs):
#      18     self.interactions[method.__name__] += 1
# ---> 19     return method(self, *args, **kwargs)

# File ~/ilabguide/venv/lib/python3.8/site-packages/learntools/vli/analytics.py:39, in displayer..wrapped(self, *args, **kwargs)
#      37 @functools.wraps(fn)
#      38 def wrapped(self,*args, **kwargs):
# ---> 39     res = fn(self,*args, **kwargs)
#      40     display(res)
#      41     email = get_email()                

# File ~/ilabguide/venv/lib/python3.8/site-packages/learntools/core/problem_view.py:92, in ProblemView.check(self)
#      87         args = ()
#      89     # display("----")
#      90     # display(args)    
#      91     # self.problem.check_whether_attempted(*args)
# ---> 92     self.problem.check(*args)
#      93 except NotAttempted as e:
#      94     self._track_check(tracking.OutcomeType.UNATTEMPTED)

# File ~/ilabguide/venv/lib/python3.8/site-packages/suss/ict162/lab6.py:76, in Question1A.check(self, fn)
#      75 def check(self, fn):
# ---> 76     self.check_testbook(fn)

# File ~/ilabguide/venv/lib/python3.8/site-packages/suss/ict162/lab6.py:72, in Question1A.check_testbook(self, fn)
#      70 c1 = v(test[1], test[2], test[3], test[4])
#      71 print(c1.__str__())
# ---> 72 x.determine_the_grading_method((("V123","Tom", 2800, 10000), test[6], customer1.__str__()))
#      73 x.determine_the_grading_method((("V123","Tom", 2800, 10000), test[5], c1.__str__()))
#   TypeError: __str__() missing 1 required positional argument: 'self'
            # x.determine_the_grading_method((("V123","Tom", 2800, 10000), test[6], str(customer1(1, 'John', 1000)))) #TODO: this is producing the above error. we have faced this before. we cannot access abstract class Customer.__str__(), which leads us to line 121. We need to figure out (1) do we need to test abstract class? (2) if yes, how? - this is the same issue for lab6q3b
            # print(test[5]) #they are the same test[5] == c1.__str__()
            # print(c1.__str__()) #they are the same test[5] == c1.__str__()
            # because Customer is an abstract method, we cannot access the __str__() directly. 
            x.determine_the_grading_method((("V123","Tom", 2800, 10000), test[5], c1.__str__()))
                
    def check(self, fn):
        self.check_testbook(fn)

class Question1B(FunctionProblem):
    _var="ValuedCustomer"
    _test_cases = [
        # TODO: Noted on the difference in the extra spaces between the name and word `Loan`, and between the `$` and amount for Loan for two different test case.
        (['PREVAILING_INTEREST', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan', 'salary'], '123', 'Tom', 2800, 8000, """Id: 123 Name: Tom   Loan: $ 8000 Salary: $2800.00""", 84000.0, 280.0),
        (['PREVAILING_INTEREST', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan', 'salary'], '922', 'Sally', 10000, 10000, """Id: 922 Name: Sally Loan: $10000 Salary: $10000.00""", 300000.0, 350.00000000000006)
        ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)
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
                elif item == "salary":
                    if isinstance(fn.salary, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`salary` should be a property.")


            vc1 = fn(test[1], test[2], test[3], test[4])
           
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[5], vc1.__str__))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[6], vc1.getCreditLimit))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[7], vc1.getInterestOnLoan))
                
    def check(self, fn):
        self.check_testbook(fn)

class Question1C(FunctionProblem):
    _var="CorporateCustomer"
    _test_cases = [
        (['PREVAILING_INTEREST', 'assetValue', 'business', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan'], '123', 'Tom', 'Retail', 5000, 8000, """Id: 123 Name: Tom   Loan: $ 8000 Business: Retail Asset Value: $5000""", 15000, 240.00000000000003),
        (['PREVAILING_INTEREST', 'assetValue', 'business', 'getCreditLimit', 'getInterestOnLoan', 'getInterestRate', 'id', 'loan'], '922', 'Sally', 'Food', 10000, 10000, """Id: 922 Name: Sally Loan: $10000 Business: Food Asset Value: $10000""", 30000, 300.0)
        ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            answer = dir(fn)
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
                elif item == "assetValue":
                    if isinstance(fn.assetValue, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`assetValue` should be a property.")
                elif item == "business":
                    if isinstance(fn.business, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`assetValue` should be a property.")

            cc1 = fn(test[1], test[2], test[3], test[4], test[5])
           
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[6], cc1.__str__))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[7], cc1.getCreditLimit))
            x.determine_the_grading_method(((test[1], test[2], test[3]), test[8], cc1.getInterestOnLoan))
                
    def check(self, fn):
        self.check_testbook(fn)

Question1 = MultipartProblem(
    Question1A,
    Question1B,
    Question1C
)    
