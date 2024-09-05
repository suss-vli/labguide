#!/usr/bin/env python3

import typer
import shutil
from pathlib import Path
import os
import subprocess

app = typer.Typer()

labguide_courses = ["ict133", "ict162", "ict233", "anl588"]

@app.command()
def setup(course: str = typer.Argument(None, help="The name of the course to set up (optional).")):
    package_dir = Path(__file__).parent.parent
    labs_dir = Path.cwd() / "labs"

    if course:
        # Handle the case where a course argument is provided
        course_folder = labs_dir / course
        requirements_file = course_folder / "requirements.txt"
        
        if course_folder.exists() and course_folder.is_dir():
            if requirements_file.exists():
                # Install requirements if requirements.txt exists
                subprocess.run(["pip", "install", "-r", str(requirements_file)], check=True)
                print(f"Installed requirements from {requirements_file}.")
                print(f"{course} labguide setup is completed. You can start lab1 in the `labs/{course}` folder.")
            else:
                print(f"No requirements.txt found in {course_folder}.")
        else:
            print(f"Course folder {course_folder} does not exist. Please run `suss-labguide get {course}` to fetch the course data.")
    else:
        # Handle the case where no course argument is provided
        source_folder = package_dir / "lab0"
        dest_folder = labs_dir / "lab0"
        requirements_file = dest_folder / "requirements.txt"
        
        if not dest_folder.exists():
            dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)
            
            if requirements_file.exists():
                subprocess.run(["pip", "install", "-r", str(requirements_file)], check=True)
                print(f"Installed requirements from {requirements_file}.")
                print(f"LabGuide setup is completed. You can find the labs in `labs/` folder and try lab0.")
            else:
                print(f"No requirements.txt found in {dest_folder}.")
        else:
            print(f"labs/lab0 already exists. Specify a course to setup for the course. Example: labguide setup [course code].")

@app.command()
def get(course: str):
    
    if course not in labguide_courses:
        print(f"Invalid course: '{course}'")
        print(f"Please select from these available courses:\n{{'\n'.join(labguide_courses)}}")
        return
    # Start from the current directory and search upwards for "labs" directory
    current_dir = Path.cwd()
    labs_dir = None
    
    # Look for "labs" directory from current directory upwards
    for parent in [current_dir] + list(current_dir.parents):
        possible_labs_dir = parent / "labs"
        if possible_labs_dir.exists() and possible_labs_dir.is_dir():
            labs_dir = possible_labs_dir
            break

    # If "labs" directory was not found, print an error
    if not labs_dir:
        print("Could not find 'labs' directory in the current or parent directories.")
        return
    
    # Define the path for the destination folder within labs/
    course_folder = labs_dir / course

    # Check if the course folder already exists
    if course_folder.exists():
        print(f"Course folder {course_folder} already exists. Use a different name or remove the existing folder.")
        return

    # Define the repository URL using the course name
    repo_url = f"https://github.com/suss-vli/labguide_{course}.git"

    # Clone the repository into the labs folder as the specified course
    try:
        subprocess.run(["git", "clone", repo_url, str(course_folder)], check=True)
        print(f"Cloned {repo_url} into {course_folder}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_url}: {e}")

if __name__ == "__main__":
    app()

if __name__ == "__main__":
    app()
