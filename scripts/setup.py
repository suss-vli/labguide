#!/usr/bin/env python3

import os
import subprocess
import sys
import shutil

# def remove_venv():
#     if os.path.isdir("venv"):
#         shutil.rmtree("venv")

def check_arguments():
    if len(sys.argv) != 2:
        print("Usage: setup_course {folder}")
        sys.exit(1)
    return sys.argv[1]

def initialize_submodules(folder):
    dev_path = os.path.dirname(__file__)
    labguide_package_path =  os.path.abspath(os.path.join(dev_path, '..'))
    print(labguide_package_path)
    os.chdir(labguide_package_path) 
    subprocess.check_call(["git", "submodule", "init", "suss", "learntools", folder])
    subprocess.check_call(["git", "submodule", "update", "suss", "learntools", folder])

def create_venv():
    subprocess.check_call([sys.executable, "-m", "venv", "venv"])
    activate_script = ". ./venv/bin/activate"
    subprocess.check_call([activate_script], shell=True)

def install_dependencies(folder):
    print(os.cwd())
    dev_path = os.path.dirname(__file__)
    labguide_package_path =  os.path.abspath(os.path.join(dev_path, '..'))
    # os.path.abspath(os.path.join(os.path.dirname(__file__), 'labguide'))
    print(labguide_package_path)
    os.chdir(labguide_package_path)  # Change to main_package directory
    print(os.cwd())
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "./suss"])
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "./learntools"])
    # requirements_file = os.path.join(labguide_package_path, folder, "requirements.txt")
    # print(f"Installing requirements from file: {requirements_file}")
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
    # subprocess.check_call([sys.executable, "-m", "pip", "install", "ipykernel"])
    # subprocess.check_call([sys.executable, "-m", "ipykernel", "install", "--user", "--name=venv"])
    # os.chdir('..')  # Go back to the original directory

def setup_course():
    # remove_venv()
    folder = check_arguments()
    initialize_submodules(folder)
    create_venv()
    install_dependencies(folder)

if __name__ == "__main__":
    setup_course()
