import random
import os
import yaml
from learntools.vli.analytics import process_path, abbreviate_question, get_email
from learntools.core.tracking import OutcomeType
from git import GitConfigParser
from learntools.vli.encryption import load_config

COUNTER = random.randint(2, 4)
config_file = ".config.yml"
instructor_config_file = ".instructor_config.yml"

# if this question is inside the show_solution_list, then show the solution.
def included_in_show_solution_list(answer):
    config_data = {}
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            config_data = yaml.safe_load(f)
    else:
        print(f'{config_file} is not present.')
        return
    
    show_solution_list = config_data.get("show_solution_list")
    if show_solution_list is None:
        # print(f'"show_solution_list" key is missing in {config_file}.')
        return False
    elif answer in show_solution_list:
        return True


def get_current_question(class_name_and_path):
    class_name, path = class_name_and_path
    exercise, course = process_path(path)
    lab = course.split('_')[0]
    return f"{lab}{abbreviate_question(class_name)}"

def get_instructor_email():
    try:    
        config_parser = GitConfigParser("/home/labsuser/.gitconfig")
        if config_parser is None:
            email = "student"
        else:
            email = config_parser.get_value('user', 'email')
            if email is None:
                email = "student"
    except Exception as e:
        email = "student"               
    return email


# This function will check wthether this account is an instructor account
# we will check the instructor_config_file to see if the email is in the instructor_list
def check_if_this_account_is_an_instructor():
    #get the email in .config.yml matches the email in .gitconfig
    data = load_config()
    instructor_config_filepath =  data["suss_path"] +instructor_config_file
    instructor_email =  get_instructor_email()
    # print(instructor_config_filepath)
    # print(instructor_email)
    if os.path.exists(instructor_config_filepath):
        with open(instructor_config_filepath, 'r') as f:
            config_data = yaml.safe_load(f)
            if instructor_email in config_data["instructors_list"]: 
                return True
    else:
        # print("instructor_config_file is not present")
        return False
             
    return False

def always_show_solution():
    config_data = load_config()
    always_show_solution = config_data.get("always_show_solution")
    if always_show_solution is None:
        return False
    elif always_show_solution == True:
        return True
    else:
        return False

# placed in problem_view.py. When student trigger solution(), we will check if the question is in the show_solution_list
def solution_accessible_after():
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            try:
                current_question = get_current_question( self.print_class_name())
                if check_if_this_account_is_an_instructor() or included_in_show_solution_list(current_question) or always_show_solution() or self._num_checks >= COUNTER:
                    return method(self, *args, **kwargs)
                else:
                    raise Exception (f"Solution can be accessed after attempting the question a few times.")
            except Exception as e:
                print(e)
        return wrapper
    return decorator

# placed in problem_view.py. When student trigger check(), we will update the _num_checks
def check_before_solution(method):
    def wrapper(self, *args, **kwargs):
        results = method(self, *args, **kwargs)
        if self._last_outcome == OutcomeType.PASS:
            self._num_checks = COUNTER + 1
        else:
            self._num_checks = self._num_checks + 1
        return results
    return wrapper
