#!/usr/bin/env python3

import typer
import shutil
from pathlib import Path
import subprocess

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
    dest_folder = destination / "folder"

    # Copy the entire "folder/" directory into the new directory
    if source_folder.exists() and source_folder.is_dir():
        shutil.copytree(source_folder, dest_folder, dirs_exist_ok=True)
        print(f"Copied {source_folder} to {dest_folder}")
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
