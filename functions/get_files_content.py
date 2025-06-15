import os
from google.genai import types
from config import MAXCHARS
def get_file_content(working_directory, file_path):
    #max characters to get, truncate the rest
    try:
        #get absolute path and check for errors
        abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))
        if not abs_file_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(abs_file_path,"r") as f:
            file_content_string = f.read(MAXCHARS)
            if f.read(1):
                file_content_string +='[...File "{file_path}" truncated at 10000 characters]'
        return file_content_string
    except Exception as err:
        return f"Error: {err}"



schema_get_file_content = types.FunctionDeclaration(
    name = "get_file_content",
    description = "Gets the file's content from the specified file path where content is truncated at 10000 characters, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The path to the file, relative to the working directory."
            ),
        },
        required = ["file_path"]
    )
)


