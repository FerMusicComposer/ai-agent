import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import llm_core as core
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
if len(sys.argv) < 2:
    print("A prompt must be provided.")
    sys.exit(1)

verbose = False
if len(sys.argv) > 2 and sys.argv[2] == "--verbose":
    verbose = True

if not core.user_prompt:
    print("A prompt must be provided.")
    sys.exit(1)

MAX_ITERATIONS = 20

print(f"User prompt:\n{core.user_prompt}")

for i in range(MAX_ITERATIONS):
    if verbose:
        print(f"\n --- Agent Iteration {i + 1}/{MAX_ITERATIONS} --- \n")

    response = client.models.generate_content(
        model=core.model,
        contents=core.messages,
        config=types.GenerateContentConfig(tools=[core.available_functions], system_instruction=core.system_prompt)
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    func_called_this_iteration = False

    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                core.messages.append(candidate.content)
            
            if response.function_calls:
                for function_call_part in response.function_calls: 
                    func_called_this_iteration = True
                    function_call_result = call_function(function_call_part, verbose)
                    core.messages.append(function_call_result)

                    if verbose:
                        response_content = function_call_result.parts[0].function_response.response if function_call_result.parts else "No response parts"
                        print(f"-> {response_content}")

    if not func_called_this_iteration:
        if response.text:
            print(f"\nFinal Response:\n{response.text}")
            break
        else:
            print("\nAgent finished without a clear text response or function call in the last iteration.")
            break
    
else:
    print(f"\nMax iterations ({MAX_ITERATIONS}) reached. Agent stopped.")
    if core.messages and core.messages[-1].parts and core.messages[-1].parts[0].text:
        print(f"Last LLM message:\n{core.messages[-1].parts[0].text}")