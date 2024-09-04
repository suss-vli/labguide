import time
from ...dev import x
import tkinter as tk
from learntools.core import *
from tkinter import ttk

class Question2(FunctionProblem):
    _var="Q2GUI"    
    _test_cases = [
        (10, 10, "ht 10.0 wt 10.0, bmi is 0.10\n", "ht 10.0 wt 10.0, bmi is 70.30\n"),
        ("ten", 10, "ten is not a number\n", "ten is not a number\n")
        # unable to test the condition below for "Please enter both height and weight"
        # ("", "", "Please enter both height and weight\n", "Please enter both height and weight\n") 
    ]
    
    # def test_cases(self):
    #     return self._test_cases
    
    def insert_into_entry(self,root, value, value2):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("1 - 15 may")
                # print(child.winfo_children())
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):  # if the grandchild is an Entry
                        # print("reach grandchild")
                        grandchild.insert(0, value)  # insert the value into the Entry
                        # grandchild.insert(0, value2)  # insert the value into the Entry
                        root.update()
        
        return

    def invoke_element(self,root):
        for child in root.winfo_children():
            for grandchild in child.winfo_children():
                if isinstance(grandchild, ttk.Button):  # if the grandchild is an Entry
                    # print("reach grandchild")
                    # print(grandchild)
                    grandchild.event_generate('<Button-1>')
                    # root.call(grandchild['checkGuess']())
                    # grandchild.invoke()  # insert the value into the Entry
                    root.update()
                    # root.update_idletasks()
                    return

    def select_lb_rbtn(self,root,element):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):
                for grandchild in child.winfo_children():
                    # for great_grandchild in grandchild.winfo_children():
                    if isinstance(grandchild, ttk.Radiobutton):
                        element.set(5)
                        root.update()
                        return

    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, ttk.Label):  # if the grandchild is an Entry
                # print("reach grandchild")
                # print(f"child:")
                # print(child.cget("text"))
                return child.cget("text")

            for grandchild in child.winfo_children():
                if isinstance(grandchild, ttk.Label): # if the grandchild is an Entry
                    # print("reach grandchild")
                    # print(grandchild.cget("text"))
                    print(grandchild.winfo_name())
                    # return grandchild.cget("text")
                    # return grandchild.get(1.0, tk.END)

    def check_testbook(self, fn):
        #TODO: Note that we allowed the error to surface when there is no answer or no return value for this lab. 
        # For instance, student will face AttributeError: 'Q1GUI' object has no attribute 'tk' for lab5q1
        # TODO: we need to fix this in the future. Maybe we should capture these error? 
        for test in self._test_cases:
            app, root = x.setup_gui3(tk,fn)
            # print("blah")
            time.sleep(2)
            # x.scan_through_every_layers(root)

            # test kg
            self.insert_into_entry(root, test[0], test[1])
            self.invoke_element(root)
            time.sleep(2)
            # answer = self.get_text_from_scrolled_text(root)
            answer = app._output_lbl.cget("text")
            # print(f"answer is '{answer}'")
            x.grading_with_string_comparison2((test[2], answer))
            # test lb
            self.select_lb_rbtn(root, app._unit)
            self.insert_into_entry(root, test[0], test[1])
            self.invoke_element(root)
            # answer2 = self.get_text_from_scrolled_text(root)
            answer2 = app._output_lbl.cget("text")
            # print(f"answer2 is '{answer2}'")
            x.grading_with_string_comparison2((test[3], answer2))

            x.clear_gui(app,root)

    # This is where the actual tests happen
    def check(self, fn):
        self.check_testbook(fn)       
