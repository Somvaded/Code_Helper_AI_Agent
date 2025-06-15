import os
from google.genai import types

def write_file(working_directory , file_path , content):
    abs_working_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
    if not abs_file_path.startswith(abs_working_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.exists(os.path.dirname(abs_file_path)) == False:
        try:
            os.makedirs(os.path.dirname(abs_file_path) , exist_ok =True)
        except Exception as err:
            return f"Error: creating directory: {err}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as err:
        return f"Error: writing to file: {err}"

schema_write_file = types.FunctionDeclaration(
    name = "write_file",
    description = "Writes given content to a file within the working directory, can create the file if it doesn't exist.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path to the file , relative to the working directory."
            ),
            "content": types.Schema(
                type = types.Type.STRING,
                description = "Contains the content to write or overwrite in the file."
            )
        },
        required = ["file_path","content"]
    )
)
