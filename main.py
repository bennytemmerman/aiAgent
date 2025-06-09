import os
import sys
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.environ.get("GEMINI_API_KEY")

# Check if a prompt was provided
if len(sys.argv) < 2:
    print("Error: No prompt provided.")
    print("Usage: python main.py \"Your prompt here\"")
    sys.exit(1)

# Join all command-line arguments into a single prompt string
user_prompt = " ".join(sys.argv[1:])

# Initialize the Gemini client
client = genai.Client(api_key=api_key)

# Generate content using the provided prompt
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=user_prompt
)

# Print the model's response
print("\nResponse:")
print(response.text)

# Print token usage
print(f"\nPrompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

