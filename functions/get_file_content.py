import os

MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        target_file = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file is within working directory
        if not target_file.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Check if target is a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file content
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS + 1)  # read one more to check if truncation is needed

        if len(content) > MAX_CHARS:
            return content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'

        return content

    except Exception as e:
        return f'Error: {str(e)}'
