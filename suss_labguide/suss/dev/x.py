# X is the utility tools of `suss` package of iLabGuides
# iLabGuides contains a set of jupyter notebooks and a python package called `suss`
import re
import os
import io
import csv
import sys
import yaml
import socket
import difflib
import nbformat
import platform
from pprint import pprint
from termcolor import colored
from IPython.display import display
from learntools.core.richtext import *
from contextlib import redirect_stdout
import filecmp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# These colour lambdas are required for string comparison in the grading function
red = lambda text: f"<span style=\"color:black; background-color:#f4cec6; border-style: dashed; border-color: red; border-width: thin;\">{text}</span>"
green = lambda text: f"<span style=\"color:black; background-color:#C7F5C7; border-style: dashed; border-color: green; border-width: thin;\">{text}</span>"
blue = lambda text: f"<span style=\"color:blue;   background-color: black;\">{text}</span>"
white = lambda text: f"<span>{text}</span>"

def checking_origin():
    # this will check if the platform is an approved origin. If it is not, say so.
    # if it is, say so. 
    print("Vocareum")
    
# allow logging to every aspect of ilabguide. 
# allow switching off log when we are not doing development or when we are doing testing
def log(str, colour=None):
    config_file = ".config.yml"
    config_data = query_config(config_file)
    if check_key_in_yaml(config_file, "debug") == True and config_data["debug"] == True \
        and check_key_in_yaml(config_file, "env") == True and config_data["env"] != "production":
        if colour is not None:
            display(RichText("<b>"+str+"</b>", color=colour))
        else: 
            pprint(str)
            
def is_internet_down():
    print("Checking internet connection...")
    try:
        # Attempt to connect to a well-known internet host (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        # may want to check two more DNS servers to ensure accuracy
        print("Internet is up")
        return False  # Internet is up
    except OSError:
        print("Internet is down")
        return True   # Internet is down

# update_url_in_code(code, new_url, variable_name) #trigger  #Q1
# update_url_in_code(code, new_url, variable_name, None) # Q2

def update_url_in_code(code, new_url, variable_name, class_name="Request"):
    if class_name is None:
        # Create a regular expression pattern to find the entire line containing the variable assignment
        pattern = re.compile(rf"^{variable_name}\s*=\s*['\"].*?['\"]", re.MULTILINE)

        # Use regular expression to find and replace the entire line
        updated_code = pattern.sub(f'{variable_name} = "{new_url}"', code)

    else:
        # Create a regular expression pattern to match lines containing the specified variable and 'Request'
        pattern = re.compile(rf"^{variable_name}\s*=\s*{class_name}\(.*?\)", re.MULTILINE)

        # Use regular expression to find and replace the URL, wrapping it with the specified class
        updated_code = pattern.sub(f'{variable_name} = {class_name}(\'{new_url}\')', code)

    return updated_code

def update_date_in_code(text, new_date):
    # Define a regular expression pattern to match date='yyyy-mm-dd'
    date_pattern = r"date=['\"](\d{4}-\d{2}-\d{2})['\"]"
    
    # Use re.sub() to replace matched date patterns with the new date
    updated_text = re.sub(date_pattern, f"date='{new_date}'", text)
    
    return updated_text

def update_csv_in_code(code, new_csv, variable_name):
    # Create a regular expression pattern to find the entire line containing the variable assignment
    pattern = re.compile(rf"{variable_name}\s*=\s*pd\.read_csv\(['\"]([^'\"]+)['\"]\)", re.MULTILINE)

    # Use regular expression to find and replace the entire line
    updated_code = pattern.sub(f"{variable_name} = pd.read_csv('{new_csv}')", code)

    return updated_code

# below 2 update_<something>_in_code functions are required for ANL588

def update_x_in_code(code, x, new_x):
    # Update the regular expression pattern to specifically match 'x' with word boundaries
    pattern_with_word_boundaries = re.compile(rf"\b{re.escape(x)}\b")
    
    # Update the regular expression pattern to specifically match 'x' without word boundaries
    pattern_without_word_boundaries = re.compile(re.escape(x))
    
    # Use pattern_with_word_boundaries.sub to replace occurrences of 'x' with 'new_x'
    updated_code = pattern_with_word_boundaries.sub(new_x, code)
    
    # If pattern_with_word_boundaries.sub didn't result in any changes, try pattern_without_word_boundaries.sub
    if updated_code == code:
        updated_code = pattern_without_word_boundaries.sub(new_x, code)
    
    return updated_code

def update_list_in_code(code, old_list, new_list):
    # Convert lists to strings
    if all(isinstance(item, str) for item in old_list):
        old_list_str = ', '.join([f'"{item}"' for item in old_list])
    else:
        old_list_str = str(old_list)
    
    if all(isinstance(item, str) for item in new_list):
        new_list_str = ', '.join([f'"{item}"' for item in new_list])
    else:
        new_list_str = str(new_list)

    # Escape special characters in the old list string
    escaped_old_list = re.escape(old_list_str)

    # Compile regex pattern to find old list occurrences
    pattern = re.compile(escaped_old_list)

    # Replace old list occurrences with new list
    updated_code = pattern.sub(new_list_str, code)

    # Check if the pattern was found
    if updated_code == code:
        # If pattern not found, search for alternative pattern that is without space
        old_list_str2 = ','.join([f'"{item}"' for item in old_list])
        escaped_old_list2 = re.escape(old_list_str2)
        pattern2 = re.compile(escaped_old_list2)
        updated_code = pattern2.sub(new_list_str, code)

    return updated_code

# ICT 162        
def test_through_every_layers(app, root, appwin):
    log("this is app")
    scan_through_every_layers(app)
    log("-----")
    log("this is root")
    scan_through_every_layers(root)
    log("-----")
    log("this is app.win")
    scan_through_every_layers(appwin)
    log("-----")

# required for ICT162
def scan_through_every_layers(app):
    for child in app.winfo_children():
        log(child.winfo_children())
        for grandchild in child.winfo_children():
            log(grandchild.winfo_children())

def setup_gui3(tk,fn):
    win = tk.Tk()
    app = fn(win)
    app.pack()
    # app.grid()
    app.update()
    # win.mainloop()
    return app, win

# required for ICT162
def setup_gui(tk, fn):
    root = tk.Tk()
    app = fn(root)
    # app.pack()
    # change - to fix q1
    app.grid()
    app.update()
    return app, root

def this_is_mac():
    if platform.system() == 'Darwin':
        return True
    else:
        return False

# Required for ict162 lab5
def clear_gui(app, root):
    # to fix the crashing kernel and the update issue after app is destroyed
    if app is not None:
        app.destroy()
        app.update()
        
    if root is not None:
        root.destroy()
        if this_is_mac() == True: # required to work on ubuntu + mac
            root.update()

    # app.destroy()
    # root.destroy()
    # app.update()
    # root.update()

