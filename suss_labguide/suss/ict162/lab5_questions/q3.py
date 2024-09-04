import time
from ...dev import x
import tkinter as tk
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext

class Question3(FunctionProblem):
    _var="ATMGui"
    _test_cases = [
        (1, 111, "ten", 10, 200, 20, """1 100 retrieved
ten is not a whole number
Balance before deposit $100.00
Balance after depositing 10 is $110.00
ten is not a whole number
Insufficient balance $110.00 to withdraw $200
Balance before withdrawing $110.00
Balance after withdrawing 20 is $90.00
checking balance activated.
Balance is $90.00\n\n""", "1 90 retrieved\n\n"),
(2, 222, "ten", 20, 300, 30, """2 200 retrieved
ten is not a whole number
Balance before deposit $200.00
Balance after depositing 20 is $220.00
ten is not a whole number
Insufficient balance $220.00 to withdraw $300
Balance before withdrawing $220.00
Balance after withdrawing 30 is $190.00
checking balance activated.
Balance is $190.00\n\n""", "2 190 retrieved\n\n"),
(3, 333, "ten", 30, 400, 40, """3 300 retrieved
ten is not a whole number
Balance before deposit $300.00
Balance after depositing 30 is $330.00
ten is not a whole number
Insufficient balance $330.00 to withdraw $400
Balance before withdrawing $330.00
Balance after withdrawing 40 is $290.00
checking balance activated.
Balance is $290.00\n\n""", "3 290 retrieved\n\n"),
# TODO: come back to look at this next round. below test case is to test when the pin is incorrect. test will pass but it will throw an exception error in Tkinter for AttributeError: 'NoneType' object has no attribute 'pin'
# (1, 222, "ten", 10, 200, 20, "Please check data. Login is unsuccessful\n\n", "Please check data. Login is unsuccessful\n\n")

# TODO: we can add more test cases to test 2nd and 3rd bank account, and also when pin/account id is invalid, or only pin/id is entered and not both causing an error
    ]
       
    #TODO note that this takes in a values as a list
    def insert_into_entry(self, root, values):
        values_iter = iter(values)
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):
                        try:
                            next_value = next(values_iter)
                        except StopIteration:
                            break  # No more values to insert
                        grandchild.insert(0, next_value)
                        root.update()
                            
    def invoke_element(self,root,element):
            # print("reach invoke element")
        for child in root.winfo_children():
            # if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("reach child")
                # print(len(child.winfo_children()))
                # print(child.winfo_children())
            for grandchild in child.winfo_children():
                if isinstance(grandchild, ttk.Button) and grandchild is element:  # if the grandchild is an Entry
                    # print("reach grandchild")
                    # print(grandchild)
                    element.event_generate('<Button-1>')
                    # root.call(grandchild['checkGuess']())
                    # grandchild.invoke()  # insert the value into the Entry
                    root.update()
                    # root.update_idletasks()
                # else for great_grandchild in grandchil.winfo_children():
                #     if isinstance(great_grandchild, ttk.Button):
                #         element.event_generate('<Button-1>')
                    return
                
    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("1 - 15 may")
                # print(child.winfo_children())
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, scrolledtext.ScrolledText):  # if the grandchild is an Entry
                        # print("reach grandchild")
                        return grandchild.get(1.0, tk.END)

    # def test_cases(self):
    #     return self._test_cases

    def check_testbook(self, fn):
        #TODO: Note that we allowed the error to surface when there is no answer or no return value for this lab. 
        # For instance, student will face AttributeError: 'Q1GUI' object has no attribute 'tk' for lab5q1
        # TODO: we need to fix this in the future. Maybe we should capture these error? 
        for test in self._test_cases:
            source = x.get_source_code("lab5", 12, "Bank, BankAccount")
            x.test_for_none_162(source, "lab5", "12",  ["Bank", "BankAccount"])
            data = x.create_many_objects_from_source_code(source, ["Bank", "BankAccount"])
            bank =  data["Bank"]('POSB')
            # print(bank)
            bank.addAccount(data["BankAccount"](1, 111, 100))
            bank.addAccount(data["BankAccount"](2, 222, 200))
            bank.addAccount(data["BankAccount"](3, 333, 300))
            root = tk.Tk()
            app = fn(bank, root)
            # app = fn(bank)
            app.pack()
            app.update()

            # app, root = x.setup_gui(tk,fn)
            time.sleep(2)
            # print("root - printed")
            # x.scan_through_every_layers(root)
            # print("app - printed")
            # x.scan_through_every_layers(app)
            
            #change 1
            # print("app.win - printed")
            # x.scan_through_every_layers(app.win)

            #change 2
            # self.insert_into_entry(app.win, ["1","111"])
            self.insert_into_entry(root, [test[0], test[1]])

            # time.sleep(2)
            #change 3
            # self.invoke_element(app.win)
            self.invoke_element(root, app._login_btn)  

            # Enable the _amount_ety widget
            # app._amount_ety.config(state=tk.NORMAL)

            # Insert the value "ten" into _amount_ety
            
            app._amount.set(test[2])
            self.invoke_element(root, app._deposit_btn)

            app._amount.set(test[3])
            self.invoke_element(root, app._deposit_btn)

            app._amount.set(test[2])
            self.invoke_element(root, app._withdraw_btn)

            app._amount.set(test[4])
            self.invoke_element(root, app._withdraw_btn)

            app._amount.set(test[5])
            self.invoke_element(root, app._withdraw_btn)

            self.invoke_element(root, app._check_btn)
            
            #change 4
            # answer = self.get_text_from_scrolled_text(app.win)
            answer = self.get_text_from_scrolled_text(root)

            # print(f"answer is '{answer}'")
            x.grading_with_string_comparison2((test[6], answer))
            
            self.invoke_element(root, app._logout_btn)

            self.insert_into_entry(root, [test[0], test[1]])
            self.invoke_element(root, app._login_btn)

            answer2 = self.get_text_from_scrolled_text(root)
            x.grading_with_string_comparison2((test[7], answer2))

            #change 5
            # x.clear_gui(app.win, root)
            x.clear_gui(app, root)

    def check(self, fn):
        self.check_testbook(fn)       
