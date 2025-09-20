import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'could not create the parent directory {parent_dir} = {e}'
        
        
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"failed to write to file: {file_path}, {e}"
    

schema_write_file = types.FunctionDeclaration(
name="write_file",
description="Overwrites an existing file or write to a new file if it doesn't exist(creates the required parent directory safely), constrained to the working directory.",
parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
        "file_path": types.Schema(
            type=types.Type.STRING,
            description="The path to the file to write. ",
            ),
            "content": types.Schema(
            type=types.Type.STRING,
            description="The contents to write to the file as a string. ",
            ),
        },
    ),
)