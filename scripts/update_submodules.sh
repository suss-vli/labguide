#!/bin/bash

# Step 1: Ensure you're in the root directory of your Git repository
repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root" || exit

# Check if specific submodules are passed as arguments
if [ "$#" -gt 0 ]; then
    submodules=("$@")
    echo "Initializing and updating specified submodules: ${submodules[*]}"
else
    submodules=($(git config --file .gitmodules --get-regexp path | awk '{ print $2 }'))
    echo "Initializing and updating all submodules: ${submodules[*]}"
fi

# Step 2: Initialize and update the specified or all submodules to the recorded commits
for submodule in "${submodules[@]}"; do
    echo "Initializing submodule '$submodule'..."
    git submodule init "$submodule"
    
    echo "Updating submodule '$submodule' to the recorded commit..."
    git submodule update "$submodule"
done

# Step 3: Fetch and update the specified or all submodules to the latest commits from their remote repositories
for submodule in "${submodules[@]}"; do
    echo "Fetching and merging latest commits for submodule '$submodule'..."
    git submodule update --remote --merge "$submodule"
done

# Step 4: Add the updated submodule references to the staging area
echo "Staging submodule updates..."
git add .

# Step 5: Commit the updates
echo "Committing the updates..."
git commit -m "Update submodules to the latest commits"

# Optional: Push the changes to the remote repository
# echo "Pushing updates to remote repository..."
# git push origin main  # Replace 'main' with your branch name if different

echo "Submodules have been initialized, updated, and committed."
