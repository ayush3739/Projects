# Stock News Messenger

A stock monitoring system that tracks significant price changes and sends relevant news updates via SMS.

## Features
- Monitors stock price movements for specified companies
- Detects significant price changes (customizable threshold)
- Fetches relevant news articles when price changes occur
- Sends SMS notifications with stock info and news via Twilio
- Modular design with separate modules for stock and news handling

## Files
- `main.py` - Main application logic and coordination
- `Stock_handle.py` - Stock price monitoring and analysis
- `news_data.py` - News article fetching and processing
- `readme.md` - This documentation

## How It Works
1. Monitors specified stock (default: Tesla/TSLA)
2. Compares current price with previous day's closing price
3. If significant change detected, fetches relevant news
4. Sends SMS notification with:
   - Stock symbol and price change percentage
   - Brief news headline and description
   - Company name for context

## Setup
1. Create `.env` file with required API credentials:
   ```
   ACCOUNT_ID=your_twilio_account_sid
   auth_token=your_twilio_auth_token
   what_from=your_twilio_phone_number
   what_to=recipient_phone_number
   STOCK_API_KEY=your_stock_api_key
   NEWS_API_KEY=your_news_api_key
   ```
2. Install required packages:
   ```bash
   pip install requests twilio python-dotenv
   ```

## Configuration
- Modify `STOCK` and `COMPANY_NAME` variables for different stocks
- Adjust price change threshold for notifications
- Customize SMS message format as needed

## Requirements
- Python 3.x
- Twilio account for SMS
- Stock API access (Alpha Vantage or similar)
- News API access
- requests, twilio, python-dotenv packages
