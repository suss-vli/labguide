#!/usr/bin/env python3

import typer
import shutil
from pathlib import Path
import subprocess
import os

app = typer.Typer()

@app.command()
def setup():
    # Get the path to the "folder/" in your installed package
    package_dir = Path(__file__).parent.parent
    source_folder = package_dir / "lab0"

    # Destination is a new directory in the current working directory
    destination = Path.cwd() / "labs"

    # Create the new directory
    destination.mkdir(exist_ok=True)

    # Define the path for the destination folder
    dest_folder = destination / "lab0"

    # Copy the entire "lab0/" directory into the new directory
    if source_folder.exists() and source_folder.is_dir():
        items_to_copy = list(source_folder.glob('*')) + list(source_folder.glob('.*'))
        
        for item in items_to_copy:
            dest_item = dest_folder / item.name
            if item.is_dir():
                shutil.copytree(item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(item, dest_item)
        print(f"LabGuide is setup. You can find lab files in the `labs/` directory and try lab0.")
    else:
        print(f"Source folder {source_folder} does not exist")
        
@app.command()
def get(course: str):
    # Define the repository URL (example format)
    repo_url = f"https://github.com/suss-vli/labguide_{course}.git"
    
    # Clone the repository into the current working directory
    try:
        subprocess.run(["git", "clone", repo_url], check=True)
        print(f"Cloned {repo_url} into the current directory.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone {repo_url}: {e}")

if __name__ == "__main__":
    app()
