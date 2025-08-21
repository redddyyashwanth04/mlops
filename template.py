import os
from pathlib import Path
# print(Path("a/b/b.text"))
#these are the list of the file requirements
list_of_files=[
    ".github/workflows/.gitkeep"
    ,"src/_init_.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py"
    "src/pipeline/__init__.py",
    "src/pipeline/trainig_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"

]
def create_files_and_directories(file_list):
    """
    Creates the specified directories and files from a list of file paths.

    Args:
        file_list (list): A list of file paths to be created.
    """
    print("Starting creation of files and directories...")
    for file_path in file_list:
        # Get the directory part of the file path
        dir_name = os.path.dirname(file_path)

        # If a directory exists in the path, create it.
        # The exist_ok=True flag prevents errors if the directory already exists.
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            print(f"Created directory: {dir_name}")

        # Create the file with a simple comment inside
        try:
            with open(file_path, "w") as f:
                # Add a simple line to the file so it's not empty
                if file_path.endswith(".py"):
                    f.write("# This is a Python file")
                elif file_path.endswith(".sh"):
                    f.write("#!/bin/bash\n# This is a shell script")
                elif file_path.endswith(".txt"):
                    f.write("# This is a text file")
                else:
                    f.write("# This is an empty file to keep the directory")
            print(f"Created file: {file_path}")
        except Exception as e:
            print(f"Error creating file {file_path}: {e}")

    print("\nFile and directory creation complete!")

# Run the function with the provided list
create_files_and_directories(list_of_files)