# Usage: x.find_cell("lab6q1a", 10)
# it will print out every cell with its cell number and the first line of the cell  
def show_every_cells_of_notebook(notebook_name, max_range):
    with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    for i in range(min(max_range, len(nb["cells"]))):
        str = nb["cells"][i]["source"].split("\n")[0]
        log(f'cell {i} - {str}')
    log("-----end-of-find-cell----")

def show_ten_cells_around_this_cell(notebook_name, cell_index):
    with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    start_index = max(0, cell_index - 5)
    end_index = min(len(nb["cells"]), cell_index + 6)

    for i in range(start_index, end_index):
        if i >= 0:        
            cell_source = nb["cells"][i]["source"].split("\n")[0]
            arrow = "->" if i == cell_index else "  "
            line = f'{arrow} Cell {i} - {cell_source}'
            if i == cell_index:
                line = colored(line, "red")
            log(line)
            
    log("-----end-of-find-cell----")

def show_twenty_cells_around_this_cell(notebook_name, cell_index):
    with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    log("-----cell_index----")
    log(cell_index)
    log(type(cell_index))
    start_index = max(0, cell_index - 10)
    end_index = min(len(nb["cells"]), cell_index + 11)

    for i in range(start_index, end_index):
        if i >= 0:
            
            cell_source = nb["cells"][i]["source"].split("\n")[0]
            arrow = "->" if i == cell_index else "  "
            line = f'{arrow} Cell {i} - {cell_source}'
            if i == cell_index:
                line = colored(line, "red")
            log(line)

    log("-----end-of-find-cell----")
    
    
def get_source_code(notebook_name, cell_idx=None, what_to_find=None):    
    try:
        nb = ""
        with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)
            
        # Get the source code of a cell
        cell_source = nb["cells"][cell_idx]["source"]
        
        # Split the source code into lines
        # lines = cell_source.splitlines()
        desired_content = cell_source # default is the whole cell content``
        # # Find the line numbers of the start and end indices
        # end_line = None
        # for i, line in enumerate(lines):
        #     try:
        #         if "DO NOT REMOVE" in line:
        #             end_line = i - 1  # Subtract 1 to exclude the end line itself
        #     except Exception as e:
        #         pprint("The line `# DO NOT REMOVE this comment.` is not found in the cell. Please add it back to the cell where it was previously.")
        #         break
        
        # # Retrieve the desired portion of the cell content
        # desired_content = "\n"+ "\n".join(lines[0:end_line + 1]) +"\n"
        # test_for_none_162(desired_content, notebook_name, cell_idx, what_to_find)
        
        return desired_content
    except Exception as e:
        # capture the exception when the cell_idx is wrong
        show_twenty_cells_around_this_cell(notebook_name, cell_idx)
        raise Exception(f"At cell {cell_idx}, iLabGuide fails to find one or some of the following class(es): {what_to_find}")

def get_multiple_cell_source(notebook_name, cell_idx=None):
    cell_numbers = cell_idx
    previous = ""
    for item in cell_numbers: 
        current = get_source_code(notebook_name, item)
        previous = previous + "\n" + current
    return previous

def get_all_source_code(notebook_name):
    try:
        nb = ""
        with open(f"{notebook_name}.ipynb", "r", encoding="utf-8") as f:
            nb = nbformat.read(f, nbformat.NO_CONVERT)

        all_cell_contents = []  # Create a list to store cell contents

        for cell in nb["cells"]:
            if cell.cell_type == "code":
                cell_source = cell["source"]
                all_cell_contents.append(cell_source)

        # Join all cell contents into a single string with line breaks
        all_contents = "\n".join(all_cell_contents)

        return all_contents
    except Exception as e:
        raise Exception(f"An error occurred while extracting cell contents from the notebook: {str(e)}")

def get_question_source(source, question_number):
    
    question_source = []  # Use a list to store the lines

    lines = source.split('\n')
    capturing = False
    # the following can only capture 1st question and 2nd question source codes of the lab. subsequent questions will always include 2nd question codes as well
    for line in lines:
        if capturing and f"{question_number}.check()" in line:
            capturing = False
            break
        if capturing:
            question_source.append(line)
        if question_number == "q1" or question_number == "q1.a":
            if line.strip().startswith('# write your answer here'):
                capturing = True
        elif line.strip().endswith(".solution()"):
                capturing = True

    result = '\n'.join(question_source)
    return result

def get_question_source2(source, question_number):
    
    question_source = []  # Use a list to store the lines

    lines = source.split('\n')
    capturing = False
    # the following can only capture 1st question and 2nd question source codes of the lab. subsequent questions will always include 2nd question codes as well
    for line in lines:
        if capturing and f"{question_number}.check()" in line:
            capturing = False
            break
        if capturing:
            question_source.append(line)
        if line.strip().startswith(f'# Answer to {question_number}'):
                capturing = True

    result = '\n'.join(question_source)
    return result

def filter_source(source, what_to_filter):
    lines = source.split('\n')
    filtered_lines = [
        line.split('#')[0].rstrip() if '#' in line else line 
        for line in lines 
        if line.strip() and not line.lstrip().startswith(what_to_filter)
    ]
    updated_source = '\n'.join(filtered_lines)
    return updated_source


def test_for_none_162(desired_content, notebook_name, cell_idx, what_to_find):
    try:
        individual_cell_number = ""
        if isinstance(what_to_find, list):
            # there are multiple objects
            objects = create_many_objects_from_source_code(desired_content, what_to_find)                
            cell_numbers = cell_idx.split(",")
                        
            for index, item in enumerate(what_to_find):
                # when the number of cell numbers is less than the number of objects
                if len(cell_numbers) -1 > index:
                    individual_cell_number = int(cell_numbers[index])
                else: # when there is only one cell number, take the last item
                    individual_cell_number = int(cell_numbers[-1])
                    
                a = type(objects[f'{item}'])
                if a == type(None):
                    show_twenty_cells_around_this_cell(notebook_name, individual_cell_number)
                    raise Exception(f"At cell {individual_cell_number}, iLabGuide fails to find one or some of the following class(es): {item}.<br> Note: It may detect just {item} above, but there are {what_to_find} to check.")
        else:
            #create a single object
            obj = create_object_from_source_code(desired_content, what_to_find) 
            a = type(obj)
            if a == type(None):
                show_twenty_cells_around_this_cell(notebook_name, cell_idx)
                raise Exception(f"At cell {cell_idx}, iLabGuide fails to find one or some of the following class(es): {what_to_find}. <br>")
            
    except Exception as e:
        # log("-------")
        # log(individual_cell_number)
        show_twenty_cells_around_this_cell(notebook_name, individual_cell_number)
        raise Exception(f"At cell {individual_cell_number}, iLabGuide fails to find one or some of the following class(es): {item}.<br>1) There may be one or more calling function(s) at cell {individual_cell_number}. Please remove or comment them.<br>2) There may be one or more calling function(s) inside dependent cell before cell {individual_cell_number}. Please remove or comment them.")

