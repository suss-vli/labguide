import time
from ...dev import x
import tkinter as tk
from unittest.mock import patch
from learntools.core import *
from tkinter import ttk, Label, Button, scrolledtext


class Question1(FunctionProblem):
    _var="Q1GUI"
    _test_cases = [("seven is not a whole number\n\n", """seven is not a whole number
40 too low!\n\n""", """seven is not a whole number
40 too low!
90 too high!\n\n""", """seven is not a whole number
40 too low!
90 too high!
50 correct!\n\n""")]
    
    # def test_cases(self):
    #     return self._test_cases
    
    def insert_into_entry(self,root, value):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("1 - 15 may")
                # print(child.winfo_children())
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, ttk.Entry):  # if the grandchild is an Entry
                        # print("reach grandchild")
                        grandchild.insert(0, value)  # insert the value into the Entry
                        root.update()
                        return
        #     else: 
        #         print("insert_into_entry - not a frame")
        # else:
        #     print("insert_into_entry - no children")
                        
    def get_text_from_scrolled_text(self,root):
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("1 - 15 may")
                # print(child.winfo_children())
                for grandchild in child.winfo_children():
                    if isinstance(grandchild, scrolledtext.ScrolledText):  # if the grandchild is an Entry
                        # print("reach grandchild")
                        return grandchild.get(1.0, tk.END)

                        
    def invoke_element(self,root):
        # print("reach invoke element")
        for child in root.winfo_children():
            if isinstance(child, tk.Frame):  # if the child is a Frame
                # print("reach child")
                # print(len(child.winfo_children()))
                # print(child.winfo_children())
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
        #     else:
        #         print("invoke_element - not a frame")
        # else:
        #     print("insert_into_entry - no children")


    def check_testbook(self, fn):
        #TODO: Note that we allowed the error to surface when there is no answer or no return value for this lab. 
        # For instance, student will face AttributeError: 'Q1GUI' object has no attribute 'tk' for lab5q1
        # TODO: we need to fix this in the future. Maybe we should capture these error? 

        # this may be incomplete because we need to find a way to fix the guessed number
        # (app, root) = x.setup_gui(tk, fn)
        # time.sleep(2)
        # self.insert_into_entry(app.win, 40)
        # self.invoke_element(app.win, app._guess_btn)
        # str = self.get_text_from_scrolled_text(app.win)
        # print(f"str is '{str}'")
        # assert " is not a whole number\n\n" == str, f"well"        
        # x.clear_gui(app.win, root)

        #change - q1s
        for test in self._test_cases:
            with patch('random.randint', return_value=50):
                (app, root) = x.setup_gui(tk, fn)
                time.sleep(2)
                number1 = "seven"#40
                self.insert_into_entry(root, number1)
                self.invoke_element(root)
                str1 = self.get_text_from_scrolled_text(root)
                # print(f"str is '{str}'")
                x.grading_with_string_comparison2((test[0], str1))
                
                number = 40
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str2 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[1], str2))

                number = 90
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str3 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[2], str3))

                number = 50
                self.insert_into_entry(root, number)
                self.invoke_element(root)
                str4 = self.get_text_from_scrolled_text(root)
                x.grading_with_string_comparison2((test[3], str4))

                x.clear_gui(app, root)

    
    def check(self, fn):
        self.check_testbook(fn)