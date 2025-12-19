# Flight Deals Finder - User Guide

## Overview
This project helps you find and get notified about cheap flight deals. It automatically checks flight prices from your Google Sheets, compares them with current prices, and sends notifications when better deals are found.

## Prerequisites
Before you start, make sure you have:
- Python 3.x installed
- A Google account for Google Sheets
- A Twilio account (for WhatsApp/SMS notifications)
- An Amadeus API account (for flight search)
- A Gmail account (for email notifications)

## Installation

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

The required packages are:
- `requests` - For making API calls
- `python-dotenv` - For managing environment variables
- `twilio` - For sending WhatsApp/SMS notifications

### 2. Set Up API Accounts

#### Amadeus API (Flight Search)
1. Go to [Amadeus for Developers](https://developers.amadeus.com/)
2. Sign up for a free account
3. Create a new application
4. Note down your **API Key** and **API Secret**

#### Sheety API (Google Sheets Integration)
1. Create a Google Sheet with two sheets:
   - **Prices Sheet**: Columns: `city`, `iataCode`, `lowestPrice`, `id`
   - **Users Sheet**: Columns: `yourEMail`
2. Go to [Sheety](https://sheety.co/)
3. Sign up and connect your Google Sheet
4. Enable GET and PUT operations for the Prices sheet
5. Enable GET operation for the Users sheet
6. Set up Basic Authentication and note your username and password
7. Copy the API endpoints

#### Twilio (WhatsApp/SMS)
1. Sign up at [Twilio](https://www.twilio.com/)
2. Get your Account SID and Auth Token
3. For WhatsApp: Join the Twilio WhatsApp Sandbox
4. Note down your verified number and WhatsApp number

#### Gmail (Email Notifications)
1. Enable 2-Step Verification on your Gmail account
2. Generate an App Password:
   - Go to Google Account Settings > Security
   - Select "2-Step Verification"
   - Scroll to "App passwords"
   - Generate a new app password

### 3. Configure Environment Variables

Create a `.env` file in the project directory with the following:

```env
# Amadeus API
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_api_secret

# Sheety API
SHEETY_PRICES_ENDPOINT=your_sheety_prices_endpoint
Sheety_users_endpoint=your_sheety_users_endpoint
SHEETY_USRERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password

# Twilio
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=your_twilio_phone_number
TWILIO_VERIFIED_NUMBER=your_verified_phone_number
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number

# Gmail
Email_ID=your_gmail_address
APP_pass=your_gmail_app_password
```

## Google Sheets Setup

### Prices Sheet Structure
| city | iataCode | lowestPrice | id |
|------|----------|-------------|-----|
| Paris | | 5000 | 2 |
| Tokyo | | 15000 | 3 |
| New York | | 10000 | 4 |

- **city**: Destination city name
- **iataCode**: Leave empty, will be auto-filled by the program
- **lowestPrice**: Your target price threshold in your currency
- **id**: Unique row identifier (starts from 2 as row 1 is headers)

### Users Sheet Structure
| yourEMail | id |
|-----------|-----|
| user1@example.com | 2 |
| user2@example.com | 3 |

- **yourEMail**: Email addresses to receive notifications
- **id**: Unique row identifier

## How to Use

### 1. Configure Your Origin City
In `main.py`, set your origin city IATA code:
```python
ORIGIN_CITY_IATA = "LON"  # Change to your city code (e.g., "NYC", "DEL", "BOM")
```

### 2. Add Destinations to Google Sheet
1. Open your Google Sheet (Prices sheet)
2. Add destination cities and target prices
3. Leave the `iataCode` column empty

### 3. Add Email Recipients
1. Go to the Users sheet in your Google Sheet
2. Add email addresses of people who should receive notifications

### 4. Run the Program
```bash
python main.py
```

## What the Program Does

1. **Fetches Destination Data**: Reads your destination cities from Google Sheets
2. **Gets IATA Codes**: Automatically fetches airport codes for cities that don't have them
3. **Updates Google Sheet**: Saves the IATA codes back to your sheet
4. **Searches for Flights**: 
   - Searches for direct flights first
   - If no direct flights found, searches for flights with stopovers
   - Search window: Tomorrow to 6 months from today
5. **Compares Prices**: Checks if found prices are lower than your target prices
6. **Sends Notifications**: 
   - Sends WhatsApp messages
   - Sends emails to all recipients in your Users sheet

## Customization Options

### Change Search Timeframe
In `main.py`, modify:
```python
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
```

### Change Currency
In `flight_search.py`, update the `check_flights` method:
```python
"currencyCode": "INR",  # Change to "USD", "EUR", "GBP", etc.
```

### Modify Number of Flight Results
In `flight_search.py`, change:
```python
"max": "10",  # Number of results to fetch
```

### Enable/Disable Notifications
In `main.py`, comment/uncomment notification methods:
```python
# notification_manager.send_sms(message_body=message)  # SMS (commented out)
notification_manager.send_whatsapp(message_body=message)  # WhatsApp
notification_manager.send_emails(email_list=emails_list, email_body=message)  # Email
```

## Code Structure

### main.py
Main execution file that:
- Initializes all components
- Coordinates the flight search process
- Handles notifications

### data_manager.py
Manages Google Sheets integration:
- Fetches destination data
- Updates IATA codes
- Retrieves customer emails

### flight_search.py
Handles Amadeus API integration:
- Generates authentication tokens
- Searches for IATA codes
- Queries flight availability

### flight_data.py
Processes flight information:
- Defines FlightData class
- Finds cheapest flights from search results

### notification_manager.py
Manages all notifications:
- Sends SMS via Twilio
- Sends WhatsApp messages via Twilio
- Sends emails via Gmail SMTP

## Troubleshooting

### "No airport code found"
- Check if the city name is spelled correctly
- Try using a major city nearby
- Some smaller cities might not have airport data

### API Rate Limiting
- The program includes `time.sleep(2)` to prevent rate limiting
- If you still hit limits, increase the sleep duration

### WhatsApp Not Working
- Make sure you've joined the Twilio WhatsApp Sandbox
- Verify your WhatsApp number is correctly formatted
- Check that you've sent the join code to the sandbox number

### Email Not Sending
- Verify your Gmail app password is correct
- Check that 2-Step Verification is enabled on your Google account
- Some email providers might block SMTP access

### Missing Environment Variables
- Double-check all variables in your `.env` file
- Make sure there are no spaces around the `=` sign
- Ensure the `.env` file is in the same directory as your Python files

## Best Practices

1. **API Credits**: Both Amadeus and Twilio have free tiers with limits. Monitor your usage.
2. **Run Schedule**: Consider running the script once daily to conserve API credits
3. **Target Prices**: Set realistic target prices based on historical data
4. **Email List**: Don't add too many recipients to avoid spam filters
5. **Security**: Never commit your `.env` file to version control

## Tips for Beginners

- Start with just one or two destinations to test
- Use the print statements to debug and understand the flow
- Check your Google Sheet after the first run to see IATA codes
- Test with a higher target price first to ensure notifications work
- Keep your API keys secure and never share them

## Learning Objectives

This project teaches you:
- REST API integration (Amadeus, Sheety, Twilio)
- Environment variable management
- Object-oriented programming in Python
- JSON data processing
- Error handling
- Email and SMS automation
- Working with external services

## Support and Resources

- [Amadeus API Documentation](https://developers.amadeus.com/self-service)
- [Sheety Documentation](https://sheety.co/docs)
- [Twilio Documentation](https://www.twilio.com/docs)
- [Python Requests Documentation](https://requests.readthedocs.io/)

Happy flight hunting! ✈️
