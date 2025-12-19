# Flight Deals Finder

An automated flight price monitoring system that tracks cheap flight deals and sends WhatsApp notifications when prices drop below your target threshold.

## Features
- **Google Sheets Integration**: Manages destination cities and target prices via Sheety API
- **Flight Price Monitoring**: Uses Amadeus API to search for flight deals
- **IATA Code Management**: Automatically fetches and updates airport codes for cities
- **Price Comparison**: Compares current prices with your target thresholds
- **WhatsApp & Email Notifications**: Sends instant alerts via Twilio when deals are found
- **Multi-destination Support**: Monitors multiple destinations simultaneously
- **Direct & Indirect Flights**: Searches for both direct flights and flights with stopovers
- **Customer Email List**: Manages customer emails for notifications

## How It Works
1. Reads destination cities and target prices from Google Sheets
2. Fetches IATA airport codes for cities (if not already stored)
3. Searches for direct flights from origin city to each destination
4. If no direct flights found, searches for indirect flights with stopovers
5. Compares found prices with target prices in spreadsheet
6. Sends WhatsApp and email notifications when cheaper flights are discovered
7. Includes flight details: price, dates, airports, route information, and number of stops

## Files
- `main.py` - Main application logic and flight monitoring coordination
- `data_manager.py` - Google Sheets API integration via Sheety (with HTTP Basic Auth)
- `flight_search.py` - Amadeus flight search API integration
- `flight_data.py` - Flight data structure and cheapest flight finder
- `notification_manager.py` - WhatsApp and email notifications via Twilio and SMTP
- `requirements.txt` - Python package dependencies
- `readme.md` - This documentation

## Setup Requirements
1. **Google Sheets**: Spreadsheet with cities, IATA codes, and target prices
2. **Sheety API**: Free service to access Google Sheets via REST API (with Basic Auth)
3. **Amadeus Travel API**: Flight search API (free tier available)
4. **Twilio Account**: WhatsApp messaging service
5. **Gmail Account**: For sending email notifications (with app password)
6. **Python Environment**: Python 3.x with required packages

## Environment Configuration
Create `.env` file with:
```
# Sheety API (Google Sheets access with Basic Auth)
SHEETY_PRICES_ENDPOINT=your_sheety_prices_endpoint
Sheety_users_endpoint=your_sheety_users_endpoint
SHEETY_USRERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password

# Amadeus Flight API
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_api_secret

# Twilio WhatsApp Integration
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number
TWILIO_VERIFIED_NUMBER=recipient_whatsapp_number
TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number

# Email Integration (Gmail)
Email_ID=your_email@gmail.com
APP_pass=your_gmail_app_password
```

## Google Sheets Structure

### Prices Sheet
Your spreadsheet should have columns:
- `city` - Destination city name
- `iataCode` - Airport code (auto-populated by the system)
- `lowestPrice` - Your target price threshold
- `id` - Row identifier for Sheety API

### Users Sheet
For customer email notifications:
- `yourEMail` - Customer email addresses
- Additional columns as needed

## Flight Search Logic
- **Origin**: Configurable origin city (default: LON - London)
- **Search Window**: Tomorrow to 6 months from today
- **Flight Type**: First searches for direct flights, then searches for flights with stopovers if needed
- **Currency**: Indian Rupees (INR) - easily changeable
- **Results**: Top 10 cheapest options per destination
- **Stops**: Tracks number of stops (0 for direct flights)

## Notification Features
- **Deal Alerts**: Only notifies when prices drop below your target
- **Detailed Info**: Includes price, route, departure/return dates, and number of stops
- **WhatsApp Integration**: Reliable message delivery via Twilio
- **Email Notifications**: Sends to all customers in the email list
- **Stop Information**: Specifies if flight is direct or includes stopovers
- **Price Comparison**: Shows actual price vs target price

## Example Alert Messages

### Direct Flight
```
Low price alert! Only GBP 150 to fly direct 
from LON to PAR, 
on 2024-01-15 until 2024-01-22.
```

### Flight with Stops
```
Low price alert! Only GBP 180 to fly 
from LON to NYC, 
with 1 stop(s) 
departing on 2024-01-15 and returning on 2024-01-22.
```

## Installation  
```bash
pip install -r requirements.txt
python main.py
```

## Required Packages
- `python-dotenv==1.0.1` - Environment variable management
- `Requests==2.32.3` - HTTP library for API calls
- `twilio==9.1.1` - WhatsApp/SMS notifications

## API Services Used
- **Sheety**: Free Google Sheets API access (up to 1000 requests/month)
- **Amadeus**: Free tier includes 1000 flight searches/month
- **Twilio**: Pay-per-message WhatsApp service with free trial credits
- **Gmail SMTP**: Free email sending service

## Code Structure

### FlightData Class
Stores flight information with:
- `price`: Flight cost
- `origin_airport`: Origin IATA code
- `destination_airport`: Destination IATA code
- `out_date`: Departure date
- `return_date`: Return date
- `stops`: Number of stopovers

### FlightSearch Class
Handles Amadeus API integration:
- Generates authentication tokens
- Searches for IATA codes by city name
- Checks flight availability with customizable parameters
- Supports both direct and indirect flight searches

### DataManager Class
Manages Google Sheets data:
- Retrieves destination data from Sheety API
- Updates IATA codes in the spreadsheet
- Fetches customer email addresses
- Uses HTTP Basic Authentication

### NotificationManager Class
Sends notifications:
- WhatsApp messages via Twilio API
- SMS messages via Twilio API
- Email notifications via Gmail SMTP

## Customization Ideas
- Change origin city and search timeframe
- Add multiple origin cities for comparison
- Include one-way flight options
- Modify currency (currently set to INR)
- Monitor specific airlines or flight classes
- Include hotel and car rental deals
- Add price history tracking
- Customize email templates
- Add more notification channels (Slack, Telegram, etc.)

## Learning Concepts
- REST API integration and authentication (Bearer Token & Basic Auth)
- JSON data processing and parsing
- Environment variable security with python-dotenv
- Object-oriented programming design
- Error handling and API rate limiting
- Automated notification systems (WhatsApp, Email)
- Data persistence with external services (Google Sheets)
- HTTP Basic Authentication
- SMTP email integration
- Token-based API authentication

## Error Handling
- Checks for empty flight data
- Handles API rate limiting
- Manages authentication token expiration
- Validates IATA code searches
- Handles missing environment variables

## Requirements
- Python 3.x
- requests, python-dotenv, twilio packages
- Internet connection
- Active API accounts (Sheety, Amadeus, Twilio)
- Google Sheets document with destination data
- Gmail account with app password enabled

Perfect for learning API integration while building a practical travel tool that can save you money on flights!
