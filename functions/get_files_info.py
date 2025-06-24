import os

def get_files_info(working_directory, directory=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        
        if directory is None:
            full_target_path = abs_working_dir
        else:
            full_target_path = os.path.abspath(os.path.join(abs_working_dir, directory))

        if not full_target_path.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.exists(full_target_path):
            return f'Error: Directory "{directory}" does not exist'
        if not os.path.isdir(full_target_path):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(full_target_path)
        output = []

        for entry in sorted(entries):
            entry_path = os.path.join(full_target_path, entry)
            is_dir = os.path.isdir(entry_path)
            file_size = 0

            if not is_dir:
                file_size = os.path.getsize(entry_path)
            
            output.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        
        return "\n".join(output)
    
    except OSError as e:
        return f'Error: an OS error occurred: {e}'
    except Exception as e:
        return f'Error: an unexpected error occurred: {e}'
        