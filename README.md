# Projects Portfolio

A collection of Python projects demonstrating web development, automation, API integration, and data processing skills.

## 📊 Repository Overview

This repository contains **35+ projects** covering:
- 🌐 **Web Development** (Flask applications)
- 🤖 **Automation & Bots** (Selenium, web scraping)
- 📧 **API Integration** (REST APIs, external services)
- 🎮 **Games** (Turtle graphics, GUI applications)
- 📊 **Data Processing** (CSV, spreadsheets)

**Primary Language:** Python (with Jupyter Notebook for some projects)

---

## 🌟 Featured Projects

### 1. **Flight Deals Finder** 🛫
An automated flight price monitoring system with multi-destination tracking and instant notifications.

**Features:**
- Google Sheets integration via Sheety API
- Flight price monitoring using Amadeus API
- IATA code management
- WhatsApp & Email notifications (Twilio + Gmail SMTP)
- Direct & indirect flight search
- Price comparison and alerts

**Tech Stack:** Python, Amadeus API, Sheety API, Twilio, SMTP, python-dotenv

**Use Case:** Get notified when flight prices drop below your target threshold

---

### 2. **Blog Website** ✍️
A full-featured Flask blog with user authentication, admin controls, and comment system.

**Features:**
- User authentication (register/login/logout)
- Admin-only post management
- Rich text editor (CKEditor)
- Comments system with timestamps
- Gravatar avatars
- SMTP email contact form
- Responsive Bootstrap UI

**Tech Stack:** Flask, SQLAlchemy, Flask-Login, Flask-Bootstrap, Flask-CKEditor, Flask-Gravatar, SQLite

**Database Models:** Users, BlogPosts, Comments with relationships

---

### 3. **Coffee and Wifi Cafe Tracker** ☕
A Flask web app for tracking and rating cafes based on amenities.

**Features:**
- Cafe database with CSV storage
- Add new cafes with ratings
- Emoji-based rating system (coffee ☕, wifi 💪, power 🔌)
- Location tracking via Google Maps URLs
- Operating hours tracking
- WTForms validation
- Bootstrap responsive UI

**Tech Stack:** Flask, Flask-WTF, Flask-Bootstrap, WTForms, CSV

**Rating Categories:** Coffee quality, wifi strength, power socket availability

---

### 4. **Exercise Tracker** 💪
Natural language exercise logging system with automatic calorie calculation.

**Features:**
- Natural language processing for exercise input
- Automatic calorie estimation (Nutritionix API)
- Google Sheets logging (Sheety API)
- Date and time stamps
- User profile customization

**Tech Stack:** Python, Nutritionix API, Sheety API, python-dotenv

**Use Case:** Track workouts by describing them in plain English

---

## 📁 Complete Project List

### 🌐 Web Development & APIs

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Blog Website** | Full-featured blog with auth & comments | Flask, SQLAlchemy, Bootstrap |
| **Coffee and Wifi Cafe Tracker** | Rate and track cafes | Flask, WTForms, CSV |
| **MY TOP 10 MOVIES (website)** | Movie rating website | Flask, SQLAlchemy |
| **Flask WTForms Login** | Login system implementation | Flask, WTForms |
| **TinDog Project** | Landing page project | HTML, CSS, Bootstrap |

### 🤖 Automation & Bots

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Flight Deals** | Automated flight price monitoring | Amadeus API, Twilio, Sheety |
| **Instagram Follower Bot** | Instagram automation | Selenium |
| **Cookie Clicker Bot** | Game automation bot | Selenium |
| **Gym Booking Bot** | Automated gym slot booking | Selenium |
| **Internet Speed Twitter Bot** | Tweet ISP when speed is slow | Selenium, Twitter API |
| **Automating Data Entry with Web Scraping** | Scrape and fill forms | BeautifulSoup, Selenium |

### 📧 Messaging & Notifications

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Birthday wish and quote sender** | Automated birthday wishes | SMTP, email |
| **Mail Merge Project** | Personalized bulk emails | Python, file I/O |
| **Rain alert** | Weather-based notifications | Weather API, SMS |
| **Stock news messenger** | Stock price alerts with news | Alpha Vantage API, News API |

### 🎯 Data & Tracking

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Exercise Tracker** | NLP-based workout logging | Nutritionix API, Sheety |
| **Habit Tracker** | Habit tracking with Pixela | Pixela API, requests |
| **Amazon Price Tracker** | Monitor product prices | BeautifulSoup, SMTP |