def test_for_none_233(desired_content, notebook_name, cell_idx, value=None, var=None):
    try:
        # individual_cell_number = ""
        if var == "url":
            updated_source = update_url_in_code(desired_content, value, "url", class_name=None)
        elif var == "req":
            updated_source = update_url_in_code(desired_content, value, "req")
        elif var == "date":
            updated_source = update_date_in_code(desired_content, value)
        elif var == "phone_data":
            updated_source = update_csv_in_code(desired_content, value, "phone_data")

        if updated_source == desired_content:
            show_twenty_cells_around_this_cell(notebook_name, cell_idx)
            raise Exception(f"At cell {cell_idx}, iLabGuide fails to find the following variable: `{var}` There may be a different name for the variable or there is no variable defined in {cell_idx}. \n Please define your variable as `{var}`.")
            
    except Exception as e:
        # log("-------")
        # log(individual_cell_number)
        show_twenty_cells_around_this_cell(notebook_name, cell_idx)
        raise Exception(f"At cell {cell_idx}, iLabGuide fails to find the following variable: `{var}`. There may be a different name for the variable or there is no variable defined in {cell_idx}. \n Please define your variable as `{var}`.")

def test_for_none_588(desired_content, notebook_name, cell_idx, value, new_value, what_to_find, var=None):
    try:
        # individual_cell_number = ""
        if var == "list":
            updated_source = update_list_in_code(desired_content, value, new_value)
        elif var == "csv":
            updated_source = update_csv_in_code(desired_content, value, what_to_find)
        else:
            updated_source = update_x_in_code(desired_content, value, new_value)

        if updated_source == desired_content:
            show_twenty_cells_around_this_cell(notebook_name, cell_idx)
            raise Exception(f"At cell {cell_idx}, iLabGuide fails to find the following: `{what_to_find}` There may be an incorrect definition of the variable in {cell_idx}. \n Please check that `{what_to_find}` is defined.")
            
    except Exception as e:
        # log("-------")
        # log(individual_cell_number)
        show_twenty_cells_around_this_cell(notebook_name, cell_idx)
        raise Exception(f"At cell {cell_idx}, iLabGuide fails to find the following: `{what_to_find}` There may be an incorrect definition of the variable in {cell_idx}. \n Please check that `{what_to_find}` is defined.")


def print_current_location(text=None):
    log(f"--- {text} ---")
    current_file = os.path.abspath(__file__)
    current_module = __name__
    log("Current file:", current_file)
    log("Current module:", current_module)

# create multiple objects from source code within one namespace. This is required for inherited classes
def create_many_objects_from_source_code(source_code, object_names):
    namespace = {} 
    try:
        # Execute the source code in the namespace
        # the namespace is being filled despite the error has been thrown
        exec(source_code, namespace)
        multiple_objs = {obj_name: namespace.get(obj_name) for obj_name in object_names}
    except Exception as e:
        try: 
            # incase error like name 'q1' is not defined happens
            # error does not mean the namespace is not created. In fact, the namespace is in there. 
            multiple_objs = {obj_name: namespace.get(obj_name) for obj_name in object_names}
        except Exception as e:
            return None

        return multiple_objs
    return multiple_objs

def create_object_from_source_code(source_code, object_name):
    # Create a new namespace for the object/class
    namespace = {}
    try:
        # Execute the source code in the namespace
        # the namespace is being filled despite the error has been thrown
        exec(source_code, namespace)
        # Get the object/class from the namespace (assuming it was defined in the code)
        obj = namespace.get(object_name)
    except Exception as e:
        try: 
            # incase error like name 'q1' is not defined happens
            # error does not mean the namespace is not created. In fact, the namespace is in there. 
            # log(e)
            obj = namespace.get(object_name)
        except Exception as e:
            # log("do nothing")
            return None
        return obj
    return obj

def get_object_from_lab(notebook_name, cell_idx, object_name):
    #1
    source_code = get_source_code(notebook_name, cell_idx, object_name)
    #2 
    test_for_none_162(source_code, notebook_name, str(cell_idx), change_to_list(object_name))
    #3
    obj = create_object_from_source_code(source_code, object_name)
    return obj

def change_to_list(element):
    if ',' in element:
        return element.split(',')
    else:
        return [element]

def get_edits_string(old, new):
    if old is None or new is None:
        return ""
    
    result = ""
    codes = difflib.SequenceMatcher(a=old, b=new).get_opcodes()
    for code in codes:
        if code[0] == "equal": 
            result += white(old[code[1]:code[2]])
        elif code[0] == "delete":
            result += red(old[code[1]:code[2]])
        elif code[0] == "insert":
            result += green(new[code[3]:code[4]])
        elif code[0] == "replace":
            result += (red(old[code[1]:code[2]]) + green(new[code[3]:code[4]]))
    return result

def print_comparison(original, output):
    log("--original--")
    log(original)
    log("--output--")
    log(output)

# we may want to rewrite the incorrect statement. currently only specific to class.
def justfail(args, msg=None):
    if msg is None:
        assert 1 == 2, ("""The attribute `{}` is not defined in the class `{}`.""").format(args[0], args[1])
    else:
        assert 1 == 2, (f"""{msg}""")

def justpass():
    assert 1==1

# should i have a parameter and cause this to be a super big function?
# can we standardise the grading to always have at most five args
# input
# expected
# type 
# out
# type

# TODO note that this determines the best method moving forward.
# However there may be unknowns with `determine_the_grading_method` function
def determine_the_grading_method(args, para=None):
    if type(args[1]) == str:
        if type(args[2]).__name__ == "method":
            grading_string_comparison_with_context(args, para)
        else:
            grading_with_string_comparison(args)
    elif type(args[2]).__name__ == "method":
        grading_with_checking_class_method(args)
    elif type(args[1]).__name__ == "DataFrame":
        grading_df(args)
    else: 
    # there are 9 datatypes, we discussed this. we may face future errors.
    # elif type(args[1]) == float or int:
        grading(args)

def grading_with_assertion(assertion, args):
    """Grading Functionalities"""
    assert assertion, ("""
Using the test value of `{}` as input(s), the expected print statement should be:
<pre>{}</pre>
({})

but got the following statement instead:
<pre>{}</pre>
({})
                       
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))


def grading_return_value(args):
    """Grading Functionalities"""
    assert args[1] == args[2], ("""
Using the test value of `{}` as input(s), the expected return value should be:
<pre>{}</pre>
({})

but got the following return value instead:
<pre>{}</pre>
({})
                                
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))


def grading_with_string_comparison(args):
    """Grading Functionalities"""
    if callable(args[2]):
        assert args[1] == args[2](), ("""
Using the test value of `{}` as input(s), the expected print statement should be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2](), type(args[2]()).__name__, get_edits_string(args[1], args[2]()))
    else:
        assert args[1] == args[2], ("""
Using the test value of `{}` as input(s), the expected print statement should be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(args[1], args[2]))

