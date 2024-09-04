### testing transaction.json to track hint()###
import functools
from IPython.display import display
import json
import os
import datetime
import csv
import re
import yaml
from git import GitConfigParser
from learntools.vli.encryption import  load_config

def abbreviate_question(question):
    return re.sub(r'(?i)question(\d+[a-z]*)', lambda m: 'q' + m.group(1).lower(), question)

# Function `process_path` will return the exercise and course name from the path
def process_path(path):
    if path is None:
        return
    exercise, course = path.split('/')[-1].split('.')[0], path.split('/')[-2]
    return exercise, course

# Function `get_email` that return the email according to the git config
def get_email():
    try:    
        config_parser = GitConfigParser("/home/labsuser/.gitconfig")
        if config_parser is None:
            email = "student"
        else:
            email = config_parser.get_value('user', 'email')
            if email is None:
                email = "student"
    except:
        email = "student"               
    return email

# These code add to displayer function to track the various functions within iLabGuide. Without returning the result
def displayer(fn):
    @functools.wraps(fn)
    def wrapped(self,*args, **kwargs):
        config = load_config()

        if config.get('analytics', False):
            res = fn(self,*args, **kwargs)
            display(res)
            email = get_email()                
            class_name, path = self.print_class_name()
            dir_path = os.getcwd()

            file_path = os.path.join(dir_path, 'transaction.json')
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    json.dump({"count": 0, "data": []}, f)

            with open(file_path, 'r') as f:
                data = json.load(f)
                
            exercise,course = process_path(path)

            index = len(data["data"]) + 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # This may fix the multiple line issue
            result = repr(res).replace("\n", " ")
            
            # This may be the second solution
            hash = {"index": index,
                        "timestamp": timestamp,
                        "class_name": class_name,
                        "method_name": fn.__name__,
                    "course": course,
                    "exercise": exercise,
                    "student": email,
                    "result": f'''{result}'''}
            
            hash_without_result = {"index": index,
                            "timestamp": timestamp,
                            "class_name": class_name,
                            "method_name": fn.__name__,
                            "course": course,
                            "exercise": exercise,
                            "student": email}

            with open("output.csv", "w", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL, quotechar='"', doublequote=True, lineterminator="\n")
                for row in data:
                    writer.writerow(row)

            
            data["data"].append(hash)

            count = data["count"] + 1
            data["count"] = count

            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)
                
            
            # CSV    
            dir_path = os.getcwd()

            # create the transaction.csv file if it does not exist
            file_path = os.path.join(dir_path, 'transaction.csv')
            file_exists = os.path.exists(file_path)

            with open(file_path, 'a', newline='', encoding='utf-8') as f:
                fieldnames = ['index', 'timestamp', 'class_name', 'method_name', 'course', 'exercise', 'student', 'result']
                writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, quotechar='"', doublequote=True, lineterminator="\n")
                
                if not file_exists:
                    writer.writeheader()

                # add the current timestamp to the transaction.csv file with an index
                index = 1
                if file_exists:
                    with open(file_path, 'r', newline='', encoding='utf-8') as rf:
                        reader = csv.reader(rf)
                        index = len(list(reader))
                        
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow(hash)

            dir_path = os.getcwd()

            # create the transaction.csv file if it does not exist
            file_path = os.path.join(dir_path, 'transaction_without_result_column.csv')
            file_exists = os.path.exists(file_path)

            with open(file_path, 'a', newline='', encoding='utf-8') as f:
                fieldnames = ['index', 'timestamp', 'class_name', 'method_name', 'course', 'exercise', 'student']
                writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL, quotechar='"', doublequote=True, lineterminator="\n")
                
                if not file_exists:
                    writer.writeheader()

                # add the current timestamp to the transaction.csv file with an index
                index = 1
                if file_exists:
                    with open(file_path, 'r', newline='', encoding='utf-8') as rf:
                        reader = csv.reader(rf)
                        index = len(list(reader))

                        
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow(hash_without_result)
        else:
            return fn(self, *args, **kwargs)  # Execute the function and return its result, skip analytics



        # Don't propagate the return to avoid double printing.
    return wrapped
