# Exercise Tracker

An automated exercise logging system that uses natural language processing to track workouts and log them to Google Sheets.

## Features
- Natural language exercise input processing
- Automatic calorie calculation using Nutritionix API
- Logs exercise data to Google Sheets via Sheety API
- Includes date and time stamps
- User profile customization (age, weight, height)

## How It Works
1. User describes their workout in natural language
2. Nutritionix API processes the description and estimates calories
3. Exercise data is automatically logged to Google Sheets
4. Includes exercise type, duration, and calories burned

## Setup
1. Create `.env` file with API credentials:
   ```
   API_KEY=your_nutritionix_api_key
   APP_ID=your_nutritionix_app_id
   pass=your_sheety_basic_auth_token
   ```
2. Configure user profile variables (age, weight, height)
3. Set up Google Sheets with Sheety API

## API Integration
- **Nutritionix API**: Natural language exercise processing
- **Sheety API**: Google Sheets integration for data storage
- **Basic Authentication**: Secure API access

## Requirements
- Python 3.x
- requests
- python-dotenv
- Nutritionix API account
- Sheety account for Google Sheets integration
