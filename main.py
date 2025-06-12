import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(client, messages, verbose=False):
    for iteration in range(20):
        if verbose:
            print(f"\n--- Iteration {iteration + 1} ---")

        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[available_functions]  # ✅ tools go inside the config
    ),
)


        if verbose and hasattr(response, "usage_metadata"):
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        function_called = False

        for candidate in response.candidates:
            content = candidate.content
            messages.append(content)

            for part in content.parts:
                if hasattr(part, "function_call") and part.function_call:
                    function_called = True
                    function_result = call_function(part.function_call, verbose=verbose)
                    messages.append(function_result)

        if not function_called:
            # Final result — LLM has no more function calls, just a response
            print("\nFinal response:")
            print("".join(p.text or "" for p in messages[-1].parts if hasattr(p, "text")))
            break

if __name__ == "__main__":
    main()
