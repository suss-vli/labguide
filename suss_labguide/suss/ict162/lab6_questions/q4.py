from learntools.core import *
from ...dev import x
import time
import tkinter as tk
from tkinter import ttk, Label, Button, scrolledtext

class Question4A(FunctionProblem):
    _var="Store"
    _test_cases = [
        ('Clam Chowder', 9.90, 'Mushroom', 7.90, 'Tomato', 5.90, 'Pumpkin', 'Oxtail', """C Clam Chowder   $9.90 Available: 50
M Mushroom       $7.90 Available: 50
O Oxtail         $9.90 Available: 50
P Pumpkin        $5.90 Available: 50
T Tomato         $5.90 Available: 50""", 'C', 20, """C Clam Chowder   $9.90 Available: 30""", 10, """C Clam Chowder   $9.90 Available: 40
M Mushroom       $7.90 Available: 50
O Oxtail         $9.90 Available: 50
P Pumpkin        $5.90 Available: 50
T Tomato         $5.90 Available: 50""")        
    ]
   
    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        for test in self._test_cases: 
            Soup = x.get_object_from_lab("lab6", 35, "Soup")
            store = fn()
            store.addSoup(Soup(test[0], test[1]))
            store.addSoup(Soup(test[2], test[3]))
            store.addSoup(Soup(test[4], test[5]))
            store.addSoup(Soup(test[6], test[5]))
            store.addSoup(Soup(test[7], test[1]))

        x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7]), test[8], store.listAvailableSoup))
        store.purchase(test[9], test[10])
        x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7]), test[11], store.listSoupToReplenish))
        store.replenish(test[9], test[12])
        x.determine_the_grading_method(((test[0], test[1], test[2], test[3], test[4], test[5], test[6], test[7]), test[13], store.listAvailableSoup))

        x.grading_check_setter("`store._soups['C'].quantity = 10", 10, store._soups['C'], "quantity", store._soups['C']._quantity, "@quantity.setter")
    def check(self, fn):
        self.check_testbook(fn)       

class Question4B(FunctionProblem):
    _var="CashRegisterGui"
    _test_cases = [("""Please enter valid soup code

Please enter a whole number for quantity

Please enter valid quantity

Purchase operation is successful

List of Available Soups:
C Clam Chowder   $9.90 Available: 40
M Mushroom       $7.90 Available: 50
O Oxtail         $9.90 Available: 50
P Pumpkin        $5.90 Available: 50
T Tomato         $5.90 Available: 50

Please enter valid quantity

Replenish operation is successful

List of Soups to Replenish:
C Clam Chowder   $9.90 Available: 45


""")]
    
    # def test_cases(self):
    #     return self._test_cases


    #TODO note that this takes in a values as a list
    def insert_into_entry(self, root, values):
        # print("did it reach here")
        values_iter = iter(values)
        # print(root.winfo_children())
        for child in root.winfo_children():
            # if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):
                        try:
                            next_value = next(values_iter)
                        except StopIteration:
                            break  # No more values to insert
                        grandchild.insert(0, next_value)
                        root.update()       

    def select_replenish_radiobutton(self,root,element):
        for child in root.winfo_children():
            for grandchild in child.winfo_children():
                for great_grandchild in grandchild.winfo_children():
                    if isinstance(great_grandchild, tk.Radiobutton):
                        element.set(1)
                        root.update()
                        return

    def invoke_element(self,root,element):
        for child in root.winfo_children():
                for grandchild in child.winfo_children():
                    for great_grandchild in grandchild.winfo_children():
                        if isinstance(great_grandchild, ttk.Button):  
                            element.event_generate('<Button-1>')
                            root.update()
                            return
                
    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            for grandchild in child.winfo_children():
                for great_grandchild in grandchild.winfo_children():
                    if isinstance(great_grandchild, scrolledtext.ScrolledText):  # if the grandchild is an Entry
                        return great_grandchild.get(1.0, tk.END)

    def check_testbook(self, fn):
        for test in self._test_cases:
            source = x.get_source_code("lab6", 35, "Soup, Store")
            x.test_for_none_162(source, "lab6", "35", ["Soup", "Store"])
            data = x.create_many_objects_from_source_code(source, ["Soup", "Store"])
            Soup = data["Soup"]
            Store = data["Store"] 

            store = Store()
            store.addSoup(Soup('Clam Chowder', 9.90))
            store.addSoup(Soup('Mushroom', 7.90))
            store.addSoup(Soup('Tomato', 5.90))
            store.addSoup(Soup('Pumpkin', 5.90))
            store.addSoup(Soup('Oxtail', 9.90))
            # print(store.listAvailableSoup())

            # print("does this work")
            # (app, root) = x.setup_gui4(store, tk, fn)
            
            root = tk.Tk()
            app = fn(store, root)
            app.grid()
            # app.mainloop()
            # app.grid()
            app.update()

            # print("reached here")
            time.sleep(2)
                        
            # test invalid code and qty input

            soup_code = "X"
            number = 10
            self.insert_into_entry(root, [soup_code, number])
            self.invoke_element(root, app.submit_btn)

            soup_code1 = "C"
            number1 = "seven"
            self.insert_into_entry(root, [soup_code1, number1])
            self.invoke_element(root, app.submit_btn)

            number2 = 51
            self.insert_into_entry(root, [soup_code1, number2])
            self.invoke_element(root, app.submit_btn)

            # test valid qty
            number3 = 10
            self.insert_into_entry(root, [soup_code1, number3])
            self.invoke_element(root, app.submit_btn)
            #test display
            self.invoke_element(root, app.display_btn)
   

            # test replenish
            self.select_replenish_radiobutton(root, app.radValue)
            self.insert_into_entry(root, [soup_code1, 50])
            self.invoke_element(root, app.submit_btn)

            self.insert_into_entry(root, [soup_code1, 5])
            self.invoke_element(root, app.submit_btn)
            # check display for replenish qty
            self.invoke_element(root, app.display_btn)
            str = self.get_text_from_scrolled_text(root)
            x.grading_with_string_comparison2((test, str))  

            x.clear_gui(app, root)



            # root = tk.Tk()
            # app = fn(store, root)
            # app.pack()

            # app.update()
            # #change1
            # x.scan_through_every_layers(app)
            # #change2
            # x.test_through_every_layers(app, root, app)
            # # time.sleep(2)

            # #testing inserting value
            # self.insert_into_entry(root, ["C", "10"])
            # self.invoke_element(root)

            # answer= self.get_text_from_scrolled_text(root)
            # print(f"answer is '{answer}'")
            # assert answer == "hello"

            # #change3
            # x.clear_gui(app, root)

    def check(self, fn):
        self.check_testbook(fn)    

Question4 = MultipartProblem(
    Question4A,
    Question4B
)     