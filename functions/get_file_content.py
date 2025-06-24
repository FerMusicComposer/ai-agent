import os

def get_file_content(working_directory, file_path):
    MAX_CHARS = 10000

    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_target_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not full_target_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(full_target_path):
            return f'Error: File "{file_path}" does not exist'
        if not os.path.isfile(full_target_path):
            return f'Error: "{file_path}" is not a file'

        with open(full_target_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        if len(content) > MAX_CHARS:
            original_len = len(content)
            content = content[:MAX_CHARS]
            content += f'\n[...File "{file_path}"  truncated ar {MAX_CHARS} characters from {original_len}]'

        return content
    
    except IOError as e:
        return f'Error: An I/O error occurred while reading "{file_path}": {e}'
    except Exception as e:
        return f'Error: An unexpected error occurred while reading "{file_path}": {e}'