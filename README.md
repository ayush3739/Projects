# 🚀 Projects Portfolio

Welcome to my projects repository! This collection showcases various web applications and tools I've built using Python, Flask, and modern web technologies.

## 📋 Table of Contents
- [Featured Projects](#-featured-projects)
- [All Projects](#-all-projects)
- [Technologies Used](#-technologies-used)
- [Getting Started](#-getting-started)

## ⭐ Featured Projects

### 🌟 Blog Website
A full-featured blog platform with comprehensive user management and rich content creation capabilities.

**Key Features:**
- 🔐 **User Authentication System** - Secure registration and login with password hashing
- 👨‍💼 **Admin Controls** - Role-based access for content management
- ✍️ **Rich Text Editor** - CKEditor integration for beautiful blog post formatting
- 💬 **Comments System** - Interactive discussion threads on blog posts
- ����️ **Gravatar Integration** - Automatic avatar generation for user profiles
- 📧 **SMTP Email Contact Form** - Direct communication with site administrators
- 📱 **Responsive Bootstrap UI** - Mobile-friendly design that works on all devices
- 🗄️ **SQLite Database** - Efficient data storage and retrieval

**Tech Stack:** Flask, SQLAlchemy, Flask-Login, Flask-CKEditor, Bootstrap 5, WTForms

**Status:** Production Ready ✅

---

### ✈️ Flight Deals Finder
Never miss a great flight deal! This automated tool monitors flight prices and sends email alerts when prices drop below your target.

**Key Features:**
- 🔍 Real-time flight price monitoring using Amadeus API
- 📧 Automated email notifications for price drops
- 🌍 Multi-destination tracking
- 💰 Custom price threshold settings
- 📊 Google Sheets integration for deal management

**Tech Stack:** Python, Amadeus API, SMTP, Google Sheets API

---

### ☕ Coffee and Wifi Cafe Tracker
A community-driven platform to discover and rate cafes based on wifi quality, power outlet availability, and coffee quality.

**Key Features:**
- 📍 Cafe location mapping
- ⭐ User ratings and reviews
- 🔌 Power outlet availability tracking
- 📶 Wifi speed ratings
- ☕ Coffee quality assessments
- 📱 Responsive design for on-the-go cafe hunting

**Tech Stack:** Flask, SQLAlchemy, Bootstrap, WTForms

---

### 🏃 Exercise Tracker
Track your workouts automatically using natural language processing powered by Nutritionix API.

**Key Features:**
- 💬 Natural language exercise input (e.g., "ran 5km in 30 minutes")
- 📊 Automatic calorie calculation
- 📈 Workout history tracking via Google Sheets
- ⏱️ Duration and intensity tracking
- 📅 Date-stamped exercise logs

**Tech Stack:** Python, Nutritionix API, Google Sheets API

---

## 📚 All Projects

### Web Applications
1. **Blog Website** - Full-featured blogging platform with authentication and admin controls
2. **Coffee and Wifi Cafe Tracker** - Find the best cafes for remote work
3. **Top Movies Website** - Personal movie ranking and review platform
4. **RESTful Blog API** - Backend API for blog operations
5. **Library Management System** - Track and manage book collections
6. **Cafe API** - RESTful API for cafe data management

### Automation & Tools
7. **Flight Deals Finder** - Automated flight price monitoring and alerts
8. **Exercise Tracker** - NLP-powered workout logging
9. **Habit Tracker** - Build and maintain healthy habits with Pixela API
10. **Stock News Alert** - Get notified about significant stock price movements
11. **Rain Alert** - Weather-based SMS notifications
12. **Birthday Wisher** - Automated birthday email sender
13. **ISS Overhead Notifier** - Get notified when ISS passes overhead

### Games & Fun
14. **Higher Lower Game** - Guess which celebrity has more Instagram followers
15. **NATO Alphabet Converter** - Convert text to NATO phonetic alphabet
16. **Password Manager** - Secure password generation and storage
17. **Flash Card App** - Language learning tool
18. **Pomodoro Timer** - Productivity timer application

### Data & APIs
19. **US States Game** - Interactive geography quiz
20. **Quizzler App** - Trivia quiz application
21. **Kanye Quotes** - Random Kanye West quote generator

## 🛠️ Technologies Used

- **Backend:** Python, Flask, SQLAlchemy, Flask-Login, Flask-Bootstrap
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** SQLite, PostgreSQL
- **APIs:** Amadeus, Nutritionix, OpenWeatherMap, Alpha Vantage, Twilio
- **Tools:** Git, RESTful API Design, WTForms, CKEditor
- **Authentication:** Flask-Login, Werkzeug Security

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ayush3739/Projects.git
cd Projects
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to any project directory:
```bash
cd <project-name>
```

5. Follow project-specific setup instructions in individual project folders.

### Running Projects

Most Flask applications can be run with:
```bash
python main.py
```
or
```bash
flask run
```

Then visit `http://localhost:5000` in your web browser.

## 📝 Notes

- Each project folder contains its own README with specific setup instructions
- API keys are required for projects using external services
- Environment variables should be stored in `.env` files (not included in repository)
- Sample `.env.example` files are provided where applicable

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📧 Contact

For questions or collaborations, feel free to reach out!

---

**Made with ❤️ and Python**
