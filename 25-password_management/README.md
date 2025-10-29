# Password Manager 🔒

A simple Python application to generate and save secure passwords for websites. Users can generate strong passwords, automatically copy them to the clipboard, and save them along with their email and website details in a local text file.

## Features

- Generate random passwords with letters, numbers, and symbols.
- Password is automatically copied to the clipboard for convenience.
- Save website, email/username, and password to a local `Passwords.txt` file.
- Simple and clean GUI using Tkinter.
- Built-in validation to prevent saving empty fields.
- Confirmation message before saving credentials.

## Screenshot
![img_1.png](img_1.png)

## How to Run

1. Make sure Python is installed.
2. Install required modules if not already installed:

```bash
pip install pyperclip
```

3. Run the script:

```bash
python main.py
```

4. Enter website, email/username, and generate a password.  
5. Click **Add** to save credentials to `Passwords.txt`.

## How it Works

- The user enters the website and email/username.
- Clicking **Generate Password** creates a random password containing letters, numbers, and symbols. It is automatically copied to the clipboard.
- Clicking **Add** shows a confirmation message with the entered details.
- If confirmed, the details are saved in `Passwords.txt` and the website and password fields are cleared for the next entry.

## Skills Practiced

- Python basics and loops
- Working with lists and randomization
- File handling (saving to `.txt`)
- GUI development with Tkinter
- Clipboard manipulation using `pyperclip`
- User input validation and message boxes