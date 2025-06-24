import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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

    # MAX_CHARS = 10000
    # print("\nTest Case: Truncation with lorem.txt (requires 'calculator/lorem.txt' to exist)")
    # try:
    #     result_lorem = get_file_content(calculator_path, "lorem.txt")
    #     print(f"Content length: {len(result_lorem)}")
    #     if len(result_lorem) > 10000:
    #         print("Truncation expected and message appears to be present.")
    #     else:
    #         print("Truncation status unclear or not as expected. Check lorem.txt content.")
    #     print("-" * 30) 
    # except Exception as e:
    #     print(f"Error during lorem.txt test: {e}")

    # print("\nTest Case 1: get_file_content('calculator', 'main.py')")
    # result1 = get_file_content(calculator_path, "main.py")
    # print(result1)

    # print("\nTest Case 2: get_file_content('calculator', 'pkg/calculator.py')")
    # result2 = get_file_content(calculator_path, "pkg/calculator.py")
    # print(result2)

    # print("\nTest Case 3: get_file_content('calculator', '/bin/cat') (should be an error)")
    # result3 = get_file_content(calculator_path, "/bin/cat")
    # print(result3)

    # print("\nTest Case 4: get_file_content('calculator', '../.gitignore') (should be an error)")
    # result4 = get_file_content(calculator_path, "../.gitignore")
    # print(result4)

    # print("\nTest Case 5: get_file_content('calculator', 'non_existent_file.txt') (should be an error)")
    # result5 = get_file_content(calculator_path, "non_existent_file.txt")
    # print(result5)

    # print("\nTest Case 6: get_file_content('calculator', '.') (should be an error - not a file)")
    # result6 = get_file_content(calculator_path, ".")
    # print(result6)

    # print("\nTest Case 1: write_file('calculator', 'lorem.txt', 'wait, this isn't lorem ipsum')")
    # # First, ensure lorem.txt exists, perhaps with some initial content
    # lorem_file_path = os.path.join(calculator_path, "lorem.txt")
    # with open(lorem_file_path, 'w', encoding='utf-8') as f:
    #     f.write("Original lorem ipsum content.")
    # result1 = write_file(calculator_path, "lorem.txt", "wait, this isn't lorem ipsum")
    # print(result1)
    # # Verify content
    # if "Successfully wrote" in result1:
    #     written_content = get_file_content(calculator_path, "lorem.txt")
    #     print(f"Content read back: '{written_content}'")
    #     if written_content == "wait, this isn't lorem ipsum":
    #         print("Content verified.")
    #     else:
    #         print("Content verification FAILED.")
    # os.remove(lorem_file_path) # Clean up

    # print("\nTest Case 2: write_file('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet')")
    # morelorem_file_path = os.path.join(calculator_path, "pkg", "morelorem.txt")
    # result2 = write_file(calculator_path, "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    # print(result2)
    # # Verify content
    # if "Successfully wrote" in result2:
    #     written_content = get_file_content(calculator_path, "pkg/morelorem.txt")
    #     print(f"Content read back: '{written_content}'")
    #     if written_content == "lorem ipsum dolor sit amet":
    #         print("Content verified.")
    #     else:
    #         print("Content verification FAILED.")
    # os.remove(morelorem_file_path) # Clean up

    # print("\nTest Case 3: write_file('calculator', '/tmp/temp.txt', 'this should not be allowed')")
    # # Note: On some systems, /tmp might not be writable or accessible this way.
    # # The error should still be about being outside the permitted working directory.
    # result3 = write_file(calculator_path, "/tmp/temp.txt", "this should not be allowed")
    # print(result3)
    # if "Error: Cannot write to" in result3 and "outside the permitted working directory" in result3:
    #     print("Error message for outside directory correctly received.")
    # else:
    #     print("Expected error for outside directory not received or incorrect.")

    # print("\nTest Case 4: write_file('calculator', 'pkg', 'trying to write to a directory')")
    # result4 = write_file(calculator_path, "pkg", "trying to write to a directory")
    # print(result4)
    # if "Error:" in result4 and "is not a file" in result4:
    #     print("Error message for writing to a directory correctly received.")
    # else:
    #     print("Expected error for writing to a directory not received or incorrect.")
    
    print("\nTest Case 1: run_python_file('calculator', 'main.py')")
    result1 = run_python_file(calculator_path, "main.py")
    print(result1)

    print("\nTest Case 2: run_python_file('calculator', 'tests.py')")
    result2 = run_python_file(calculator_path, "tests.py")
    print(result2)

    print("\nTest Case 3: run_python_file('calculator', '../main.py') (should be an error)")
    result3 = run_python_file(calculator_path, "../main.py")
    print(result3)
    if "Error: Cannot run" in result3 and "outside the permitted working directory" in result3:
        print("Error message for outside directory correctly received.")
    else:
        print("Expected error for outside directory not received or incorrect.")

    print("\nTest Case 4: run_python_file('calculator', 'nonexistent.py') (should be an error)")
    result4 = run_python_file(calculator_path, "nonexistent.py")
    print(result4)
    if "Error: File" in result4 and "not found" in result4:
        print("Error message for nonexistent file correctly received.")
    else:
        print("Expected error for nonexistent file not received or incorrect.")

    print("\n--- Tests finished ---")

if __name__ == "__main__":
    run_tests()