def grading_with_string_comparison2(args):
    """Grading Functionalities"""
    if callable(args[1]):
        assert args[0] == args[1](), ("""
iLabGuide expects the print statement to be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], type(args[0]).__name__, args[1](), type(args[1]()).__name__, get_edits_string(args[0], args[1]))
    else:
        assert args[0] == args[1], ("""
iLabGuide expects the print statement to be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], type(args[0]).__name__, args[1], type(args[1]).__name__, get_edits_string(args[0], args[1]))
          
# TODO: Should we reserve this to be only for String comparison? if one of the datatype is not string, do not show the diff
def grading_string_comparison_with_context(args, para=None):
    class_name = args[2].__self__.__class__.__qualname__.split(".")[-1]
    if para is None:
        assert args[1] == args[2](), ("""
Checking method: `{}.{}`

Using the test value of `{}` as input(s), the expected print statement should be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(class_name, args[2].__name__, args[0], args[1], type(args[1]).__name__, args[2](), type((args[2]())).__name__, get_edits_string(args[1], args[2]()))
    else:
        assert args[1] == str(args[2](para)), ("""
Checking method: `{}.{}`

Using the test value of `{}` as input(s), the expected value should be:
<pre>{}</pre>
({})

but got the following value instead:
<pre>{}</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(class_name, args[2].__name__, args[0], args[1], type(args[1]).__name__, str(args[2](para)), type(str(args[2](para))).__name__, get_edits_string(args[1], str(args[2](para))))

def grading(args):
    """Grading Functionalities"""
    assert args[1] == args[2], ("""
Using the test value of `{}` as input(s), the expected return value should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))

def grading_lists_in_csv(args):
    """Grading Functionalities"""
    assert args[1] == args[2], ("""
The expected values in `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))

def grading_df(args):
    """Grading Functionalities"""
    assert args[1].equals(args[2]), ("""
The expected Dataframe for `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], type(args[1]).__name__, args[2], type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))

def grading_with_checking_class_method(args):
    class_name = args[2].__self__.__class__.__qualname__.split(".")[-1]
    """Grading Functionalities"""
    assert args[1] == args[2](), ("""
Checking method: `{}.{}` 

Using the test value of `{}` as input(s), the expected output should be:
<pre>`{}`</pre>
({})

but got the following statement instead:
<pre>`{}`</pre>
({})
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(class_name, args[2].__name__, args[0], args[1], type(args[1]).__name__, args[2](), type((args[2]())).__name__, get_edits_string(str(args[1]), str(args[2]())))

def grading_nparray(args):
    assert np.array_equal(args[2], args[3]), ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
""").format(args[0], args[1], str(args[2]), type(args[2]).__name__, str(args[3]), type(args[3]).__name__)

def grading_nparray2(args, var=None):
    if var is None:
        assert np.array_equal(args[1], args[2]), ("""
The expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                  
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], str(args[1]), type(args[1]).__name__, str(args[2]), type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))
    elif var == "test":
        assert np.array_equal(args[2], args[3]), ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                  
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], str(args[2]), type(args[2]).__name__, str(args[3]), type(args[3]).__name__, get_edits_string(str(args[2]), str(args[3])))

def grading_npallclose(args, var=None):
    if var is None:
        assert np.allclose(args[1], args[2], atol=1e-10), ("""
The expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                           
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>                                                           
""").format(args[0], str(args[1]), type(args[1]).__name__, str(args[2]), type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))
    elif var == "test":
        assert np.allclose(args[2], args[3], atol=1e-10), ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                              
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], str(args[2]), str(args[3]), get_edits_string(str(args[2]), str(args[3])))

def grading_npisclose(args, var=None):
    if var is None:
        assert np.isclose(args[1], args[2], atol=1e-10), ("""
The expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                          
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], str(args[1]), type(args[1]).__name__, str(args[2]), type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))
    elif var == "test":
        assert np.isclose(args[2], args[3], atol=1e-10), ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                              
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], str(args[2]), str(args[3]), get_edits_string(str(args[2]), str(args[3])))
        

# grading_equal can be used for lists, or any assertion using `==`
def grading_equal(args, var=None):
    if var is None:
        assert args[1] == args[2], ("""
The expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], str(args[1]), type(args[1]).__name__, str(args[2]), type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))
    elif var == "test":
        assert args[2] == args[3], ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                  
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], str(args[2]), type(args[2]).__name__, str(args[3]), type(args[3]).__name__, get_edits_string(str(args[2]), str(args[3])))
        
def grading_df_series(args, var=None):
    if var is None:
        assert args[1].equals(args[2]), ("""
The expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                         
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], str(args[1]), type(args[1]).__name__, str(args[2]), type(args[2]).__name__, get_edits_string(str(args[1]), str(args[2])))
    elif var == "test":
        assert args[2].equals(args[3]), ("""
Using the test value of `{}` as input(s), the expected `{}` should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                  
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(args[0], args[1], str(args[2]), type(args[2]).__name__, str(args[3]), type(args[3]).__name__, get_edits_string(str(args[2]), str(args[3])))


def grading_param_attrs(args, var=None):
    
    if var is None:
        expected = args[1]
        actual = args[2]
        differing_items = {}
        for attr in actual:
            if actual[attr] != expected[attr]:
                differing_items[attr] = (actual[attr], expected[attr])

        assert actual == expected, '\n'.join([
"""The expected value of the {} `{}` should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style="font:bold">"{}</span></pre>""".format(args[0], attr, expected_value, actual_value, get_edits_string(str(expected_value), str(actual_value)))
    for attr, (actual_value, expected_value) in differing_items.items()
])

    elif var == "test":
        expected = args[2]
        actual = args[3]
        
        assert actual == expected, '\n'.join([
"""Using the value of `{}` as test input, the expected value of the {} `{}` should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style="font:bold">"{}</span></pre>""".format(args[0], args[1], attr, expected_value, actual_value, get_edits_string(str(expected_value), str(actual_value)))
    for attr, (actual_value, expected_value) in differing_items.items()
])

def get_x_y_data_from_plt(arg):
    scatter_plot = None
    for item in arg.get_children():
        if isinstance(item, plt.Axes):
            for artist in item.get_children():
                if isinstance(artist, matplotlib.collections.PathCollection):
                    scatter_plot = artist
                    break

    # Access the data points used in the scatter plot
    if scatter_plot:
        x_data = scatter_plot.get_offsets()[:, 0]
        y_data = scatter_plot.get_offsets()[:, 1]
        # print("X data:", x_data)
        # print("Y data:", y_data)
    else:
        print("Scatter plot not found on axes1")
    
    return x_data, y_data
    
