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
    labs_dir = Path.cwd()

    if course:
        # Handle the case where a course argument is provided
        course_folder = labs_dir / course
        requirements_file = course_folder / "requirements.txt"
        
        if course_folder.exists() and course_folder.is_dir():
            if requirements_file.exists():
                # Install requirements if requirements.txt exists
                subprocess.run(["pip", "install", "-r", str(requirements_file)], check=True)
                print(f"Installed requirements from {requirements_file}.")
                print(f"{course} labguide setup is completed. You can start lab1 in the `{course}` folder.")
            else:
                print(f"No requirements.txt found in {course_folder}.")
        else:
            print(f"Course folder {course_folder} does not exist. Please run `suss-labguide get {course}` to fetch the course data.")
    else:
        # Handle the case where no course argument is provided
        lab0_source = package_dir / "lab0"
        plugins_source = package_dir / ".plugins"
        lab0_dest_folder = labs_dir / "lab0"
        plugins_dest_folder = labs_dir / ".plugins"
        lab0_requirements_file = lab0_dest_folder / "requirements.txt"
        
        if not plugins_dest_folder.exists():
            plugins_dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.copytree(plugins_source, plugins_dest_folder, dirs_exist_ok=True)
            
        if not lab0_dest_folder.exists():
            lab0_dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.copytree(lab0_source, lab0_dest_folder, dirs_exist_ok=True)
            
            if lab0_requirements_file.exists():
                subprocess.run(["pip", "install", "-r", str(lab0_requirements_file)], check=True)
                print(f"Installed requirements from {lab0_requirements_file}.")
                print(f"LabGuide setup is completed. You can try lab0.")
            else:
                print(f"No requirements.txt found in {lab0_dest_folder}.")
        else:
            print(f"lab0/ already exists. Specify a course to setup for the course. Example: labguide setup [course code].")

@app.command()
def get(course: str):
    
    if course not in labguide_courses:
        print(f"Invalid course: '{course}'")
        print("Please select from these available courses:\n" + '\n'.join(labguide_courses))
        return
    # Start from the current directory and search upwards for "labs" directory
    current_dir = Path.cwd()
    
    # Define the path for the destination folder within labs/
    course_folder = current_dir / course

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
        # After cloning, navigate into the course folder
    os.chdir(course_folder)

    # Remove the .git directory
    git_dir = course_folder / ".git"
    if git_dir.exists() and git_dir.is_dir():
        shutil.rmtree(git_dir)

    # Remove the .gitignore file
    gitignore_file = course_folder / ".gitignore"
    if gitignore_file.exists() and gitignore_file.is_file():
        gitignore_file.unlink()
        
if __name__ == "__main__":
    app()

