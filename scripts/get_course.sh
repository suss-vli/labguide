#!/bin/bash

# Ensure you're in the root directory of your Git repository
repo_root=$(git rev-parse --show-toplevel)
cd "$repo_root" || exit

# Check if folder argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: ./dev/get_course.sh {folder}"
    exit 1
fi

folder=$1

git submodule init $folder
git submodule update $folder

./dev/setup.sh $folder