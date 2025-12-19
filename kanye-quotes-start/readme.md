# Kanye West Quote Generator

A fun GUI application that displays random Kanye West quotes using the Kanye.rest API.

## Features
- Random Kanye West quote generation
- Stylish GUI with custom background and Kanye image
- One-click quote fetching
- Real-time API integration
- Custom styling with images and fonts

## How It Works
1. Application displays a window with Kanye's image
2. Click on Kanye's image to get a new random quote
3. Quote appears on the background image
4. Each click fetches a fresh quote from the API

## Visual Elements
- `background.png` - Custom background image for quotes
- `kanye.png` - Clickable Kanye West image button
- Custom fonts and styling for quote display
- Responsive text wrapping for long quotes

## API Integration
- Uses the free Kanye.rest API
- No authentication required
- Real-time quote fetching
- JSON response parsing

## Example Quotes
The app fetches actual Kanye West quotes like:
- "I'm a creative genius"
- "My greatest pain in life is that I will never be able to see myself perform live"
- And many more inspiring/entertaining quotes!

## Technical Features
- Tkinter GUI framework
- HTTP requests handling
- Image integration and display
- Event-driven programming
- Error handling for API calls

## How to Use
1. Run `main.py`
2. Window opens with Kanye's image
3. Click on Kanye to get a random quote
4. Click again for more quotes!

## Learning Concepts
- API consumption and integration
- GUI development with Tkinter
- Image handling in GUI applications
- Event handling and callbacks
- JSON data parsing
- HTTP request/response handling

## Requirements
- Python 3.x
- tkinter (included with Python)
- requests library
- Internet connection for API access

## Installation
```bash
pip install requests
python main.py
```

## API Details
- **Endpoint**: https://api.kanye.rest
- **Method**: GET
- **Response**: JSON with "quote" field
- **Rate Limits**: None specified