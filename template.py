import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


project_name = "detectionClassifier"

list_of_files = [
     ".github/workflows/.gitkeep",
     f"src/{project_name}/__init__.py",
     f"src/{project_name}/components/__init__.py",
     f"src/{project_name}/utils/__init__.py",
     f"src/{project_name}/config/__init__.py",
     f"src/{project_name}/config/configuration.py",
     f"src/{project_name}/pipeline/__init__.py",
     f"src/{project_name}/entity/__init__.py",
     f"src/{project_name}/constants/__init__.py",
     "config/config.yaml",
     "dvc.yaml",
     "params.yaml",
     "requirements.txt",
     "setup.py",
     "research/trails.ipynb",
     "templates/index.html"


]

# Path class from the pathlib module in Python is used to represent and work with filesystem paths in an object-oriented way
# Path will be having a lot of inbuilt methods which will help us to create the files and folders
for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)  # Split the file path into directory and file name
    if filedir:
        # If the directory part of the file path is not empty, create the directory
        os.makedirs(filedir, exist_ok=True)  # exist_ok=True means do not raise an error if the directory already exists
        logging.info(f"Creating directory: {filedir} for the file: {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        # If the file does not exist or if it exists but is empty, create the file
        with open(file_path, 'w') as f:
            pass
    else:
        # If the file already exists and is not empty, log a message
        logging.info(f"{filename} already exists and is not empty. Skipping file creation.")
logging.info("All files and directories created successfully.")

# The above code will create the following directory structure:
# .
# ├── config
# │   ├── config.yaml
# ├── dvc.yaml
# ├── params.yaml
# ├── requirements.txt
# ├── setup.py
# ├── research
# │   └── trails.ipynb
# └── src
#     └── detectionClassifier
#         ├── __init__.py
#         ├── components
#         │   └── __init__.py
#         ├── utils
#         │   └── __init__.py
#         ├── config
#         │   └── __init__.py
#         ├── pipeline
#         │   └── __init__.py
#         ├── entity
#         │   └── __init__.py
#         └── comstants
#             └── __init__.py
# The above code will create the directory structure and empty files as specified in the list_of_files variable.