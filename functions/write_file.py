import os

def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Check if file_path is within the working_directory
        if not target_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Write content to file
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {str(e)}'
