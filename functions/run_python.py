import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        working_directory = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(working_directory, file_path))

        # Validate path
        if not target_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(target_path):
            return f'Error: File "{file_path}" not found.'

        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        # Run the Python file
        result = subprocess.run(
            ["python", target_path],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_directory
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        output_parts = []
        if stdout:
            output_parts.append(f"STDOUT:\n{stdout}")
        if stderr:
            output_parts.append(f"STDERR:\n{stderr}")
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if not output_parts:
            return "No output produced."

        return "\n\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
