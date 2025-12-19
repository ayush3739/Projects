# Flask WTForms Login Application

A Flask web application demonstrating advanced form handling using Flask-WTF and WTForms with validation, Bootstrap styling, and authentication logic.

## Features
- **WTForms Integration**: Professional form handling with Flask-WTF
- **Form Validation**: Built-in validators for email and password fields
- **Bootstrap Styling**: Clean UI with Flask-Bootstrap5 integration
- **Email Validation**: Ensures valid email format
- **Password Length Validation**: Minimum 8 character requirement
- **Authentication Logic**: Basic login credential verification
- **CSRF Protection**: Automatic CSRF token generation and validation
- **Success/Denied Pages**: Different responses based on credentials

## Pages
- **Home Page** (`/`): Landing page
- **Login Page** (`/login`): Login form with validation
- **Success Page**: Displayed on successful login
- **Denied Page**: Displayed on failed login attempt

## How to Use
1. Install required dependencies:
   ```bash
   pip install Flask Flask-WTF Flask-Bootstrap5 WTForms email-validator
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

4. Click on login and enter credentials:
   - **Email**: admin@email.com
   - **Password**: 12345678

## Form Validation Features
- **Email Field**:
  - Required field validation
  - Email format validation
  - Custom error messages

- **Password Field**:
  - Required field validation
  - Minimum length validation (8 characters)
  - Password masking in UI

## Technical Details
- **Form Class**: Custom `Myform` class inheriting from FlaskForm
- **Validators**: DataRequired, Email, length validators from WTForms
- **Bootstrap**: Flask-Bootstrap5 for responsive design
- **CSRF Protection**: Automatic token handling by Flask-WTF
- **Secret Key**: Required for session and CSRF protection

## Files Structure
- `main.py` - Flask application with WTForms integration
- `templates/` - HTML templates
  - `base.html` - Base template with Bootstrap
  - `index.html` - Home page
  - `login.html` - Login form page
  - `success.html` - Successful login page
  - `denied.html` - Access denied page
- `requirements.txt` - Python dependencies

## Code Highlights

### Form Definition
```python
class Myform(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), length(min=8)])
    submit = SubmitField(label="Log In")
```

### Form Validation
```python
@app.route("/login", methods=["GET","POST"])
def login():
    login_form = Myform()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" or login_form.password.data == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=login_form)
```

## Learning Concepts
- Flask-WTF integration for secure forms
- WTForms field types and validators
- Bootstrap integration with Flask-Bootstrap5
- CSRF protection implementation
- Form validation and error handling
- Conditional rendering based on form state
- Template inheritance with Jinja2
- Session management with secret keys

## Validators Used
- **DataRequired**: Ensures field is not empty
- **Email**: Validates email format
- **length**: Ensures minimum/maximum length requirements

## Security Features
- CSRF token protection (automatic)
- Password field masking
- Server-side validation
- Secret key for session security

## Requirements
- Python 3.x
- Flask 2.3.2
- Flask-WTF 1.2.1
- WTForms 3.0.1
- Bootstrap-Flask 2.2.0
- email-validator 2.3.0

## Important Notes
**Authentication Logic Issue**: The current code uses `or` instead of `and` for credential checking:
```python
# Current (accepts either correct email OR correct password)
if login_form.email.data == "admin@email.com" or login_form.password.data == "12345678":

# Should be (requires both correct email AND correct password)
if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
```

## Next Steps for Enhancement
- Fix authentication logic (use `and` instead of `or`)
- Implement proper user database
- Add password hashing
- Create user registration
- Add remember me functionality
- Implement logout functionality
- Add flash messages for errors
- Create user session management

Perfect for learning professional form handling with WTForms and Flask-Bootstrap integration!
