#!/bin/bash

# Check if a virtual environment exists and remove it if it does
if [ -d "venv" ]; then
    rm -rf venv
fi
# Check if folder argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: ./dev/setup.sh {folder}"
    exit 1
fi

folder=$1

git submodule init suss learntools $folder
git submodule update suss learntools $folder

python3 -m venv venv
. venv/bin/activate

pip3 install ./suss
pip3 install ./learntools
echo "Installing requirements from file: ./$folder/requirements.txt"
pip3 install -r ./$folder/requirements.txt
pip3 install ipykernel
python3 -m ipykernel install --user --name=venv