def grading_plt_figure(actual, expected):
    actual_axes = actual.get_axes()[0]
    expected_axes = expected.get_axes()[0]

    actual_position = actual_axes.get_position()
    expected_position = expected_axes.get_position()

    actual_size = actual_axes.get_position().size
    expected_size = expected_axes.get_position().size
    
    # tolerance is suggested by chatGPT as the position and sizes above are the same yet assert fails due to minor tolerance difference

    # Define a tolerance value (adjust as needed)
    tolerance = 1e-6  # You can adjust the tolerance as needed

    # Compare positions and sizes with tolerance
    assert actual.get_axes()[0].get_title() == expected.get_axes()[0].get_title(), ("""
The Title is incorrect. Expected the title to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected.get_axes()[0].get_title()), str(actual.get_axes()[0].get_title()), get_edits_string(str(expected.get_axes()[0].get_title()), str(actual.get_axes()[0].get_title())))
    assert actual.get_axes()[0].get_xlabel() == expected.get_axes()[0].get_xlabel(), ("""
The X label is incorrect. Expected the X label to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected.get_axes()[0].get_xlabel()), str(actual.get_axes()[0].get_xlabel()), get_edits_string(str(expected.get_axes()[0].get_xlabel()), str(actual.get_axes()[0].get_xlabel())))
    assert actual.get_axes()[0].get_ylabel() == expected.get_axes()[0].get_ylabel(), ("""
The Y label is incorrect. Expected the Y label to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected.get_axes()[0].get_ylabel()), str(actual.get_axes()[0].get_ylabel()), get_edits_string(str(expected.get_axes()[0].get_ylabel()), str(actual.get_axes()[0].get_ylabel())))
    assert (np.allclose(actual_position, expected_position, atol=tolerance)), ("""
The axes position is incorrect. Please check the `add_subplot()` method. 

Expected the position to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_position), str(actual_position), get_edits_string(str(expected_position), str(actual_position)))
    assert (np.allclose(actual_size, expected_size, atol=tolerance)),("""
The axes size is incorrect. Please check the `add_subplot()` method. 

Expected the size to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_size), str(actual_size), get_edits_string(str(expected_size), str(actual_size)))
    
from matplotlib import collections as mc 
# TODO: grading_anl588_x incorrect statements for when test cases are tested in the question e.g. q2.py is not clear that the incorrect is due to test case
def grading_anl588_seaborn_kdeplot(args):

    collections = args[0].collections

    # assert fill = True
    assert any(isinstance(collection, mc.PolyCollection)for collection in collections), "The option `fill = True` is not used."
    # assert use of sns.despine()
    spines = args[0].spines
    assert spines['top'].get_visible() == False, "Top spine is visible, sns.despine() not called."
    assert spines['right'].get_visible() == False, "Right spine is visible, sns.despine() not called."

    if collections:
        for collection in collections:
            # we are looking for PolyCollection to get facecolor
            if isinstance(collection, mc.PolyCollection):
                actual_fill = collection.get_facecolor().tolist()[0]
                paths = collection.get_paths()
                for path in paths:
                    vertices = path.vertices
                    x_data = vertices[:, 0]
                    y_data = vertices[:, 1]
        
    actual_title = args[0].get_title()

    # Get expected ax1
    # expected_fig, expected_ax = Question2.produce_expected("Population")
    expected_collections = args[1].collections

    if expected_collections:
        for collection in expected_collections:
            if isinstance(collection, mc.PolyCollection):
                expected_fill = collection.get_facecolor().tolist()[0]
                paths = collection.get_paths()
                for path in paths:
                    vertices = path.vertices
                    expected_x_data = vertices[:, 0]
                    expected_y_data = vertices[:, 1]

    
    expected_title = args[1].get_title()
    
    # asserting color
    assert actual_fill == expected_fill, ("""
The expected `{}` of the kdeplot should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("color", str(expected_fill), str(actual_fill), get_edits_string(str(expected_fill), str(actual_fill)))

    # assert title
    assert actual_title == expected_title, ("""
The expected `{}` of the kdeplot should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("title", str(expected_title), str(actual_title), get_edits_string(str(expected_title), str(actual_title)))
    # assert x and y data
    assert np.allclose(expected_x_data, x_data), ("""
The expected `{}` of the kdeplot should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("x data", str(expected_x_data), type(expected_x_data).__name__, str(x_data), type(x_data).__name__, get_edits_string(str(expected_x_data), str(x_data)))

    assert np.allclose(expected_y_data, y_data), ("""
The expected `{}` of the kdeplot should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("y data", str(expected_y_data), type(expected_y_data).__name__, str(y_data), type(y_data).__name__, get_edits_string(str(expected_y_data), str(y_data)))

def grading_anl588_seaborn_pairplot(args):
        
    # check if there is hue option used
    assert hasattr(args[0], "_legend"), ("The hue option is not used.")
    
    # assert hue
    actual_hue = args[0]._legend.get_title().get_text()
    expected_hue = args[1]._legend.get_title().get_text()
    assert actual_hue == expected_hue, ("""
The expected `{}` of the pairplot should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                        
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("hue", str(expected_hue), str(actual_hue), get_edits_string(str(expected_hue), str(actual_hue)))
    
    
    # Pairplots x_vars and y_vars are the same values
    actual_x_vars = args[0].x_vars
    expected_x_vars = args[1].x_vars

    
    # assert vars
    # do we want to check if the order of the variables are correct? (use set() to compare if yes) : technically, yes we need to check the order. However, ordering them wrong will produce an incorrect for the assertion below. So no additional check is needed.
    assert expected_x_vars == actual_x_vars, ("""
The expected `{}` of the pairplot should be:
<pre>`{}`</pre>
({})

but got the following instead:
<pre>`{}`</pre>
({})
                                                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("vars", str(expected_x_vars), type(expected_x_vars).__name__, str(actual_x_vars), type(actual_x_vars).__name__, get_edits_string(str(expected_x_vars), str(actual_x_vars)))

    actual_data = args[0].data
    expected_data = args[1].data

    # assert data
    grading_df_series(("data", actual_data, expected_data))

def grading_anl588_seaborn_histplot(args):
        
        actual_data = []
        for patch in args[0].patches:
            height = patch.get_height()
            left = patch.get_x()
            width = patch.get_width()
            actual_data.append((left, left + width, height))
        
        expected_data = []
        for patch in args[1].patches:
            height = patch.get_height()
            left = patch.get_x()
            width = patch.get_width()
            expected_data.append((left, left + width, height))
        
        
        # Assert x-axis
        assert args[1].get_xlabel() == args[0].get_xlabel(), ("""
The expected `{}` of the histplot should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("x-axis", str(args[1].get_xlabel()), str(args[0].get_xlabel()), get_edits_string(str(args[1].get_xlabel()), str(args[0].get_xlabel())))
        
        # check if there is hue option used
        assert args[0].get_legend() is not None, "The hue option is not used."
        
        # assert hue
        actual_hue = args[0].get_legend().get_title().get_text()
        expected_hue = args[1].get_legend().get_title().get_text()  
        assert actual_hue == expected_hue, ("""
The expected `{}` of the histplot should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format("hue", str(expected_hue), str(actual_hue), get_edits_string(str(expected_hue), str(actual_hue)))
        
        # assert data
        # shifted assert data to be the final check. if x_label or hue is incorrect, then data assertion will always fail (if it is the first check)
        assert len(actual_data) == len(expected_data), ("""Data lengths are different. The expected data length should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(len(expected_data)), str(len(actual_data)), get_edits_string(str(len(expected_data)), str(len(actual_data))))
        
        for i, (actual_bin, expected_bin) in enumerate(zip(actual_data, expected_data)):
            assert actual_bin == expected_bin, ("""Bin {} is different. The expected Bin {} should be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>
                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(i, i, str(expected_bin), str(actual_bin), get_edits_string(str(expected_bin), str(actual_bin)))

def grading_anl588_seaborn_scatterplot(actual_axes, expected_axes, tolerance=1e-6):
    actual_x_data = actual_axes.collections[0].get_offsets()[:, 0]
    actual_y_data = actual_axes.collections[0].get_offsets()[:, 1]

    expected_x_data = expected_axes.collections[0].get_offsets()[:, 0]
    expected_y_data = expected_axes.collections[0].get_offsets()[:, 1]

    actual_position = actual_axes.get_position()
    expected_position = expected_axes.get_position()

    actual_size = actual_position.size
    expected_size = expected_position.size

    actual_xticks = actual_axes.get_xticks()
    expected_xticks = expected_axes.get_xticks()

    actual_yticks = actual_axes.get_yticks()
    expected_yticks = expected_axes.get_yticks()

    actual_xlim = actual_axes.get_xlim()
    expected_xlim = expected_axes.get_xlim()

    actual_ylim = actual_axes.get_ylim()
    expected_ylim = expected_axes.get_ylim()

    # asserting x and y data
    assert np.allclose(actual_x_data, expected_x_data, atol=tolerance), ("""
The `x data` is incorrect.
                                                                         
Expected the `x data` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_x_data), str(actual_x_data), get_edits_string(str(expected_x_data), str(actual_x_data)))
    
    assert np.allclose(actual_y_data, expected_y_data, atol=tolerance), ("""
The `y data` is incorrect.
                                                                         
Expected the `y data` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_y_data), str(actual_y_data), get_edits_string(str(expected_y_data), str(actual_y_data)))
    
    # asserting title
    assert actual_axes.get_title() == expected_axes.get_title(), ("""
The Title is incorrect. Expected the title to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_axes.get_title()), str(actual_axes.get_title()), get_edits_string(str(expected_axes.get_title()), str(actual_axes.get_title())))

    # asserting x label
    assert actual_axes.get_xlabel() == expected_axes.get_xlabel(), ("""
The `x label` is incorrect. Expected the x label to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_axes.get_xlabel()), str(actual_axes.get_xlabel()), get_edits_string(str(expected_axes.get_xlabel()), str(actual_axes.get_xlabel())))

    # asserting y label
    assert actual_axes.get_ylabel() == expected_axes.get_ylabel(), ("""
The `y label` is incorrect. Expected the Y label to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_axes.get_ylabel()), str(actual_axes.get_ylabel()), get_edits_string(str(expected_axes.get_ylabel()), str(actual_axes.get_ylabel())))

    # assert ticks
    assert np.array_equal(actual_xticks, expected_xticks), ("""
The `x ticks` are incorrect. Expected the `x ticks` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_xticks), str(actual_xticks), get_edits_string(str(expected_xticks), str(actual_xticks)))

    assert np.array_equal(actual_yticks, expected_yticks), ("""
The `y ticks` are incorrect. Expected the `y ticks` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_yticks), str(actual_yticks), get_edits_string(str(expected_yticks), str(actual_yticks)))
    
    # assert limits
    assert np.allclose(actual_xlim, expected_xlim, atol=tolerance), ("""
The `x limits` are incorrect. Expected the `x limits` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_xlim), str(actual_xlim), get_edits_string(str(expected_xlim), str(actual_xlim)))
    
    assert np.allclose(actual_ylim, expected_ylim, atol=tolerance), ("""
The `y limits` are incorrect. Expected the `y limits` to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_ylim), str(actual_ylim), get_edits_string(str(expected_ylim), str(actual_ylim)))


    # asserting the layout and appearance of the plot
    assert np.allclose(actual_position, expected_position, atol=tolerance), ("""
The axes position is incorrect. Please check the `add_subplot()` method. 

Expected the position to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_position), str(actual_position), get_edits_string(str(expected_position), str(actual_position)))

    assert np.allclose(actual_size, expected_size, atol=tolerance), ("""
The axes size is incorrect. Please check the `add_subplot()` method. 

Expected the size to be:
<pre>`{}`</pre>

but got the following instead:
<pre>`{}`</pre>

See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_size), str(actual_size), get_edits_string(str(expected_size), str(actual_size)))

