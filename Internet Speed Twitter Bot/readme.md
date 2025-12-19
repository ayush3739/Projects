# Day 51 - Internet Speed Twitter Complaint Bot

## Overview
An automated bot that monitors your internet speed and tweets complaints to your internet service provider when the speed falls below the promised threshold. This project combines speed testing with social media automation.

## Project Description

### Internet Speed Twitter Bot (main.py)
A comprehensive automation system that:
- Tests internet download and upload speeds
- Compares results against promised speeds
- Automatically tweets complaints to the ISP via Twitter/X
- Optionally deletes the complaint tweet
- Uses persistent Chrome profile for Twitter session

**Key Features:**
- **Speed Testing**: Automated speed test using Speedtest.net
- **Speed Comparison**: Checks if speeds meet promised levels
- **Automatic Tweeting**: Posts complaint when speeds are below threshold
- **Tweet Deletion**: Can automatically delete the complaint tweet
- **Chrome Profile Management**: Uses custom profile for persistent Twitter login
- **Environment Variables**: Secure credential management with .env file

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser with custom profile
- **python-dotenv**: Environment variable management
- **WebDriverWait**: Explicit waits for reliable automation

## Class Structure

### InternetSpeedTwitterBot Class

#### Methods:
1. **`__init__()`**: Initializes Chrome driver with custom profile
2. **`get_internet_speed()`**: Tests internet speed on Speedtest.net
3. **`tweet_at_provider()`**: Posts complaint tweet on Twitter/X
4. **`delete_the_post()`**: Removes the complaint tweet (optional)

## Configuration

### Environment Variables (.env file)
```env
user_id=your_twitter_email
user_pass=your_twitter_password
```

### Speed Thresholds
```python
PROMISED_DOWN = 50  # Mbps
PROMISED_UP = 10    # Mbps
```

### Chrome Profile Path
```python
profile_path = r"C:\Users\ayush\AppData\Local\Google\Chrome\User Data\Profile 4\Default"
```

## Prerequisites
```bash
pip install selenium python-dotenv
```

## Setup
1. Install required packages:
   ```bash
   pip install selenium python-dotenv
   ```
2. Create a `.env` file with your Twitter credentials:
   ```
   user_id=your_twitter_email
   user_pass=your_twitter_password
   ```
3. Update the Chrome profile path to match your system
4. Update `PROMISED_DOWN` and `PROMISED_UP` with your ISP's promised speeds
5. Ensure Chrome browser is installed

## Usage

### Run the Bot
```bash
python main.py
```

### How It Works
1. Opens Speedtest.net
2. Runs speed test (takes ~45 seconds)
3. Captures download and upload speeds
4. Compares with promised speeds
5. If speeds are below threshold:
   - Opens Twitter/X
   - Composes complaint tweet
   - Posts the tweet
   - Optionally deletes the tweet

## Tweet Format
```
Hey Internet Provider, why is my internet speed {actual_down}down/{actual_up}up 
when I pay for {promised_down}down/{promised_up}up?
```

## Key Features Breakdown

### 1. Speed Testing
- Navigates to Speedtest.net
- Clicks the "GO" button
- Waits 45 seconds for test completion
- Extracts download and upload speeds using XPath

### 2. Twitter Automation
- Opens Twitter/X home page
- Locates tweet composition area
- Fills in complaint message
- Clicks post button
- Provides status updates

### 3. Tweet Deletion (Optional)
- Waits 7 seconds after posting
- Clicks options menu on the tweet
- Selects delete option
- Confirms deletion in popup

## Chrome Options
```python
chrome_options.add_experimental_option("detach", True)  # Keep browser open
chrome_options.add_argument("--start-maximized")  # Start maximized
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Anti-detection
```

## Error Handling
- **TimeoutException**: Handles element loading timeouts
- **ElementClickInterceptedException**: Manages click interception issues
- **StaleElementReferenceException**: Handles stale element references
- **NoSuchElementException**: Gracefully handles missing elements

## Example Output
```
down: 35.4
Up: 8.2
opening the Tweeter Website
----tweeted the post----
deleting the post
```

## Security Notes
- Credentials stored in `.env` file (not committed to git)
- Chrome profile path is system-specific
- Uses persistent Chrome profile to avoid repeated logins

## Notes
- Speed test takes approximately 45 seconds to complete
- Chrome profile must have Twitter already logged in for seamless automation
- XPath selectors may need updates if Twitter/X UI changes
- Tweet deletion is optional (commented out by default)
- Ensure `.env` file is in `.gitignore` to protect credentials

## Customization
- Adjust `PROMISED_DOWN` and `PROMISED_UP` to your plan
- Modify wait times based on your internet connection
- Customize tweet message format
- Change speed test website if needed
