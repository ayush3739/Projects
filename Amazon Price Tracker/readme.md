# Day 47 - Amazon Price Tracker

This folder contains a price tracking application that monitors Amazon product prices and sends email alerts when prices drop below a target threshold.

## 📁 Files Overview

- **`main.py`** - Main application for price tracking and email alerts
- **`readme.md`** - Brief project description
- **`header.ipynb`** - Jupyter notebook for testing and development
- **`.env`** - Environment variables for email credentials (not included, must be created)

## 🎯 Project Overview

This project:
1. Scrapes Amazon product pages for current prices
2. Extracts product title and price information
3. Compares the price against a target threshold
4. Sends email alerts when prices drop below the target
5. Uses environment variables for secure credential management

## 🎯 Topics Covered

### 1. Web Scraping Amazon
- Handling complex HTTP headers for Amazon
- Using custom User-Agent to avoid blocking
- Parsing HTML with BeautifulSoup
- Extracting price from `span.a-offscreen` elements
- Extracting product titles from `span#productTitle`
- Text processing to clean whitespace and newlines

### 2. Email Automation
- **SMTP**: Simple Mail Transfer Protocol
- Gmail SMTP server configuration
- TLS encryption with `starttls()`
- Email authentication
- `EmailMessage` class for composing emails
- Setting email headers (From, To, Subject)
- UTF-8 encoding for email content

### 3. Environment Variables
- **python-dotenv**: Loading environment variables from `.env` file
- Secure credential storage
- Using `os.getenv()` to access variables
- Keeping sensitive data out of source code

### 4. Data Processing
- String splitting and parsing (e.g., `split('$')`)
- Float conversion for price comparison
- Text cleaning with `split()` and `join()`
- Conditional logic for price thresholds

## 🔧 Setup Requirements

### Prerequisites
```bash
pip install beautifulsoup4 requests python-dotenv
```

### Environment Variables
Create a `.env` file in the Day 47 directory:
```env
email=your_email@gmail.com
pass=your_app_password
to_email=recipient@example.com
```

### Gmail App Password
1. Enable 2-factor authentication on your Google account
2. Go to Google Account settings → Security → App Passwords
3. Generate an app password for "Mail"
4. Use this password in your `.env` file (not your regular password)

## 🎯 Features

### Amazon Product Scraping
- Custom headers to mimic browser requests
- Extracts current price from Amazon product pages
- Handles dynamic pricing
- Cleans and formats product titles
- Works with both static test sites and live Amazon

### Price Monitoring
- Configurable target price threshold
- Automatic price comparison
- Triggers alerts when price drops

### Email Alerts
- Professional email formatting
- Price drop notifications
- Product title in subject line
- Current price in email body
- Error handling for failed sends

### Security Features
- Environment variable-based credential management
- No hardcoded passwords
- Secure SMTP with TLS encryption

## 📚 Documentation Links

### Web Scraping
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [HTTP Headers Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

### Email with Python
- [Python smtplib](https://docs.python.org/3/library/smtplib.html)
- [EmailMessage Documentation](https://docs.python.org/3/library/email.message.html)
- [Gmail SMTP Settings](https://support.google.com/mail/answer/7126229)

### Environment Variables
- [python-dotenv Documentation](https://pypi.org/project/python-dotenv/)
- [Python os.getenv()](https://docs.python.org/3/library/os.html#os.getenv)

## 🚀 Getting Started

### Step 1: Install Dependencies
```bash
pip install beautifulsoup4 requests python-dotenv
```

### Step 2: Create `.env` File
```env
email=your_gmail@gmail.com
pass=your_16_char_app_password
to_email=alert_recipient@example.com
```

### Step 3: Update Product URL
Edit `main.py` and set your target Amazon product:
```python
live_site = "https://www.amazon.com/dp/YOUR_PRODUCT_ID"
target = 100.00  # Your target price
```

### Step 4: Run the Application
```bash
cd "Day 47"
python main.py
```

## 📝 Code Example

```python
# Scrape Amazon price
response = requests.get(live_site, headers=HEADERS)
soup = BeautifulSoup(response.text, 'html.parser')
web_price = float(soup.find(name="span", class_="a-offscreen").get_text().split('$')[1])

# Check price and send alert
if web_price < target:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=passw)
        
        msg = EmailMessage()
        msg["From"] = my_email
        msg["To"] = to_email
        msg["Subject"] = f"Price drop: {product_title}"
        msg.set_content(f"{product_title} is now ${web_price:.2f}")
        
        connection.send_message(msg)
```

## 🎯 Headers Explained

The script uses comprehensive headers to appear as a legitimate browser:
- **User-Agent**: Identifies as Firefox browser
- **Accept**: Specifies accepted content types
- **Accept-Language**: Browser language preferences
- **Accept-Encoding**: Supported compression methods
- **DNT**: Do Not Track preference
- **Sec-Fetch-\***: Browser security headers

## 📝 Key Learning Points

- Web scraping e-commerce websites with anti-bot protection
- Crafting realistic HTTP headers to avoid blocking
- Email automation with Python's smtplib
- Secure credential management with environment variables
- Price monitoring and comparison logic
- Error handling for network and email issues
- Text processing and data extraction
- Combining multiple technologies (scraping + email)
- Building practical automation tools
- SMTP protocol and Gmail integration

## ⚠️ Important Notes

### Security
- Never commit `.env` file to version control
- Use app passwords, not your main Google password
- Keep credentials secure and private

### Web Scraping Ethics
- Respect Amazon's robots.txt and terms of service
- Don't overwhelm servers with frequent requests
- Consider using Amazon's Product Advertising API for commercial use
- Website structure may change; selectors might need updates

### Email Limits
- Gmail has daily sending limits
- Use app passwords for enhanced security
- Some email providers may block automated emails
- Test with static site first before using live Amazon

## 🔄 Automation Ideas

Consider scheduling this script to run automatically:
- **Cron job** (Linux/Mac): `0 9 * * * python /path/to/main.py`
- **Task Scheduler** (Windows): Create a daily task
- **Cloud functions**: Deploy on AWS Lambda or Google Cloud Functions
- Run every few hours or daily to monitor price changes

## 🎁 Example Products to Track

The script includes two URLs:
- **Static test site**: `https://appbrewery.github.io/instant_pot/` (for testing)
- **Live Amazon**: Instant Pot product (example)

Replace with any Amazon product URL you want to track!
