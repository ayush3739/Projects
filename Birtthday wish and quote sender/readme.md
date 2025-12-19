# Birthday Wish and Quote Sender

An automated system that sends personalized birthday emails to people on their special day.

## Features
- Reads birthday data from CSV file
- Checks daily for birthdays matching current date
- Randomly selects from multiple email templates
- Personalizes emails with recipient's name
- Sends emails automatically via Gmail SMTP

## Files
- `Automatic_birthdaysend.py` - Main script
- `birthdays.csv` - Birthday database with names, emails, and dates
- `letter_1.txt`, `letter_2.txt`, `letter_3.txt` - Email templates
- `quotes.txt` - Additional quotes (if used)

## Setup
1. Update `birthdays.csv` with contact information
2. Configure your email credentials in the script:
   - Replace "Your mail here" with your Gmail address
   - Replace "Your pass key" with your Gmail app password
3. Ensure Gmail 2-factor authentication and app passwords are set up

## How It Works
1. Script reads the birthday database
2. Checks if today matches any birthday
3. If match found, selects random email template
4. Replaces [NAME] placeholder with person's actual name
5. Sends personalized birthday email

## Requirements
- Python 3.x
- pandas
- smtplib (built-in)
- Gmail account with app password