### 🎮 Games

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Snake game** | Classic snake game | Turtle graphics |
| **Pong game** | Two-player pong | Turtle graphics |
| **Crossing turtle** | Road crossing game | Turtle graphics, OOP |
| **turtle race** | Betting race game | Turtle graphics |
| **Quiz game** | Trivia quiz with API | Open Trivia API, OOP |
| **higher or lower guess game** | Number guessing game | Python |
| **coffee game** | Text-based adventure | Python |

### 🛠️ Utilities & Tools

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **Password Manager** | Secure password storage | Tkinter, JSON |
| **Pomodoro timer** | Productivity timer | Tkinter |
| **miles to km** | Unit converter GUI | Tkinter |
| **NATO Alphabet game** | Phonetic alphabet converter | Pandas, list comprehension |

### 🎨 Creative & Art

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **hirst painting using turtle** | Dot art generator | Turtle graphics, colorgram |

### 🎬 Web Scraping

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **100 movies to watch** | Scrape top 100 movies list | BeautifulSoup, requests |
| **Spotify Billboard Playlist** | Create playlist from Billboard Hot 100 | BeautifulSoup, Spotipy API |

### 🎨 Miscellaneous

| Project | Description | Key Technologies |
|---------|-------------|------------------|
| **kanye-quotes-start** | Random Kanye quotes API | Tkinter, requests |

---

## 🔧 Technologies Used Across Projects

### Languages
- Python 3.x
- HTML/CSS
- SQL

### Frameworks & Libraries
- **Web:** Flask, Bootstrap, Jinja2
- **GUI:** Tkinter, Turtle Graphics
- **Data:** Pandas, SQLAlchemy, CSV
- **Web Scraping:** BeautifulSoup, Selenium
- **Forms:** WTForms, Flask-WTF
- **Auth:** Flask-Login, Werkzeug

### APIs & Services
- **Flight:** Amadeus API
- **Exercise:** Nutritionix API
- **Music:** Spotify API
- **Weather:** OpenWeatherMap
- **Stocks:** Alpha Vantage
- **News:** News API
- **Data:** Sheety API (Google Sheets)
- **Communication:** Twilio (WhatsApp/SMS), SMTP

### Tools & Concepts
- REST API integration
- OAuth authentication
- Web scraping & automation
- Database design (SQLite)
- SMTP email sending
- Environment variables (.env)
- Object-Oriented Programming
- Data persistence (JSON, CSV, DB)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager
- Virtual environment (recommended)

### Common Setup Pattern
```bash
# Clone the repository
git clone https://github.com/ayush3739/Projects.git
cd Projects

# Navigate to specific project
cd "Project Name"

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Configure environment variables (if needed)
# Create .env file with required API keys

# Run the project
python main.py
```

### API Keys Required
Many projects require API keys. Create a `.env` file in the project directory with:
- **Amadeus:** Flight search
- **Nutritionix:** Exercise tracking
- **Twilio:** WhatsApp/SMS
- **Sheety:** Google Sheets access
- **Spotify:** Music playlist creation
- Weather, News, Stock APIs as needed

---

## 📚 Learning Outcomes

These projects demonstrate proficiency in:
- ✅ Flask web application development
- ✅ RESTful API integration and consumption
- ✅ Database design and ORM usage
- ✅ User authentication and authorization
- ✅ Form validation and processing
- ✅ Web scraping and automation
- ✅ Email and messaging integration
- ✅ Environment variable management
- ✅ Object-oriented programming
- ✅ Error handling and debugging
- ✅ Frontend integration (Bootstrap)
- ✅ Data processing and persistence

---

## 📝 Notes

- **Results may be incomplete:** The repository contains 30+ projects; some may not be listed in detail
- **View all projects:** [Browse repository](https://github.com/ayush3739/Projects)
- **Individual READMEs:** Many projects have detailed documentation in their folders

---

## 🤝 Contributing

These are personal learning projects, but suggestions and improvements are welcome!

---

## 📧 Contact

For questions or collaboration, feel free to reach out through GitHub issues or the contact form in the Blog Website project.

---

**Repository:** [ayush3739/Projects](https://github.com/ayush3739/Projects)  
**Last Updated:** December 2025