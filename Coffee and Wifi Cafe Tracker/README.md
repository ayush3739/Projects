# Coffee and Wifi Cafe Tracker

A Flask web application for tracking and rating cafes based on their coffee quality, wifi strength, and power socket availability. Features a searchable database of cafes with their amenities.

## Features
- **Cafe Database**: CSV-based storage for cafe information
- **Add New Cafes**: Form to submit new cafe entries with ratings
- **View All Cafes**: Browse complete list of cafes with all details
- **Rating System**: Emoji-based ratings for coffee, wifi, and power outlets
- **Location Tracking**: Google Maps URL integration for cafe locations
- **Operating Hours**: Track opening and closing times
- **WTForms Validation**: Professional form handling with validation
- **Bootstrap UI**: Clean, responsive interface with Flask-Bootstrap5

## Pages
- **Home Page** (`/`): Welcome page with navigation
- **Add Cafe** (`/add`): Form to add new cafe with ratings
- **All Cafes** (`/cafes`): Table view of all cafes in database

## How to Use
1. Install required dependencies:
   ```bash
   pip install Flask Flask-WTF Flask-Bootstrap5 WTForms
   ```
   Or use the requirements.txt file:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Navigate to `http://localhost:5000` in your browser

4. Add cafes or browse existing ones

## Rating System

### Coffee Quality
- ☕️ - Poor
- ☕☕ - Fair
- ☕☕☕ - Good
- ☕☕☕☕ - Very Good
- ☕☕☕☕☕ - Excellent

### Wifi Strength
- ✘ - No Wifi
- 💪 - Weak
- 💪💪 - Fair
- 💪💪💪 - Good
- 💪💪💪💪 - Strong
- 💪💪💪💪💪 - Excellent

### Power Socket Availability
- ✘ - No Sockets
- 🔌 - Few
- 🔌🔌 - Some
- 🔌🔌🔌 - Good
- 🔌🔌🔌🔌 - Many
- 🔌🔌🔌🔌🔌 - Abundant

## Form Fields
- **Cafe Name**: Text input (required)
- **Location URL**: Google Maps link (required, URL validation)
- **Opening Time**: e.g., "8AM" (required)
- **Closing Time**: e.g., "5:30PM" (required)
- **Coffee Rating**: Dropdown with emoji ratings (required)
- **Wifi Rating**: Dropdown with emoji ratings (required)
- **Power Rating**: Dropdown with emoji ratings (required)

## Technical Details
- **Database**: CSV file (`cafe-data.csv`) for data persistence
- **Form Class**: `CafeForm` with WTForms validators
- **URL Validation**: Ensures valid Google Maps links
- **UTF-8 Encoding**: Proper emoji support in CSV
- **Bootstrap Integration**: Responsive design with Flask-Bootstrap5

## Files Structure
- `main.py` - Flask application with routes and form handling
- `cafe-data.csv` - CSV database of cafe information
- `templates/` - HTML templates
  - `base.html` - Base template with Bootstrap
  - `index.html` - Home page
  - `add.html` - Add cafe form
  - `cafes.html` - Display all cafes
- `static/` - CSS and asset files
- `requirements.txt` - Python dependencies

## Code Highlights

### Form Definition
```python
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", 
                          validators=[DataRequired(), URL()])
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", 
                               choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], 
                               validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", 
                             choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], 
                             validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", 
                              choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], 
                              validators=[DataRequired()])
    submit = SubmitField('Submit')
```

### CSV Writing
```python
with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
    csv_file.write(f"\n{form.cafe.data},"
                   f"{form.location.data},"
                   f"{form.open.data},"
                   f"{form.close.data},"
                   f"{form.coffee_rating.data},"
                   f"{form.wifi_rating.data},"
                   f"{form.power_rating.data}")
```

## Learning Concepts
- Flask-WTF form handling
- CSV file operations (read/write)
- SelectField with custom emoji choices
- URL validation with WTForms
- UTF-8 encoding for emoji support
- Bootstrap integration for responsive UI
- Form validation and error handling
- Redirect after POST pattern
- Data persistence with CSV
- Table rendering in Jinja2

## Validators Used
- **DataRequired**: Ensures field is not empty
- **URL**: Validates proper URL format
- **SelectField**: Dropdown with predefined choices

## Security Features
- CSRF token protection (automatic via Flask-WTF)
- URL validation prevents invalid links
- Required field validation
- Secret key for session security

## Requirements
- Python 3.x
- Flask 2.3.2
- Flask-WTF 1.2.1
- WTForms 3.0.1
- Bootstrap-Flask 2.2.0
- Werkzeug 3.0.0

## Database Schema (CSV)
```
Cafe Name, Location, Open, Close, Coffee, Wifi, Power
```

## Use Cases
- Digital nomads finding work-friendly cafes
- Coffee enthusiasts tracking favorite spots
- Remote workers locating cafes with good wifi
- Students finding study locations
- Travelers exploring local cafe scenes

## Next Steps for Enhancement
- Migrate to SQLite/PostgreSQL database
- Add search and filter functionality
- Implement cafe ratings and reviews
- Add user authentication
- Include cafe images
- Add edit/delete functionality
- Implement sorting (by rating, name, etc.)
- Add map view with markers
- Create cafe detail pages
- Add favorite/bookmark feature

Perfect for learning Flask forms, CSV operations, and building a practical CRUD application with a beautiful UI!
