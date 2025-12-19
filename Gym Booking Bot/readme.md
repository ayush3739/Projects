# Gym Booking Bot - Automated Class Booking System

## Overview
An advanced Selenium-based automation bot that automatically books gym classes based on specific criteria. Features network resilience, retry logic, and comprehensive verification mechanisms.

## Files Included

### 1. gym_booking_bot.py (Advanced Version)
Full-featured bot with network resilience and verification.

**Features:**
- Automated login with retry mechanism
- Smart class selection (Tuesday/Thursday 6:00 PM)
- Multiple booking states handling
- Network resilience with up to 7 retry attempts
- Booking verification on My Bookings page
- Comprehensive status reporting
- Chrome profile management

### 2. gym_booking_simple.py (Basic Version)
Simplified version for learning and testing.

**Features:**
- Basic login automation
- Class booking demonstration
- Simpler code structure
- Good for understanding fundamentals

## Key Features

### Automated Login
- Uses credentials from configuration
- Explicit waits for reliable page loading
- Handles login form submission
- Verifies successful login

### Smart Class Selection
Filters classes by:
- **Day**: Tuesday and Thursday only
- **Time**: 6:00 PM classes only
- **Status**: Checks if already booked or on waitlist

### Booking Actions
- **Book Class**: For available classes
- **Join Waitlist**: When class is full
- **Skip**: If already booked or waitlisted

### Network Resilience
```python
def retry(func, retries=7, description=None):
    # Automatically retries failed operations
```
- Up to 7 retry attempts
- Handles TimeoutException
- 1-second delay between retries

### Verification System
- Navigates to My Bookings page
- Counts and verifies all bookings
- Compares expected vs actual bookings
- Reports success or mismatches

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser with custom profile
- **WebDriverWait**: Explicit waits for element loading

## Configuration

### Required Credentials (in script)
```python
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"
```

### Chrome Profile
```python
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
```

## Prerequisites
```bash
pip install selenium
```

## Setup
1. Install Selenium:
   ```bash
   pip install selenium
   ```
2. Update credentials in the script:
   - Set `ACCOUNT_EMAIL` to your email
   - Set `ACCOUNT_PASSWORD` to your password
3. Create an account on the gym website first
4. Ensure Chrome browser is installed

## Usage

### Advanced Bot
```bash
python gym_booking_bot.py
```

### Simple Bot
```bash
python gym_booking_simple.py
```

## How It Works

### Step 1: Login
1. Clicks login button
2. Enters email and password
3. Submits login form
4. Waits for schedule page

### Step 2: Find Classes
1. Locates all class cards
2. Filters by day (Tue/Thu)
3. Filters by time (6:00 PM)
4. Identifies booking button states

### Step 3: Book Classes
1. Clicks "Book Class" for available classes
2. Clicks "Join Waitlist" for full classes
3. Skips already booked/waitlisted classes
4. Waits for button text to change

### Step 4: Verify
1. Navigates to My Bookings
2. Counts booked classes
3. Verifies against expected count
4. Reports results

## Output Example
```
Trying login. Attempt: 1
Trying Booking. Attempt: 1
✓ Successfully booked: Yoga on Tuesday
Trying Waitlisting. Attempt: 1
✓ Joined waitlist for: Spinning on Tuesday
✓ Already booked: Pilates on Thursday

--- Total Tuesday/Thursday 6pm classes: 3 ---

--- VERIFYING ON MY BOOKINGS PAGE ---
Trying Get my bookings. Attempt: 1
  ✓ Verified: Yoga
  ✓ Verified: Spinning
  ✓ Verified: Pilates

--- VERIFICATION RESULT ---
Expected: 3 bookings
Found: 3 bookings
✅ SUCCESS: All bookings verified!
```

## Error Handling
- **TimeoutException**: Automatic retry mechanism
- **NoSuchElementException**: Graceful handling and skipping
- **ElementClickInterceptedException**: Handled in follow logic
- **StaleElementReferenceException**: Managed during verification

## Chrome Options
```python
chrome_options.add_experimental_option("detach", True)  # Keep browser open
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")  # Custom profile
```

## Important Notes

### Browser Management
- Browser stays open with `detach=True`
- Must manually quit Chrome before re-running
- Chrome profile persists login sessions

### Wait Times
- Login wait: 2 seconds
- Class booking wait: 2 seconds
- Small delays (0.5s) between bookings

### Retry Logic
- Default: 7 retry attempts
- 1-second delay between retries
- Ensures bookings complete despite network issues

## Customization

### Change Target Days/Times
```python
if "Tue" in day_title or "Thu" in day_title:
    if "6:00 PM" in time_text:
        # Booking logic
```

### Adjust Retry Attempts
```python
def retry(func, retries=7, description=None):
    # Change retries parameter
```

### Modify Wait Times
```python
wait = WebDriverWait(driver, 2)  # Adjust timeout
```

## Troubleshooting

### SessionNotCreatedException
- Quit existing Chrome instance
- Close all Chrome windows
- Re-run the script

### Elements Not Found
- Check if gym website UI changed
- Update XPath/CSS selectors
- Increase wait times

### Login Fails
- Verify credentials are correct
- Check if account exists
- Ensure website is accessible

## Learning Outcomes
- Advanced Selenium automation
- Network resilience patterns
- Retry mechanisms
- Explicit waits and synchronization
- Chrome profile management
- Verification and validation
- Exception handling strategies
- Web scraping best practices
