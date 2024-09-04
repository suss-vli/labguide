from learntools.core import *
from suss.dev import x

class Question5A(FunctionProblem):
    _var="Vehicle"
    _test_cases = [
        (['capacity', 'computeRoadTax', 'installment', 'vehNo'], 'v1', 2000, 'John', 55, """John 55 v1 Capacity: 2000 Road Tax: $1800.0 """)
    ]
    
    def test_cases(self):
        return self._test_cases
    
    passenger_vehicle = """
    
class PassengerVehicle(Vehicle):
    def __init__(self, vehNo, capacity, owner, age):
        # write your answer here
        super().__init__(vehNo, capacity)
        self._owner = owner
        self._age = age
        pass
        
    def computeRoadTax(self):
        # write your answer here
        return self.capacity if self._age < 55 else 0.9 * self.capacity
        pass
        
    def __str__(self):
        # write your answer here
        return f'{self._owner} {self._age} {super().__str__()} '
"""
    

    def check_testbook(self, fn):
        for test in self._test_cases:
            answer = dir(fn)

            for item in test[0]:
                if item == "vehNo":
                    if isinstance(fn.vehNo, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`vehNo` should be a property.")
                elif item == "loan":
                    if isinstance(fn.loan, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`loan` should be a property.")
                elif item == "capacity":
                    if isinstance(fn.capacity, property):
                        x.justpass()
                    else:
                        x.justfail(item, "`capacity` should be a property.")
                elif item in answer: 
                    x.justpass()
                else:
                    x.justfail(item, f"""The attribute `{item}` is not defined in the class.""")
                    # TODO: we noted that we did not tell the student what to do next, even though we detected that the attribute is missing. ChatGPT will tell you what to do next.
            
            #testing abstract class string
            code = x.get_source_code("lab3", 38, "Vehicle")
            combined = code + self.passenger_vehicle
            x.test_for_none_162(combined, "lab3", "38", ["Vehicle","PassengerVehicle"])
            data = x.create_many_objects_from_source_code(combined, ["Vehicle", "PassengerVehicle"])
            pv = data["PassengerVehicle"]
            c1 = pv(test[1], test[2], test[3], test[4])
            x.determine_the_grading_method((('v1', 2000, 'John', 55,), test[5], c1.__str__))
                
    def check(self, fn):
        self.check_testbook(fn)      

class Question5B(FunctionProblem):
    _var="PassengerVehicle"
    _test_cases = [
        ('v1', 2000, 'John', 55, """John 55 v1 Capacity: 2000 Road Tax: $1800.0 """),
        ('v2', 2000, 'Jane', 54, """Jane 54 v2 Capacity: 2000 Road Tax: $2000 """)
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            p1 = fn(test[0], test[1], test[2], test[3])
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[4], p1.__str__))            

    def check(self, fn):
        self.check_testbook(fn)   

class Question5C(FunctionProblem):
    _var="CommercialVehicle"
    _test_cases = [
        ('v3', 5000, 'company1', 3, """company1 3 v3 Capacity: 5000 Road Tax: $5000"""),
        ('v4', 5000, 'company2', 3.1, """company2 3.1 v4 Capacity: 5000 Road Tax: $7500.0""")
    ]
    
    def test_cases(self):
        return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases:
            c1 = fn(test[0], test[1], test[2], test[3])        
            x.determine_the_grading_method(((test[0], test[1], test[2], test[3]), test[4], c1.__str__))
            
    def check(self, fn):
        self.check_testbook(fn) 

class Question5D(FunctionProblem):
    _var="question5d"
    _test_cases = [
        (['_age', '_capacity', '_owner', '_vehNo', 'capacity', 'computeRoadTax', 'installment', 'vehNo'], ['_capacity', '_coyReg', '_maxLadenWeight', '_vehNo', 'capacity', 'computeRoadTax', 'installment', 'vehNo'], ['v1', 2000, 'John', 55], ['v2', 2000, 'Jane', 54], ['v3', 5000, 'company1', 3], ['v4', 5000, 'company2', 3.1], """John 55 v1 Capacity: 2000 Road Tax: $1800.0 
150.0
Jane 54 v2 Capacity: 2000 Road Tax: $2000 
166.66666666666666
company1 3 v3 Capacity: 5000 Road Tax: $5000
416.6666666666667
company2 3.1 v4 Capacity: 5000 Road Tax: $7500.0
625.0\n""")
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
                        test_list = test[0] 
                    else:
                        test_list = test[1]

                for item in test_list:
                    if item in dir(obj):
                        x.justpass()
                    else:
                        x.justfail((item, obj.__class__.__name__))            


            vehicle_code = x.get_source_code("lab3", 38,"Vehicle")
            passenger_vehicle_code = x.get_source_code("lab3", 42,"PassengerVehicle") 
            commercial_vehicle_code = x.get_source_code("lab3", 46,"CommercialVehicle")

            source_code = vehicle_code + passenger_vehicle_code + commercial_vehicle_code

            x.test_for_none_162(source_code, "lab3", "38,42,46", ["Vehicle", "PassengerVehicle","CommercialVehicle"])

            data = x.create_many_objects_from_source_code(source_code, ["Vehicle", "PassengerVehicle", "CommercialVehicle"])
            
            pv = data["PassengerVehicle"]
            cv = data["CommercialVehicle"]

            pv1 = pv(*test[2])
            pv2 = pv(*test[3])
            cv1 = cv(*test[4])
            cv2 = cv(*test[5])

            # Test below is to assert p1 string
            x.determine_the_grading_method(("question5d()", pv1.__str__(), actual[0].__str__))
            
            # Test below is to assert p2 string
            x.determine_the_grading_method(("question5d()", pv2.__str__(), actual[1].__str__))

            # Test below is to assert c1 string
            x.determine_the_grading_method(("question5d()", cv1.__str__(), actual[2].__str__))
            
            # Test below is to assert c2 string
            x.determine_the_grading_method(("question5d()", cv2.__str__(), actual[3].__str__))

            # Test below is to assert the whole printout
            x.determine_the_grading_method(("question5d()", test[6], out))

    def check(self, fn):
        self.check_testbook(fn)
       
Question5 = MultipartProblem(
    Question5A,
    Question5B,
    Question5C,
    Question5D
)    
      