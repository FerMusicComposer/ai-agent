import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def run_tests():
    print("--- Running get_files_info tests ---")
    working_directory_base = os.path.abspath(os.path.dirname(__file__))
    calculator_path = os.path.join(working_directory_base, "calculator")

    project_root = os.path.abspath(os.path.dirname(__file__))
    print(f"Working directory: {working_directory_base}")
    print(f"Project root: {project_root}")
    print(f"Calculator path: {calculator_path}")

    # print("\nTest Case 1: get_files_info('calculator', '.')")
    # result1 = get_files_info(calculator_path, ".")
    # print(result1)

    # print("\nTest Case 2: get_files_info('calculator', 'pkg')")
    # result2 = get_files_info(calculator_path, "pkg")
    # print(result2)

    # print("\nTest Case 3: get_files_info('calculator', '/bin') (should be an error)")
    # result3 = get_files_info(calculator_path, "/bin")
    # print(result3)

    # print("\nTest Case 4: get_files_info('calculator', '../') (should be an error)")
    # result4 = get_files_info(calculator_path, "../")
    # print(result4)

    # print("\nTest Case 5: get_files_info('calculator', 'non_existent_dir') (should be an error)")
    # result5 = get_files_info(calculator_path, "non_existent_dir")
    # print(result5)

    # print("\nTest Case 6: get_files_info('calculator', 'main.py') (should be an error - not a directory)")
    # result6 = get_files_info(calculator_path, "main.py")
    # print(result6)

    MAX_CHARS = 10000
    print("\nTest Case: Truncation with lorem.txt (requires 'calculator/lorem.txt' to exist)")
    try:
        result_lorem = get_file_content(calculator_path, "lorem.txt")
        print(f"Content length: {len(result_lorem)}")
        if len(result_lorem) > 10000:
            print("Truncation expected and message appears to be present.")
        else:
            print("Truncation status unclear or not as expected. Check lorem.txt content.")
        print("-" * 30) 
    except Exception as e:
        print(f"Error during lorem.txt test: {e}")


    # --- Remaining Test Cases ---
    print("\nTest Case 1: get_file_content('calculator', 'main.py')")
    result1 = get_file_content(calculator_path, "main.py")
    print(result1)

    print("\nTest Case 2: get_file_content('calculator', 'pkg/calculator.py')")
    result2 = get_file_content(calculator_path, "pkg/calculator.py")
    print(result2)

    print("\nTest Case 3: get_file_content('calculator', '/bin/cat') (should be an error)")
    result3 = get_file_content(calculator_path, "/bin/cat")
    print(result3)

    print("\nTest Case 4: get_file_content('calculator', '../.gitignore') (should be an error)")
    result4 = get_file_content(calculator_path, "../.gitignore")
    print(result4)

    print("\nTest Case 5: get_file_content('calculator', 'non_existent_file.txt') (should be an error)")
    result5 = get_file_content(calculator_path, "non_existent_file.txt")
    print(result5)

    print("\nTest Case 6: get_file_content('calculator', '.') (should be an error - not a file)")
    result6 = get_file_content(calculator_path, ".")
    print(result6)

    print("\n--- Tests finished ---")

if __name__ == "__main__":
    run_tests()
