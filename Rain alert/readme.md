# Rain Alert System

An automated weather monitoring system that sends SMS alerts when rain is expected in your area.

## Features
- **Weather Forecast Monitoring**: Checks upcoming weather conditions
- **Rain Detection**: Analyzes weather data for rain probability
- **SMS Notifications**: Sends alerts via Twilio SMS service
- **Location-based**: Uses GPS coordinates for accurate local weather
- **Automated Scheduling**: Can be set to run automatically

## How It Works
1. Fetches weather forecast for specified coordinates
2. Analyzes weather condition codes for rain indicators
3. If rain is detected in the forecast, sends SMS alert
4. Saves weather data locally for reference and debugging

## Files
- `main.py` - Main weather monitoring and alert script
- `.env` - Environment variables for API keys and settings
- `weather.json` - Saved weather data for reference

## Setup Requirements
1. **OpenWeatherMap API**: Free weather data service
2. **Twilio Account**: SMS messaging service
3. **Location Coordinates**: Your latitude and longitude

## Environment Configuration
Create `.env` file with:
```
API_KEY=your_openweathermap_api_key
ACCOUNT_ID=your_twilio_account_sid
auth_token=your_twilio_auth_token
lat=your_latitude
lon=your_longitude
```

## Weather Detection Logic
- Monitors next 12 hours of weather forecast
- Rain condition codes (typically < 700 in OpenWeatherMap)
- Sends alert if any time period shows rain probability

## SMS Alert Features
- Clear, concise rain warnings
- Include time frame for expected rain
- Friendly reminder to bring umbrella
- Customizable message content

## Automation Options
- Set up as scheduled task (cron job on Linux/Mac)
- Run as Windows Task Scheduler job
- Deploy on cloud service for 24/7 monitoring
- Integrate with home automation systems

## Example Alert Message
```
🌧️ Rain Alert! 
Rain expected in your area within the next 12 hours.
Don't forget your umbrella! ☂️
```

## Installation
```bash
pip install requests python-dotenv twilio
python main.py
```

## API Services Used
- **OpenWeatherMap**: Free tier includes current weather and 5-day forecast
- **Twilio**: Pay-per-message SMS service with free trial credits

## Customization Ideas
- Adjust time range for weather monitoring
- Add different alert types (snow, storms, etc.)
- Include temperature warnings
- Send to multiple phone numbers
- Add weather summary to messages

## Learning Concepts
- API integration and HTTP requests
- Environment variable management
- JSON data processing
- Conditional logic and decision making
- SMS service integration
- Automated notification systems

## Requirements
- Python 3.x
- requests, python-dotenv, twilio packages
- Internet connection
- Twilio and OpenWeatherMap accounts

Perfect for learning API integration while creating a practical everyday tool!