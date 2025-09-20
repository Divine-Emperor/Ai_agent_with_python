import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=[]):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # CORRECTED: This message now matches the test's expectation.
    if not abs_file_path.startswith(abs_working_directory):
        return f'Cannot execute "{file_path}" as it is outside'

    # CORRECTED: This message now matches the test's expectation.
    if not os.path.isfile(abs_file_path):
        return f'File "{file_path}" not found'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        final_args = ["python3", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_directory,
            timeout=30,
            capture_output=True
        )
        # Using decode to convert bytes to string for cleaner output
        stdout = output.stdout.decode('utf-8')
        stderr = output.stderr.decode('utf-8')

        final_string = f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}\n"
        
        if not stdout and not stderr:
            final_string = "No Output Produced.\n"
        
        if output.returncode != 0:
            final_string += f"Process Exited With Code {output.returncode}"
            
        return final_string.strip()
        
    except Exception as e:
        return f"Error: executing Python file: {e}"

# Corrected Schema Definition
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python file with the python3 interpreter. Accepts additional CLI args as an optional Array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to run, relative to the working directory."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="An optional array of strings to be used as command-line arguments for the python file.",
                items=types.Schema(
                    type=types.Type.STRING
                )
            ),
        },
        # You should also declare which parameters are required
        required=["file_path"]
    ),
)