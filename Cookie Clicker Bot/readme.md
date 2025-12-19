# Cookie Clicker Bot - Selenium Web Automation

## Overview
A collection of Selenium automation scripts demonstrating web browser automation, element interaction, and automated gameplay. This project includes three distinct automation exercises.

## Projects Included

### 1. Cookie Clicker Bot (cookie_clicker_bot.py)
An automated bot that plays the Cookie Clicker game.

**Features:**
- Automatically clicks the cookie
- Purchases the best available upgrade every 5 seconds
- Runs for 5 minutes and reports final score
- Intelligent buying strategy based on available upgrades
- Error handling for missing elements

**How it works:**
- Selects English language
- Clicks cookie continuously
- Every 5 seconds, purchases the most expensive affordable item
- Stops after 5 minutes and displays final cookie count

### 2. Form Filler (form_filler.py)
Automated form submission demonstration.

**Features:**
- Navigates to form page
- Fills first name, last name, and email fields
- Automatically submits the form
- Uses NAME attribute for element location

### 3. Wikipedia Interaction (wikipedia_interaction.py)
Interactive Wikipedia navigation and search.

**Features:**
- Navigates to Wikipedia homepage
- Retrieves article count
- Demonstrates link clicking
- Performs automated search with keyboard input
- Multiple element location strategies (XPath, Link Text, Name)

## Technologies Used
- **Selenium WebDriver**: Browser automation framework
- **Python 3**: Programming language
- **Chrome WebDriver**: Chrome browser automation

## Prerequisites
```bash
pip install selenium
```

## Setup
1. Install Selenium:
   ```bash
   pip install selenium
   ```
2. Ensure Chrome browser is installed
3. ChromeDriver will be automatically managed by Selenium

## Usage

### Cookie Clicker Bot
```bash
python cookie_clicker_bot.py
```
Runs for 5 minutes, then displays final cookie count.

### Form Filler
```bash
python form_filler.py
```
Automatically fills and submits the form at the specified URL.

### Wikipedia Interaction
```bash
python wikipedia_interaction.py
```
Demonstrates Wikipedia navigation and search functionality.

## Key Concepts Demonstrated
1. **Element Location**: XPath, CSS Selector, Name, Link Text
2. **Element Interaction**: Clicking, sending keys
3. **Time Management**: Time-based automation and delays
4. **Exception Handling**: NoSuchElementException, ValueError
5. **Chrome Options**: Browser configuration and persistence
6. **Automation Logic**: Conditional actions and smart decision-making

## Technical Details

### Chrome Options
```python
chrome_options.add_experimental_option("detach", True)
```
Keeps the browser open after script completion for inspection.

### Element Selection Strategies
- **XPath**: Direct path to elements
- **CSS Selector**: CSS-based selection
- **Name**: Form field names
- **Link Text**: Clickable link text

## Notes
- Cookie Clicker bot takes 5 minutes to complete
- Form filler uses a demo form URL
- Wikipedia interaction demonstrates keyboard input (Keys.ENTER)
- All scripts use Chrome browser by default
- Browser windows remain open after completion for review

## Learning Outcomes
- Browser automation basics
- Element location and interaction
- Time-based automation
- Exception handling in web scraping
- Chrome WebDriver configuration
