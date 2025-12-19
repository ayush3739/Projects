# Day 46 - Spotify Playlist Creator from Billboard Hot 100

This folder contains a project that combines web scraping with the Spotify API to create playlists based on Billboard Hot 100 charts from any date.

## 📁 Files Overview

- **`main.py`** - Main application that scrapes Billboard and creates Spotify playlist
- **`token.txt`** - Spotify OAuth token cache (auto-generated)
- **`results.json`** - Spotify user data (auto-generated for debugging)

## 🎯 Project Overview

This project allows you to:
1. Input any date in `YYYY-MM-DD` format
2. Scrape the Billboard Hot 100 chart for that date
3. Search for those songs on Spotify
4. Create a private Spotify playlist with the found songs

## 🎯 Topics Covered

### 1. Web Scraping with Beautiful Soup
- Scraping Billboard Hot 100 chart data
- Using custom headers to avoid blocking
- Extracting song titles with CSS selectors
- Text processing with `strip()` method

### 2. Spotify API Integration
- **Spotipy**: Python library for Spotify Web API
- OAuth authentication with `SpotifyOAuth`
- User authentication and authorization
- Managing API credentials

### 3. Spotify Operations
- **User Profile**: Getting current user information
- **Search**: Finding tracks by name and year
- **Playlist Creation**: Creating private playlists
- **Playlist Management**: Adding tracks to playlists
- Error handling for missing songs

### 4. Data Handling
- JSON formatting and file writing
- Dictionary querying for nested data
- List comprehension for data extraction
- Exception handling (`IndexError`, `KeyError`)

## 🔧 Setup Requirements

### Prerequisites
```bash
pip install beautifulsoup4 requests spotipy
```

### Spotify API Credentials
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
2. Create a new app
3. Get your `CLIENT_ID` and `CLIENT_SECRET`
4. Set redirect URI to `https://example.org/callback` (or your preferred URI)
5. Replace placeholders in `main.py`:
   ```python
   CLIENT_ID = "Your_client_ID"
   CLIENT_SECRET = "Your_client_secret"
   REDIRECT_URI = "https://example.org/callback"
   ```

## 🎯 Features

### Billboard Scraping
- Fetches Billboard Hot 100 chart for any date
- URL format: `https://www.billboard.com/charts/hot-100/{date}`
- Uses BeautifulSoup to parse HTML
- Extracts song titles from `li ul li h3` elements
- Custom user-agent header to avoid blocking

### Spotify Integration
- OAuth 2.0 authentication flow
- Searches for tracks with year filter for better accuracy
- Handles missing songs gracefully
- Creates private playlists automatically
- Adds found tracks to the playlist
- Reports success rate (e.g., "85/100 songs found")

### Error Handling
- Try-except blocks for missing songs on Spotify
- Skips songs that don't exist or can't be found
- Provides feedback about skipped songs

## 📚 Documentation Links

### Spotify API
- [Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [Spotify OAuth Guide](https://developer.spotify.com/documentation/general/guides/authorization/)

### Web Scraping
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)

### Billboard Charts
- [Billboard Hot 100](https://www.billboard.com/charts/hot-100/)

## 🚀 Getting Started

### Step 1: Install Dependencies
```bash
pip install beautifulsoup4 requests spotipy
```

### Step 2: Set Up Spotify Credentials
1. Create a Spotify Developer account
2. Create a new application
3. Copy your Client ID and Client Secret
4. Update the credentials in `main.py`

### Step 3: Run the Application
```bash
cd "Day 46"
python main.py
```

### Step 4: Follow the Prompts
1. Enter a date (e.g., `2000-08-12`)
2. Authorize the application in your browser
3. Wait for the playlist to be created
4. Check your Spotify account for the new playlist!

## 📝 Key Learning Points

- Integrating multiple APIs in a single project
- OAuth 2.0 authentication flow
- Web scraping with custom headers
- API rate limiting and error handling
- Creating automated workflows
- JSON data manipulation
- File-based token caching
- Combining web scraping with API calls
- Building practical automation tools
- Handling edge cases (missing data, API errors)

## 🎵 Example Usage

```
Which year you want to travel to? Type the date in this format YYYY-MM-DD: 2000-08-12
```

The script will:
1. Scrape the Billboard Hot 100 for August 12, 2000
2. Search for each song on Spotify
3. Create a playlist named "2000-08-12 Billboard 100"
4. Add all found songs to the playlist
5. Report: "The playlist has been created. A total of 85/100 of the top 100 songs were found!"

## ⚠️ Important Notes

- Keep your Spotify credentials secure (don't commit to version control)
- The `token.txt` file contains your access token - add to `.gitignore`
- Some older songs may not be available on Spotify
- Billboard website structure may change; selectors might need updates
- Respect Billboard's terms of service when scraping
