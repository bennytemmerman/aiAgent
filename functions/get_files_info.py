import os

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = working_directory
            # Resolve absolute paths
            working_directory = os.path.abspath(working_directory)
            directory = os.path.abspath(directory)

        # Check if directory is within working_directory
        if not os.path.commonpath([directory, working_directory]) == working_directory:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            directory = os.path.abspath(directory)
            working_directory = os.path.abspath(working_directory)

            if not directory.startswith(working_directory):
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(directory):
            return f'Error: "{directory}" is not a directory'

        output_lines = []
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            try:
                file_size = os.path.getsize(full_path)
                is_dir = os.path.isdir(full_path)
                output_lines.append(f'- {entry}: file_size={file_size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: {str(e)}'

        return "\n".join(output_lines)

    except Exception as e:
        return f'Error: {str(e)}'

