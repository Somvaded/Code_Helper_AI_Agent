# Gemini Function Calling Demo

This project demonstrates how to use the Gemini API for function calling to interact with a local file system. It allows the Gemini model to list files, read file content, run Python files, and write files.

## Features

*   **Function Calling:** Uses the Gemini API to enable function calls for file system interaction.
*   **File System Access:** Provides functions to list files, read file content, run Python files, and write files within a defined working directory.
*   **Configurable:** Uses a configuration file (`config.py`) to define constants such as the working directory and maximum iteration count.
*   **Verbose Mode:** Includes a verbose mode to provide detailed output for debugging and monitoring.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Set up a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Linux and macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your Gemini API key:**
    *   Obtain an API key from the Google AI Studio.
    *   Create a `.env` file in the project directory.
    *   Add your API key to the `.env` file:
        ```
        GEMINI_API_KEY=YOUR_API_KEY
        ```

## Usage

1.  **Run the `main.py` script:**
    ```bash
    python main.py "your prompt here"
    ```
    Replace `"your prompt here"` with the prompt you want to send to the Gemini model.

2.  **Optional: Use verbose mode:**
    ```bash
    python main.py "your prompt here" --verbose
    ```
    The `--verbose` flag enables detailed output, including token counts and function call information.

## Project Structure

```
├── README.md
├── main.py           # Main script to run the application
├── call_function.py  # Module to handle function calls
├── config.py         # Configuration file
├── prompt.py         # Contains system prompts
├── functions/        # Directory containing the function definitions
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── run_python_file.py
│   └── write_file.py
├── requirements.txt  # List of dependencies
├── .env              # Environment variables (API key)
└── .gitignore        # Specifies intentionally untracked files that Git should ignore
```

## Working Project directory

1. Configure the working directory in config.py .
