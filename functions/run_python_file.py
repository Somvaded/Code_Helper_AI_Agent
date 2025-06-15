import os
import subprocess
from google.genai import types
def run_python_file(working_directory , file_path,args = None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory , file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.split("/")[-1].endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = ["python3",abs_file_path]
        if args:
            command.extend(args)
        process = subprocess.run(
            command,
            cwd = abs_working_dir, 
            capture_output=True,
            timeout = 30,
            text = True)
        output = []
        if process.stdout:
            output.append(f"STDOUT:\n{process.stdout}")
        if process.stderr:
            output.append(f"STDERR:\n{process.stderr}")
        if not process.stdout and not process.stderr :
            return "No output produced"       
        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")

        return '\n'.join(output)

    except Exception as err:
        return f"Error: executing Python file: {err}"

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "Runs a python file with specified file path and optional args for the file, file path is constrained to the working directory.",
    parameters = types.Schema(
            type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path to the file , relative to the working directory,"
            ),
            "args": types.Schema(
                type = types.Type.ARRAY,
                description = "It's an optional arguement. Contains an array of additional args for the python file to run with in the subprocess.",
                items = types.Schema(type= types.Type.STRING)
            ),
        },
        required = ["file_path"]
    )
)
