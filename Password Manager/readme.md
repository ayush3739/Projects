# Password Manager

A secure password management application built with Tkinter that generates strong passwords and stores login credentials.

## Features
- **Strong Password Generation**: Creates random passwords with letters, numbers, and symbols
- **Automatic Clipboard Copy**: Generated passwords are automatically copied to clipboard
- **Credential Storage**: Save website, email/username, and password combinations
- **Data Persistence**: Stores all data in a text file for future access
- **User-Friendly GUI**: Clean interface with logo and intuitive controls
- **Input Validation**: Ensures all required fields are filled before saving

## Files
- `main.py` - Main password manager application with GUI
- `password generator.py` - Standalone password generator script
- `logo.png` - Application logo image
- `demo.txt` - Sample data file (created when saving passwords)

## How to Use
1. Run `main.py` to start the application
2. Enter website name and email/username
3. Click "Generate Password" for a strong random password
4. Generated password is automatically copied to clipboard
5. Click "Add" to save the credentials
6. All data is stored in `demo.txt` file

## Password Generation Features
- 8-10 random letters (uppercase and lowercase)
- 2-4 random symbols (!#$%&()*+)
- 2-4 random numbers
- All characters shuffled for maximum security

## Security Note
This is a basic implementation for learning purposes. For production use, consider:
- Encrypting stored passwords
- Using a master password
- Implementing secure database storage
- Adding password strength indicators

## Requirements
- Python 3.x
- tkinter (included with Python)
- pyperclip (for clipboard functionality)

## Installation
```bash
pip install pyperclip
python main.py
```