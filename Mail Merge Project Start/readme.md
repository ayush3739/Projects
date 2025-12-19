# Mail Merge Project

An automated mail merge system that generates personalized letters from templates by replacing placeholders with actual names.

## Features
- Bulk letter generation from templates
- Name placeholder replacement
- Automatic file creation for each recipient
- Customizable letter templates
- Batch processing of recipient lists

## How It Works
1. Reads a template letter with [name] placeholder
2. Loads recipient names from a text file
3. Creates personalized letters by replacing placeholders
4. Saves individual letter files for each recipient
5. Outputs all letters to "ReadyToSend" folder

## Files
- `main.py` - Main mail merge script
- `Input/Letters/starting_letter.txt` - Letter template
- `Input/Names/invited_names.txt` - List of recipient names
- `Output/ReadyToSend/` - Generated personalized letters

## Template Format
The starting letter uses `[name]` as a placeholder:
```
Dear [name],

You are invited to my birthday party on Saturday.

Hope you can make it!

Angela
```

## Output
Each recipient gets a personalized file:
- `letter_for_John.txt`
- `letter_for_Mary.txt`
- `letter_for_David.txt`
- etc.

## Use Cases
- Birthday party invitations
- Business announcements
- Wedding invitations
- Marketing campaigns
- Event notifications

## Requirements
- Python 3.x
- Text files with names (one per line)
- Letter template with placeholders

## Usage
```bash
python main.py
```

## Learning Concepts
- File I/O operations
- String manipulation and replacement
- List processing
- Path handling
- Automation workflows
- Template systems

## Customization
- Modify the template letter as needed
- Add more placeholders (dates, locations, etc.)
- Change output file naming convention
- Process different file formats

Perfect for learning file manipulation while creating a practical office automation tool!