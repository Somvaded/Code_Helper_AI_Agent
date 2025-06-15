from functions.get_files_info import get_files_info,schema_get_files_info
from functions.get_files_content import get_file_content, schema_get_file_content
from functions.run_python_file import run_python_file, schema_run_python_file
from functions.write_file import write_file, schema_write_file
from google.genai import types
from config import WORKDIR

FUNCTIONS = {
    "get_files_info": get_files_info,
    "get_file_content":get_file_content,
    "run_python_file":run_python_file,
    "write_file":write_file
}


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def call_function(function_call_part , verbose_flag =False):
    if verbose_flag:
        print(f" - Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    parameter_dict = dict(function_call_part.args)
    parameter_dict["working_directory"] = WORKDIR
    if function_call_part.name not in FUNCTIONS:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name =  function_call_part.name,
                    response = {"error": f"Unknown function: {function_call_part.name}"}
                )
            ]
        )
    required_func = FUNCTIONS[function_call_part.name]
    result = required_func(**parameter_dict)
    return types.Content(
        role= "tool",
        parts = [
            types.Part.from_function_response(
                name = function_call_part.name,
                response = {"result":result},
            )
        ]
    )







