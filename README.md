# Spammer Bot

## Description

**Spammer Bot** is a Python script designed to automate sending messages repeatedly for fun purposes. It allows users to define a custom message and the number of times it should be sent. Please use it responsibly and do not misuse it.

## Features

- Sends a user-defined message a specified number of times.
- Safety limit of 1000 messages to prevent excessive spamming.
- Waits for a specified time to allow users to position the cursor in the desired input field.
- Simple user interaction with prompts and feedback.

## Requirements

- Python 3.x
- `pyautogui` library
- `keyboard` library
- `pyinstaller` (for creating the executable)

## Installation

1. Clone this repository or download the `Spammer.py` file.
2. Install the required libraries using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script using Python:
   ```bash
   python Spammer.py
   ```
2. Follow the on-screen instructions:
   - Enter the number of messages you want to send (up to 1000).
   - Enter the message you want to spam.
   - Position your cursor in the input field where you want the messages to be sent.
   - Wait for the countdown to complete, and the spamming will begin.

## Creating Executable

To create a standalone executable file using `pyinstaller`:

1. Install `pyinstaller` if you haven't already:
   ```bash
   pip install pyinstaller
   ```
2. Create the executable:
   ```bash
   pyinstaller --onefile Spammer.py
   ```
3. The executable file (`Spammer.exe`) will be created in the `dist` directory.

## Safety and Responsibility

- This script is intended for fun and educational purposes only.
- Do not use this script to spam, harass, or annoy others.
- Misuse of this script can lead to consequences, and the author is not responsible for any misuse.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Jone Santhanaraj**

## Disclaimer

Please use this script responsibly. The author is not responsible for any misuse or damage caused by this script.
