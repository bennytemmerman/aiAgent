import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.environ.get("GEMINI_API_KEY")

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    print("Usage: python main.py \"Your prompt here\"")
    sys.exit(1)

# Extract --verbose flag if present
verbose = False
args = sys.argv[1:]

if "--verbose" in args:
    verbose = True
    args.remove("--verbose")

# Join remaining args as the prompt
user_prompt = " ".join(args)

if not user_prompt:
    print("Error: No prompt provided.")
    print("Usage: python main.py \"Your prompt here\" [--verbose]")
    sys.exit(1)

# Create the messages list using types.Content
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Generate content using the provided prompt
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

# Print the model's response
print("\nResponse:")
print(response.text)

# If verbose, show prompt and token usage
if verbose:
    print(f"\nUser prompt: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
