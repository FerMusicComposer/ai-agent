import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_target_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not full_target_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_target_path):
            return f'Error: File "{file_path}" not found'
        if not os.path.isfile(full_target_path):
            return f'Error: "{file_path}" is not a file'
        if not full_target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        result = subprocess.run(['python', full_target_path], check=True, timeout=30, capture_output=True, text=True, cwd=abs_working_dir)
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        if not result.stdout and not result.stderr:
            return 'No output produced.'
        output = []
        if result.stdout:
            output.append('STDOUT:')
            output.append(result.stdout)
        if result.stderr:
            output.append('STDERR:')
            output.append(result.stderr)
        return '\n'.join(output)

    except subprocess.CalledProcessError as e:
        return f'Error: Process exited with code {e.returncode}'
    except subprocess.TimeoutExpired as e:
        return f'Error: Process timed out after {e.timeout} seconds'
    except Exception as e:
        return f"Error: executing Python file: {e}"
