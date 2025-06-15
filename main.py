import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from call_function import call_function,available_functions
from prompt import system_prompt
from config import MAX_ITERATION

def main():
    #load the .env
    load_dotenv()

    #get api key and create client with it 
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key = api_key)
    verbose_flag = False

    #   check if the prompt is passed
    if len(sys.argv) < 2:
        print("Prompt not provided")
        sys.exit(1)

    #check the --verbose tag to take care of noisy output
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose": 
        verbose_flag = True


    user_prompts = sys.argv[1]
    messages = [
        types.Content(
            role = "user" , 
            parts = [types.Part(text = user_prompts)]) 
        ]
    if verbose_flag:
        print(f"User Prompt: {user_prompts}\n")

    iteration = 0

    while True:
        iteration +=1 
        if iteration > MAX_ITERATION:
            print(f"Maximum iteration ({MAX_ITERATION}) reached.")
            sys.exit(1)
        try:
            final_response = generate_response(client, messages, verbose_flag)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as err:
            print(f"Error in generating response: {err}")



def generate_response(client , messages, verbose_flag):

    response = client.models.generate_content(
        model = 'gemini-2.0-flash-001' ,
        contents = messages,
        config = types.GenerateContentConfig(
            tools = [available_functions],
            system_instruction = system_prompt,
        )
    )

    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    if verbose_flag == True:
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {response_tokens}")

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        return response.text

    function_responses = []

    if response.function_calls:
        for func in response.function_calls:
            function_result = call_function(func,verbose_flag)
            if(
                not function_result.parts 
                or not function_result.parts[0].function_response
            ):
                raise Exception("empty function call result")
            if verbose_flag:
                print(f"-> {function_result.parts[0].function_response.response}")
            function_responses.append(function_result.parts[0])
    if not function_responses:
        raise Exception("no functions generated...")
    messages.append(types.Content(
        role = "tool",
        parts = function_responses
    ))
if __name__ =="__main__":
    main()
