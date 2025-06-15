import os
from google.genai import types

def get_files_info(working_directory , directory = None):
    try:
        if directory == None:
            directory = "."
        working_path  = os.path.abspath(working_directory)
        directory_path =os.path.abspath(os.path.join(working_path , directory))
        if directory_path.startswith(working_path)== False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if os.path.isdir(directory_path) == False:
            return f'Error: "{directory}" is not a directory'
        contents = os.listdir(directory_path)
        res = []
        for content in contents:
            name = content
            content_path = os.path.join(directory_path , content)
            file_size = os.path.getsize(content_path)
            is_dir =  os.path.isdir(content_path)
            string_line = f'- {name}: file_size={file_size} bytes, is_dir={is_dir}'
            res.append(string_line)
        return "\n".join(res)
    except Exception as err:
        return f"Error:{err}"

#Schemas for function declaration
schema_get_files_info = types.FunctionDeclaration(
    name = "get_files_info",
    description = "Lists files in a specified directory along with their sizes and if directory is not provided list all the files in the working directory, constrained to the working directory.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type = types.Type.STRING,
                description = "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself."
            ),
        },
    )
)
