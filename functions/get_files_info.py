import os

def get_files_info(working_directory, directory=None):
    try:
        # Set directory to working_directory if not provided
        if directory is None:
            directory = working_directory

        # Get absolute paths
        working_directory = os.path.abspath(working_directory)
        target_directory = os.path.abspath(os.path.join(working_directory, directory))

        # Check if the target directory is within the working directory
        if not target_directory.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Check if target is a directory
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'

        # Build directory listing string
        result_lines = []
        for item in os.listdir(target_directory):
            item_path = os.path.join(target_directory, item)
            try:
                is_dir = os.path.isdir(item_path)
                size = os.path.getsize(item_path)
                result_lines.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: Failed to get info for "{item}": {str(e)}'

        return "\n".join(result_lines)

    except Exception as e:
        return f'Error: {str(e)}'
