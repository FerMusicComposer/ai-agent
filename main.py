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

response = client.models.generate_content(
    model=core.model,
    contents=core.messages,
    config=types.GenerateContentConfig(tools=[core.available_functions], system_instruction=core.system_prompt)
)

if verbose:
    print(f"User prompt:\n{core.user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if response.function_calls is not None:
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        print(f"-> {function_call_result.parts[0].function_response.response}")
else:
    print(f"Response:\n{response.text}")