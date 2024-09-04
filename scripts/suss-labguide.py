#!/usr/bin/env python3

import typer
import shutil
from pathlib import Path
import os
import subprocess

app = typer.Typer()

@app.command()
def setup(course: str = None):
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
            destination.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)
            print(f"LabGuide setup is completed. You can find the labs in `labs/` folder and try lab0.")
            
            if requirements_file.exists():
                subprocess.run(["pip", "install", "-r", str(requirements_file)], check=True)
                print(f"Installed requirements from {requirements_file}.")
            else:
                print(f"No requirements.txt found in {dest_folder}.")
        else:
            print(f"labs/lab0 already exists. Use the course argument to specify a different course.")

        

@app.command()
def get(course: str):
    # Define the repository URL using the course name
    repo_url = f"https://github.com/suss-vli/labguide_{course}.git"
    
    # Define the path for the destination folder within labs/
    labs_dir = Path.cwd() / "labs"
    course_folder = labs_dir / course

    # Check if the course folder already exists
    if course_folder.exists():
        print(f"Course folder {course_folder} already exists. Use a different name or remove the existing folder.")
        return

    # Clone the repository into the labs folder as the specified course
    try:
        subprocess.run(["git", "clone", repo_url, str(course_folder)], check=True)
        print(f"Cloned {repo_url} into {course_folder}.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_url}: {e}")

if __name__ == "__main__":
    app()