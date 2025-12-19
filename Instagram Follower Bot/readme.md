# Day 52 - Instagram Follower Bot

## Overview
An automated Instagram bot that logs into your account and automatically follows users from a target account's followers list. This project demonstrates advanced web automation with Instagram's dynamic interface.

## Project Description

### Instagram Follower Bot (main.py)
A sophisticated automation system that:
- Logs into Instagram using credentials
- Navigates to a target account's followers
- Scrolls through the followers list
- Automatically follows users who aren't already followed
- Tracks follow statistics and reports results

**Key Features:**
- **Automated Login**: Secure login with environment variables
- **Follower Discovery**: Navigates to target account's followers
- **Smart Scrolling**: Scrolls through followers modal to load more users
- **Selective Following**: Only follows users not already followed
- **Status Tracking**: Distinguishes between "Follow", "Following", and "Requested" states
- **Chrome Profile Management**: Uses custom profile for persistent sessions
- **Detailed Reporting**: Provides comprehensive statistics

## Technologies Used
- **Selenium WebDriver**: Browser automation
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser with custom profile
- **python-dotenv**: Environment variable management

## Class Structure

### InstaFollower Class

#### Methods:
1. **`__init__()`**: Initializes Chrome driver with custom profile
2. **`login()`**: Logs into Instagram with credentials
3. **`find_followers()`**: Navigates to target account and opens followers modal
4. **`follow()`**: Follows users from the followers list

## Configuration

### Environment Variables (.env file)
```env
user_name=your_instagram_username
password=your_instagram_password
```

### Target Account
```python
Search = "codinganddecoding"  # Target account to follow users from
```

### Chrome Profile Path
```python
profile_path = "Your chrome profile path"
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
2. Create a `.env` file with your Instagram credentials:
   ```
   user_name=your_instagram_username
   password=your_instagram_password
   ```
3. Update the Chrome profile path to match your system
4. Update the `Search` variable with the target account username
5. Ensure Chrome browser is installed

## Usage

### Run the Bot
```bash
python main.py
```

### How It Works
1. Logs into Instagram (if using login method)
2. Navigates to target account profile
3. Clicks on followers button
4. Scrolls through followers modal (2 iterations)
5. Finds all "Follow" buttons
6. Clicks each button with a 0.5-second delay
7. Reports statistics

## Key Features Breakdown

### 1. Login Process
- Navigates to Instagram login page
- Fills username and password
- Clicks login button
- Handles "Not now" popup for save login info

### 2. Follower Navigation
- Goes directly to target profile URL
- Clicks followers link
- Waits for followers modal to load
- Captures modal element for scrolling

### 3. Smart Scrolling
```python
for i in range(2):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    time.sleep(2)
```
- Scrolls through modal to load more followers
- Configurable scroll iterations
- Waits between scrolls for content loading

### 4. Follow Automation
- Locates all buttons containing "Follow" text
- Distinguishes button states:
  - **"Follow"**: Not following, will click
  - **"Following"**: Already following, skip
  - **"Requested"**: Follow request pending, skip
- 0.5-second delay between follows to avoid rate limiting
- Exception handling for click interceptions

## Output Example
```
Found 50 follow buttons
Followed: 30, Already following: 15, Requested: 5
Total:(50/50)
```

## Chrome Options
```python
chrome_option.add_experimental_option('detach', True)  # Keep browser open
chrome_option.add_argument(f'--user-data-dir={profile_path}')  # Custom profile
```

## Error Handling
- **ElementClickInterceptedException**: Handles when elements are blocked by overlays
- **StaleElementReferenceException**: Handles when elements are no longer attached to DOM
- **NoSuchElementException**: Handles missing elements gracefully

## Important Notes

### Instagram Rate Limits
- Instagram has rate limits for following users
- Following too many users too quickly can result in temporary blocks
- Recommended: Add longer delays between follows for safety
- Consider reducing the number of follows per session

### Ethical Considerations
- Use responsibly and respect Instagram's Terms of Service
- Don't spam follow/unfollow
- Consider the accounts you're targeting
- Be aware of potential account restrictions

### Login Method
```python
# Currently login is commented out in main execution
# object.login()  # Uncomment if not using Chrome profile with saved login
```

## Security Notes
- Credentials stored in `.env` file (not committed to git)
- Chrome profile path is system-specific
- Using Chrome profile with saved login is more reliable
- Ensure `.env` file is in `.gitignore`

## Customization
- Adjust scroll iterations for more/fewer followers
- Modify delay between follows (currently 0.5 seconds)
- Change target account in `Search` variable
- Add filters for specific follower types
- Implement unfollow functionality

## Alternative Scrolling Method
The code includes an alternative scrolling method (commented out):
```python
# modal.send_keys(Keys.END)
# time.sleep(2)
```

## Future Enhancements
- Add unfollow functionality
- Implement follower filters (verified accounts, follower count, etc.)
- Add delay randomization for more natural behavior
- Create scheduling for automated daily follows
- Add analytics and reporting
- Implement database to track followed users
