# Day 53 - Data Entry Automation Bot

## Overview
An intelligent web scraping and automation bot that extracts rental property listings from a Zillow clone website and automatically fills the data into a Google Form. This project demonstrates combining web scraping with browser automation for automated data entry tasks.

## Project Description

### Data Entry Automation (main.py)
A sophisticated automation system that:
- Scrapes rental property data from a Zillow clone website
- Extracts property addresses, prices, and listing links
- Automatically fills a Google Form with the scraped data
- Processes all listings without manual intervention
- Provides progress tracking and completion statistics

**Key Features:**
- **Web Scraping**: Extracts property data using BeautifulSoup
- **Data Processing**: Cleans and formats addresses and prices
- **Form Automation**: Uses Selenium to fill Google Forms automatically
- **Batch Processing**: Handles multiple listings in one run
- **Progress Tracking**: Reports completion status for each entry
- **Environment Variables**: Secure credential management with .env file

## Technologies Used
- **BeautifulSoup4**: HTML parsing and web scraping
- **Selenium WebDriver**: Browser automation for form filling
- **Requests**: HTTP library for fetching web pages
- **Python-dotenv**: Environment variable management
- **Python 3**: Programming language

## How It Works

### 1. Web Scraping Phase
```python
# Fetches the Zillow clone website
response = requests.get(web_link)
soup = BeautifulSoup(response.text, 'html.parser')
```

### 2. Data Extraction
The bot extracts three key pieces of information:

**Property Links:**
```python
links = [i.get('href') for i in soup.select(".StyledPropertyCardDataWrapper a")]
```

**Addresses:**
```python
address = [i.get_text() for i in soup.select('.StyledPropertyCardDataWrapper a address')]
address_list = [i.replace(" | ", " ").strip() for i in address]
```

**Prices:**
```python
price = [i.get_text().replace("/mo", "").split("+")[0] 
         for i in soup.select('.StyledPropertyCardDataWrapper span')]
```

### 3. Automated Form Filling
Using Selenium, the bot:
1. Opens the Google Form
2. Locates input fields using XPath
3. Fills in address, price, and link for each property
4. Clicks the submit button
5. Repeats for all listings

## Configuration

### Environment Variables (.env file)
```env
form_link=your_google_form_link
```

### Target Website
```python
web_link = "https://appbrewery.github.io/Zillow-Clone/"
```

### Chrome Profile Path (Optional)
```python
profile_path = "C:/Users/ayush/AppData/Local/Google/Chrome/User Data/profile 4/"
```
**Note**: Update this path to match your system if using custom Chrome profiles.

## Prerequisites
```bash
pip install selenium beautifulsoup4 requests python-dotenv
```

## Setup

1. **Install required packages:**
   ```bash
   pip install selenium beautifulsoup4 requests python-dotenv
   ```

2. **Create a `.env` file with your Google Form link:**
   ```env
   form_link=https://docs.google.com/forms/d/e/your-form-id/viewform
   ```

3. **Create a Google Form with three questions:**
   - Question 1: Address (Short answer)
   - Question 2: Price (Short answer)
   - Question 3: Link (Short answer)

4. **Update the Chrome profile path** (if needed) to match your system

5. **Ensure Chrome browser is installed**

## Usage

### Run the Bot
```bash
python main.py
```

### Expected Output
```
there are 45 in total
address lists is created
['$3,000', '$2,500', '$2,800', ...]
price list is created.
filling the form
https://docs.google.com/forms/...
filled the form 1 times
filled the form 2 times
...
filled the form with all the data and with Total Entries:: 45/45
```

## Code Breakdown

### Data Extraction Process

**Step 1: Fetch the webpage**
```python
response = requests.get(web_link)
soup = BeautifulSoup(response.text, 'html.parser')
```

**Step 2: Extract property links**
- Uses CSS selector to find all property card links
- Extracts the `href` attribute

**Step 3: Extract and clean addresses**
- Finds all address elements
- Removes pipe separators and extra whitespace
- Creates a clean list of addresses

**Step 4: Extract and format prices**
- Removes "/mo" suffix from prices
- Splits on "+" to remove additional fees
- Extracts base rental price only

### Form Filling Process

**Step 1: Initialize Chrome WebDriver**
```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
```

**Step 2: Loop through all properties**
```python
for i in range(len(links)):
    driver.get(form_link)
    time.sleep(1.5)  # Wait for form to load
```

**Step 3: Fill form fields**
- Locates each input field using XPath
- Sends data using `send_keys()`
- Clicks submit button

**Step 4: Track progress**
- Prints status after each submission
- Shows completion percentage

## Chrome Options
```python
chrome_options.add_experimental_option("detach", True)  # Keeps browser open
```
This option prevents the browser from closing immediately after the script completes, allowing you to see the final state.

## XPath Locators
The script uses specific XPath expressions to locate form elements:
- Address field: `//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input`
- Price field: `//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input`
- Link field: `//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input`
- Submit button: `//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span`

**Note**: These XPaths are specific to Google Forms structure. If your form has a different structure, you'll need to update them.

## Important Notes

### Google Form Setup
- The form must have exactly three questions in order: Address, Price, Link
- All questions should be "Short answer" type
- The form should allow multiple submissions

### XPath Customization
If you're using a different Google Form:
1. Open Chrome DevTools (F12)
2. Inspect each form field
3. Right-click → Copy → Copy XPath
4. Replace the XPath values in the code

### Timing Considerations
- The script includes a 1.5-second delay between form submissions
- This prevents overwhelming Google's servers
- Adjust `time.sleep(1.5)` if needed for slower connections

### Browser Behavior
- The browser window stays open after completion (detach option)
- You can observe the automation process in real-time
- Forms are submitted one by one sequentially

## Security Notes
- Store sensitive data in `.env` file
- Add `.env` to `.gitignore` to avoid committing credentials
- Form links should be kept private if they contain sensitive data
- Chrome profile paths may contain personal information

## Commented Code
The script includes commented code for opening spreadsheets:
```python
# def open_spreadsheet():
#     # Code to open Google Sheets with results
```
This functionality can be enabled if you want to view the spreadsheet after data entry.

## Troubleshooting

### Common Issues

**Issue: "No such element" error**
- Solution: Update XPath locators for your specific form

**Issue: Data not appearing in form**
- Solution: Increase `time.sleep()` duration to allow more loading time

**Issue: Chrome driver not found**
- Solution: Selenium automatically manages ChromeDriver, ensure Chrome is installed

**Issue: Empty data lists**
- Solution: Website structure may have changed, verify CSS selectors

## Customization Ideas
- Add error handling for failed submissions
- Implement retry logic for network issues
- Add data validation before submission
- Create a log file for tracking submissions
- Add support for different property websites
- Implement headless browser mode for faster execution
- Add email notifications upon completion

## Use Cases
- Automating repetitive data entry tasks
- Creating property databases from listings
- Market research and price analysis
- Real estate data aggregation
- Learning web scraping and automation

## Future Enhancements
- Add support for multiple property websites
- Implement database storage for scraped data
- Create a GUI for easier configuration
- Add data visualization and analysis
- Implement scheduling for periodic scraping
- Add email reports with summary statistics
- Create export functionality (CSV, Excel)

## Learning Outcomes
By completing this project, you'll learn:
- Web scraping with BeautifulSoup
- Browser automation with Selenium
- Data cleaning and processing
- Working with environment variables
- XPath for element location
- Combining multiple libraries for complex tasks
- Handling timing and synchronization in automation

