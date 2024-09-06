
import os

hint = ""
file_path = os.path.dirname(CURRENT_PATH_NAME)
hint_file_path = os.path.dirname(file_path)

path_components = CURRENT_PATH_NAME.split("/")
module_name = path_components[4]
lab_name = path_components[5].split(".")[0]

hint_file = os.path.join(hint_file_path, ".plugins/helpful_warning/", f"{module_name}/{lab_name}.hint")

if os.path.exists(hint_file):
    with open(hint_file, 'r') as file:
        hint = file.read()

print(hint)