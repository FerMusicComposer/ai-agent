# Gemini CLI AI Agent

This is a project from [boot.dev](https://boot.dev) which consisted in creating a CLI coding agent using [Gemini 2.0 Flash](https://github.com/google/genai) as a model.

The goal of this project was to make the agent interact with the contents of an specific directory, which for security reasons is the only place where the agent can read and modify files, and also run Python scripts.
It is basically a toy version of tools like Claude Code or Gemini CLI

The agent is able to:

* List files and directories
* Read the contents of a file
* Write to a file (if it does not exist, create it)
* Run a Python file

The agent is also able to answer to user questions regarding the contents of the directory. It can also fix bugs in the code if you point it to them. Just type in the CLI and the agent will answer.

Here's an example:
```
$ python3 main.py "how does the calculator render results to the console?"

# Output
# User prompt:
# how does the calculator render results to the console?
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: get_files_info
# Calling function: get_file_content
# 
# Final Response:
# The `render` function in `pkg/render.py` takes the expression and the result as input and formats them into a box-like structure using ASCII characters. Here's a breakdown:
# 
# 1.  **Formats the result:** It checks if the result is a float with an integer value (e.g., 5.0). If so, it converts it to an integer string (e.g., "5"). Otherwise, it converts the result to a string.
# 2.  **Calculates box width:** It determines the width of the box based on the lengths of the expression and the result string, adding 4 for padding.
# 3.  **Builds the box:** It creates a list of strings, each representing a line of the box. The box includes the expression and the result, padded with spaces.
# 4.  **Joins the lines:** It joins the lines of the box with newline characters to create a single string.
# 
# Finally, the `main` function in `main.py` prints this formatted string to the console.

```

If you want to try it (Not recommended):

1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Create a .env file and add your Gemini key (***WARNING!!!*** If you do this, remember to ***include your .env file in your .gitignore***)
4. Run the program with `python3 main.py "your question here"`

***IMPORTANT***
Please understand this is a toy version of tools like Claude Code or Open Code. Even those tools, with the amazing teams behind them, are not completely secure.
This project has implemented enough guard rails to ensure the agent wont run wild through your directories wrecking havoc, but don't trust it. 
***Read the code before executing it to make sure you understand what it does.***
