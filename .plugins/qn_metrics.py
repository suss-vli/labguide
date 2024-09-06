import json
import os
import nbformat
from datetime import datetime
from hashlib import sha256

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
total_qn_count = 0
total_correct_count = 0

# to-do: are we able to retrieve student info through context in the future?
USER_NAME = "bryanc"
USER_EMAIL = "bryanc@example.com"
USER_ID = f"{USER_NAME},{USER_EMAIL}"
USER_ID = sha256(USER_ID.encode('utf-8')).hexdigest()

# Process Notebook File
try:
    with open(CURRENT_PATH_NAME, 'r', encoding="utf-8") as file:
        nb = nbformat.read(file, nbformat.NO_CONVERT)
        
        for cell in nb["cells"]:
            # Get total number of questions
            if cell["cell_type"] == "markdown" and cell["source"]:
                if cell["source"].strip().startswith("### Question") or cell["source"].strip().startswith("###  Question"):
                    total_qn_count += 1
                
            # Get total number of correct
            elif cell["cell_type"] == "code" and cell["outputs"]:
                for output in cell["outputs"]:
                    if output.get("data", {}):
                        plaintext = output.get("data", {}).get("text/plain")
                        
                        if plaintext.strip().startswith("Correct"):
                            total_correct_count += 1
                
    
    print(f"Total Questions: {total_qn_count}")
    print(f"Total Correct: {total_correct_count}")
except Exception as e:
    raise Exception(f"An error occurred while extracting cell contents from the notebook: {str(e)}")

# Write .json with meterics
try:
    data = {
        "id": USER_ID,
        "datetime": timestamp,
        "num_of_correct": total_correct_count,
        "total_questons": total_qn_count
    }
    
    # Just save file based on last 8 characters of hash
    name = CURRENT_FILE_NAME.split(".")[0]
    json_file_name = f"{name}_{USER_ID[-8:]}.json"
    
    with open(json_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)
except Exception as e:
    raise Exception(f"An error occurred while generating json.")