def grading_anl588_seaborn_catplot(args, param=None):
        # Access the axes object
        actual_axes = args[0].ax 
        expected_axes = args[1].ax

        if not args[0]._legend or args[0]._legend.get_title().get_text() == "":
            justfail("hue", "The `hue` parameter is not used. Please use the `hue` parameter in the catplot function.")

        actual_hue = args[0]._legend.get_title().get_text()
        expected_hue = args[1]._legend.get_title().get_text()
        
        assert actual_hue == expected_hue, ("""
The hue parameter is incorrect. Expected the hue parameter to be:
<pre>`{}`</pre>
                                            
but got the following instead:
<pre>`{}`</pre>
                                            
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_hue), str(actual_hue), get_edits_string(str(expected_hue), str(actual_hue)))
        
        # Get the x-axis label
        actual_x_label = actual_axes.get_xlabel() if actual_axes.get_xlabel() else justfail("xlabel", "The `x-axis` label is not used. Please use the `x` parameter in the catplot function.")
        expected_x_label = expected_axes.get_xlabel()

        assert actual_x_label == expected_x_label, ("""
The `x-axis` label is incorrect. Expected the `x-axis` label to be:                                     
<pre>`{}`</pre>
                                                    
but got the following instead:
<pre>`{}`</pre>
                                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_x_label), str(actual_x_label), get_edits_string(str(expected_x_label), str(actual_x_label)))


        actual_kind = None
 
        for ax in args[0].axes.flat:
            if ax.get_children()[0].__class__.__name__ == 'Rectangle' and  ax.get_children()[0].get_width() == 0.4:
                actual_kind = 'count'
            elif ax.get_children()[0].__class__.__name__ == 'Rectangle' and ax.get_children()[0].get_width() != 0.4:
                actual_kind = 'bar'
            elif ax.get_children()[0].__class__.__name__ == 'PolyCollection':
                actual_kind = 'violin'
            elif ax.get_children()[0].__class__.__name__ == 'PathPatch':
                actual_kind = 'box'
            elif ax.get_children()[0].__class__.__name__ == 'PathCollection':
                actual_kind = 'strip'
            elif ax.get_children()[0].__class__.__name__ == 'PatchCollection':
                actual_kind = 'boxen'
            elif ax.get_children()[0].__class__.__name__ == 'Line2D':
                actual_kind = 'point'

        if actual_kind is None or 'strip' in actual_kind:
            justfail("kind = 'count'", "The `kind` parameter is not defined or `strip` is assigned to it. Please use the `kind` parameter and assign `count` to it in the catplot function.")


        expected_kind = None
        for ax in args[1].axes.flat:
            if ax.get_children()[0].__class__.__name__ == 'Rectangle' and  ax.get_children()[0].get_width() == 0.4:
                expected_kind = 'count'
            elif ax.get_children()[0].__class__.__name__ == 'Rectangle' and ax.get_children()[0].get_width() != 0.4:
                expected_kind = 'bar'
            elif ax.get_children()[0].__class__.__name__ == 'PolyCollection':
                expected_kind = 'violin'
            elif ax.get_children()[0].__class__.__name__ == 'PathPatch':
                expected_kind = 'box'
            elif ax.get_children()[0].__class__.__name__ == 'PathCollection':
                expected_kind = 'stripe'
            elif ax.get_children()[0].__class__.__name__ == 'PatchCollection':
                expected_kind = 'boxen'
            elif ax.get_children()[0].__class__.__name__ == 'Line2D':
                expected_kind = 'point'

        assert actual_kind == expected_kind, ("""
The `kind` parameter is incorrect. Expected the `kind` to be:                                     
<pre>`{}`</pre>
                                                    
but got the following instead:
<pre>`{}`</pre>
                                                    
See the difference:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(str(expected_kind), str(actual_kind), get_edits_string(str(expected_kind), str(actual_kind)))
                
        # Get the data
        # Direct data access is not possible through the catplot object directly
        # However, you can inspect the original DataFrame used for creating the plot
        actual_data = args[0].data
        expected_data = args[1].data

        grading_df_series(("data", actual_data, expected_data))
        if param == "alpha":
            # Get the alpha value
            actual_alpha = [p.get_alpha() for p in actual_axes.patches]
            actual_alpha = actual_alpha[0] 
            if actual_alpha is None:
                justfail("alpha", "The `alpha` parameter is not used. Please use the `alpha` parameter in the catplot function.")

            expected_alpha = [p.get_alpha() for p in expected_axes.patches][0]  # Assuming uniform alpha

            assert actual_alpha == expected_alpha, ("""
    The `alpha` parameter is incorrect. Expected the `alpha` parameter to be:
    <pre>`{}`</pre>
                                                    
    but got the following instead:
    <pre>`{}`</pre>
                                                    
    See the difference:
    <pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
    """).format(str(expected_alpha), str(actual_alpha), get_edits_string(str(expected_alpha), str(actual_alpha)))
        elif param == "palette":
            # Get the palette
            actual_palette = args[0].axes.flat[0].get_children()[0].get_facecolor()
            expected_palette = args[1].axes.flat[0].get_children()[0].get_facecolor()

            assert np.array_equal(actual_palette,expected_palette), ("""
The `palette` parameter is incorrect or not defined. Please use the `palette` parameter. Expected the `palette` parameter to be: `Dark2`""")


import filecmp
import os.path

def grading_directory(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path
    @param dir2: Second directory path

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """

    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0:
        print("false actual")
        for item in dirs_cmp.left_only:
            print(item)
        return False
    if len(dirs_cmp.right_only)>0:
        print("false test")
        for item in dirs_cmp.right_only:
            print(item)
        return False
    if len(dirs_cmp.funny_files)>0:
        print("false funny")
        return False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0 or len(errors)>0:
        print("false 2")
        return False
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not grading_directory(new_dir1, new_dir2):
            print("false 3")
            return False
    return True

def grading_directory3(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path - actual directory
    @param dir2: Second directory path - test directory

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """
    
    dirs_cmp = filecmp.dircmp(dir1, dir2)
    if len(dirs_cmp.left_only)>0:
        # print("false actual2")
        for item in dirs_cmp.left_only:
            print(item)
        # return False
        justfail((dir1, dir2), f"There are extra files/folders or different file/folder names in `{dir1}: {dirs_cmp.left_only}`. Please remove them or revert the file/folder names back to original.")
    if len(dirs_cmp.right_only)>0:
        # print("false test")
        # for item in dirs_cmp.right_only:
        #     print(item)
        # return False
        justfail((dir1, dir2), f"Some files/folders are missing in `{dir1}`: {dirs_cmp.right_only}. Please add them or run `scrapy startproject hot_100_mar` again.")
    if len(dirs_cmp.funny_files)>0:
        print("false funny")
        # return False
        justfail((dir1, dir2), f"Please check the file permissions.")
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0:
        # print("false mismatch")
        justfail((dir1, dir2), f"The content in the file/files are different: `{mismatch}`. Did you edit them before you run `q1.check()`?")
    if len(errors)>0:
        # print("false errors")
        # return False
        justfail((dir1, dir2), f"These files are not accessible: `{errors}`. Please check the file permissions.")

    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not grading_directory3(new_dir1, new_dir2):
            return False
    justpass()

def grading_directory4(dir1, dir2):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: First directory path - actual directory
    @param dir2: Second directory path - test directory

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """
    
    # Define the list of files to exclude
    exclude_files = ['output.csv', 'transaction.csv', 'transaction.json', 'transaction_without_result_column.csv', '.gitignore', '.ipynb_checkpoints']

    dirs_cmp = filecmp.dircmp(dir1, dir2)

    filtered_left_only = [file for file in dirs_cmp.left_only if not any(exclude_file in file for exclude_file in exclude_files)]
    filtered_right_only = [file for file in dirs_cmp.right_only if not any(exclude_file in file for exclude_file in exclude_files)]
    filtered_common_files = [file for file in dirs_cmp.common_files if not any(exclude_file in file for exclude_file in exclude_files)]

    if len(filtered_left_only)>0:
        # print("false actual2")
        # for item in filtered_left_only:
        #     print(item)
        # return False
        justfail((dir1, dir2), f"There are extra files/folders or different file/folder names in `{dir1}: {filtered_left_only}`. Please remove them or revert the file/folder names back to original.")
    if len(filtered_right_only)>0:
        # print("false test")
        # for item in dirs_cmp.right_only:
        #     print(item)
        # return False
        justfail((dir1, dir2), f"Some files/folders are missing in `{dir1}`: {dirs_cmp.right_only}. \nPlease add them or run `scrapy startproject hot_100_mar` again, or run the `scrapy crawl` command in the terminal again.")
    if len(dirs_cmp.funny_files)>0:
        print("false funny")
        # return False
        justfail((dir1, dir2), f"Please check the file permissions.")
    (_, mismatch, errors) =  filecmp.cmpfiles(
        dir1, dir2, filtered_common_files, shallow=False)
    if len(mismatch)>0:
        print(f"mismatch: {mismatch}")
        justfail((dir1, dir2), f"The content in the file/files are different: `{mismatch}`. Did you edit them before you run `q1.check()`?")
    if len(errors)>0:
        # print("false errors")
        # return False
        justfail((dir1, dir2), f"These files are not accessible: `{errors}`. Please check the file permissions.")
    
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(dir1, common_dir)
        new_dir2 = os.path.join(dir2, common_dir)
        if not grading_directory4(new_dir1, new_dir2):
            return False
    justpass()

def grading_directory2(actual_dir, test_dir):
    """
    Compare two directories recursively. Files in each directory are
    assumed to be equal if their names and contents are equal.

    @param dir1: Actual directory path from student's ilabguide
    @param test_dir: Directory path of the test folder within `suss`

    @return: True if the directory trees are the same and 
        there were no errors while accessing the directories or files, 
        False otherwise.
   """
    result = True
    # assert os.path.exists(actual_dir), f"Directory not found: {actual_dir}. Try running `scrapy startproject hot_100_mar` again."
    dirs_cmp = filecmp.dircmp(actual_dir, test_dir)

    if len(dirs_cmp.left_only)>0:
        result = False 
        assert result, f"There are extra files/folders in `{actual_dir}: {dirs_cmp.left_only}`. Please remove them."
    if len(dirs_cmp.right_only)>0:
        result = False
        assert result, f"Some files/folders are missing in `{actual_dir}`: {dirs_cmp.right_only}. Please add them or run `scrapy startproject hot_100_mar` again."
    if len(dirs_cmp.funny_files)>0:
        result = False
    (_, mismatch, errors) =  filecmp.cmpfiles(
        actual_dir, test_dir, dirs_cmp.common_files, shallow=False)
    if len(mismatch)>0:
        result = False
        assert result, f"The content in the file/files are different: `{mismatch}`. Did you edit them before you run `q1.check()`?"
    if len(errors)>0:
        result = False
        assert result, f"These files are not accessible: `{errors}`. Please check the file permissions."
    
    # TODO: The check below will return incorrect due to additional __pycache__ file : e.g. hot_100_list_spider.cpython-38.pyc - middlewares.cpython-38.pyc- items.cpython-38.pyc - settings.cpython-38.pyc
    for common_dir in dirs_cmp.common_dirs:
        new_dir1 = os.path.join(actual_dir, common_dir)
        new_dir2 = os.path.join(test_dir, common_dir)
        # print_directory_contents(new_dir1)
        # print("-----above is newdir1, below is newdir2---")
        # print_directory_contents(new_dir2)
        if not grading_directory2(new_dir1, new_dir2):
            result = False
            assert result, f"The subdirectories in {actual_dir} is incorrect."
    assert result

def print_directory_contents(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Directory: {root}")
        print("Files:")
        for file in files:
            print(f"- {file}")
        print("Directories:")
        for subdir in dirs:
            print(f"- {subdir}")

def grading_check_setter(args0, args1, obj, attr, args4, args5):
    try:
        setattr(obj, attr, args1)
        actual_value = getattr(obj, attr)
        if actual_value == args1:
            justpass()
        else:
            determine_the_grading_method((args0, args1, actual_value))
    except AttributeError as e:
        justfail(args4, f"{args5} is not defined. Please check your code.")
        pprint(f"{type(e).__name__}: {str(e)}")

def read_dat_file(fn, filename):
    try:
        with redirect_stdout(open('intermediate','w')): 
            actual = fn()
        
        # we need another file because for lab6q1c there is a print statement and a output file
        # this file reader is to read the print statements
        with open("intermediate", 'r', encoding='utf-8') as z:
            out1 = z.read()
        
        # this is to read the output file
        with open(filename, 'r', encoding='utf-8') as a:
            out = a.read()

        # delete the intermediate file
        os.remove("intermediate")
         
        return (out1+out,actual)
    except:
        
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
        return (contents, None)
    
def compare_printout_with_args(fn, args):
    f = io.StringIO()
    with redirect_stdout(f):
        actual = fn(args)
    out = f.getvalue() 
    return (out, actual) 

# returning a tuple. But what if the function has more than one return value? refactoring the code into a function for reusability
def compare_printout(fn):
    f = io.StringIO()
    with redirect_stdout(f):
        actual = fn()
    out = f.getvalue() 
    return (out, actual) 

def capture_print_output():
    # Create a StringIO buffer to capture the printed content
    output_buffer = io.StringIO()
    
    # Redirect the standard output (sys.stdout) to the buffer
    sys.stdout = output_buffer
    
    return output_buffer


def compare_printout_from_while_loop(fn):
    try:
        f = io.StringIO()
        with redirect_stdout(open('out','w')):
            actual = fn()   
        with open('out', 'r', encoding='utf-8') as a:
            out = a.read()
            
        return (out, actual) 
    except:
        # tb = traceback.format_exc()
        # # add color to the traceback
        # colored_tb = colored(tb, 'red')
        # pprint(colored_tb)
        with open('out', 'r', encoding='utf-8') as f:
            contents = f.read()
        return (contents,None)

def query_config(file):
    config_data = {}
    if os.path.exists(file):
        with open(file, 'r') as f:
            config_data = yaml.safe_load(f)
    else:
        log(f'{file} is not present.')
    return config_data

def check_key_in_yaml(file_path, key_to_check):
    with open(file_path, 'r') as file:
        yaml_content = yaml.safe_load(file)

    exists = key_to_check in yaml_content
    # if exists:
    #     log(f"Key '{key_to_check}' exists.")
    # else:
    #     log(f"Key '{key_to_check}' does not exist.")

    return exists

def grading_csv(test_file, path, expected_file, args):
    script_directory = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    expected_file_path = os.path.join(script_directory, expected_file)  # Adjust the path as needed


    # Open forecast.csv and another CSV file for comparison
    with open(path) as actual_file, open(expected_file_path) as expected_file:
        actual_csv = csv.reader(actual_file)
        expected_csv = csv.reader(expected_file)

        # Convert the CSV data into lists of rows
        actual_data = list(actual_csv)
        expected_data = list(expected_csv)
        
        # Check if the number of rows is the same
        assert len(actual_data) == len(expected_data)

        # Check if each row in forecast.csv matches the corresponding row in another_file.csv
        for actual_row, expected_row in zip(actual_data, expected_data):
            grading_lists_in_csv((test_file, actual_row, expected_row))

    # Check the headers
    with open(path) as f:
        actual_headers = next(csv.reader(f))
        expected_headers = args
        assert actual_headers == expected_headers
            
def source_code_comparison(original, output):
    if original == output:
        log("There is no difference, thus you will see `incorrect`.")
    else:
        assert original == output, ("""
<b>Original Source Code:</b>
<pre>`{}`</pre>
({})

<b>Modified Source Code:</b>
<pre>`{}`</pre>
({})

See the String diff:
<pre><span style=\"font:bold\">"</span>{}<span>"</span></pre>
""").format(original, type(original).__name__, output, type(output).__name__, get_edits_string(original, output))