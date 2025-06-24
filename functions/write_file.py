import os

def write_file(working_directory, file_path, content):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        full_target_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

        if not full_target_path.startswith(abs_working_dir):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.exists(full_target_path) and not os.path.isfile(full_target_path):
            return f'Error: "{file_path}" is not a file'
        
        os.makedirs(os.path.dirname(full_target_path), exist_ok=True)

        with open(full_target_path, 'w', encoding='utf-8', errors='ignore') as file:
            file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except IOError as e:
        return f'Error: An I/O error occurred while writing "{file_path}": {e}'
    except Exception as e:
        return f'Error: An unexpected error occurred while writing "{file_path}": {e}'