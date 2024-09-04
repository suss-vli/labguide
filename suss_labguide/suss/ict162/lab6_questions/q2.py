from learntools.core import *
from ...dev import x

class Question2(FunctionProblem):
    _var="Bank"
    _test_cases = [
        ('123', 'Tom', 2800, 10000, '922', 'Sally', 'Food', 10000, 10000, """Id: 123 Name: Tom   Loan: $10000 Salary: $2800.00                    Credit Limit: $ 84000 Interest on Loan: $350""", """Id: 123 Name: Tom   Loan: $10000 Salary: $2800.00                    Credit Limit: $ 84000 Interest on Loan: $350
Id: 922 Name: Sally Loan: $10000 Business: Food Asset Value: $10000  Credit Limit: $ 30000 Interest on Loan: $300""", """Id: 922 Name: Sally Loan: $10000 Business: Food Asset Value: $10000""")
    ]
    
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            customer_code = x.get_source_code("lab6", 5, "Customer") 
            valued_customer_code = x.get_source_code("lab6", 9, "ValuedCustomer") 
            corporate_customer_code =x.get_source_code("lab6", 13, "CorporateCustomer")
            text_source = customer_code + valued_customer_code + corporate_customer_code
            x.test_for_none_162(text_source, "lab6", "5,9,13", ["Customer", "ValuedCustomer", "CorporateCustomer"])
            data = x.create_many_objects_from_source_code(text_source, ["Customer", "ValuedCustomer", "CorporateCustomer"])
            
            c1 = data["Customer"]
            vc = data["ValuedCustomer"]
            cc = data["CorporateCustomer"]
            
            cList = fn()
            cList.add(vc(test[0], test[1], test[2], test[3]))
            
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[9], cList.listAllStr))
            cList.add(cc(test[4], test[5], test[6], test[7], test[8]))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7], test[8]), test[10], cList.listAllStr))
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7], test[8]), test[11], cList.search), test[4])

    def check(self, fn):
        self.check_testbook(fn)       
