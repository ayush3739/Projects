# Blog Website (Flask)

A full-featured blog built with Flask, featuring user authentication, admin-only post management, rich text editing, comments, Gravatar avatars, Bootstrap styling, and SMTP email for contact messages.

---

## Overview

This project implements a simple yet complete blogging platform using Flask and SQLAlchemy. Admins can create, edit, and delete posts; authenticated users can comment; and anyone can browse posts. The app includes a contact form powered by SMTP (Gmail) and supports rich text editing via CKEditor.

Key application entrypoint: [PROJECTS/Blog Website/main.py](PROJECTS/Blog%20Website/main.py)

---

## Features

- **User Auth:** Register, login, logout using `Flask-Login` with hashed passwords.
- **Admin Controls:** `admin_only` decorator protects post creation, editing, and deletion.
- **Rich Editing:** Post bodies created/edited with `Flask-CKEditor`.
- **Responsive UI:** `Flask-Bootstrap (Bootstrap5)` for modern styling.
- **Avatars:** `Flask-Gravatar` for user avatars in comments.
- **Comments:** Authenticated users can comment on posts; comments timestamped.
- **Email Contact:** Contact form sends emails via Gmail SMTP with app password.
- **Persistent Storage:** `SQLite` database with typed SQLAlchemy models.
- **Flash Messages:** Clear UX feedback for auth, errors, and actions.

---

## Tech Stack

- **Backend:** Flask, Flask-Login, Flask-SQLAlchemy, Werkzeug security
- **Frontend:** Jinja2 templates, Bootstrap 5 via Flask-Bootstrap, CKEditor
- **Avatars:** Flask-Gravatar
- **Email:** `smtplib` using Gmail SMTP
- **Config:** `python-dotenv` for environment variables
- **DB:** SQLite (via SQLAlchemy ORM)

---

## Project Structure

- **App:** [PROJECTS/Blog Website/main.py](PROJECTS/Blog%20Website/main.py)
- **Forms:** [PROJECTS/Blog Website/forms.py](PROJECTS/Blog%20Website/forms.py) (e.g., `CreatePostForm`, `RegisterForm`, `LoginForm`, `CommentForm`)
- **Templates:** Typical Jinja templates (e.g., `index.html`, `post.html`, `make-post.html`, `register.html`, `login.html`, `contact.html`, `about.html`)
- **Database:** `sqlite:///posts.db` configured in the app
- **Config:** `.env` file for secrets and email settings

---

## Environment Variables

Create a `.env` file in the project folder with:

- **`secret_key`**: Flask `SECRET_KEY` for sessions.
- **`email`**: Gmail address used to send contact emails.
- **`pass`**: Gmail App Password (not your normal password).
- **`to_email`**: Recipient address for contact form messages.

Example `.env`:

```
secret_key=super-secret-key
email=your-gmail@example.com
pass=your-gmail-app-password
to_email=recipient@example.com
```

Notes:
- Use Google App Passwords with 2FA enabled; normal passwords won’t work.
- The app reads envs via `python-dotenv` (`load_dotenv(".env")`).

---

## Database Models

Defined in [PROJECTS/Blog Website/main.py](PROJECTS/Blog%20Website/main.py) using SQLAlchemy 2.0 typed mappings:

- **`User`**
  - `id`, `email` (unique), `password` (hashed), `name`, `is_admin` (bool)
  - Relationships: `posts`, `comments`
- **`BlogPost`**
  - `id`, `author_id`, `title` (unique), `subtitle`, `date` (string), `body` (Text), `img_url`
  - Relationships: `author` (`User`), `comments`
- **`Comments`**
  - `id`, `author_id`, `post_id`, `text` (<= 300 chars), `created_at` (UTC)
  - Relationships: `comment_author` (`User`), `parent_post` (`BlogPost`)

---

## Routes

- **`/`**: List all posts.
- **`/register`**: Sign up a new user.
- **`/login`**: Login existing user.
- **`/logout`**: Logout current user.
- **`/post/<int:post_id>`**: View a single post and its comments; submit comment when logged in.
- **`/new-post`**: Create a post (admin-only).
- **`/edit-post/<int:post_id>`**: Edit a post (admin-only).
- **`/delete/<int:post_id>`**: Delete a post (admin-only).
- **`/about`**: About page.
- **`/contact`**: Contact page; sends SMTP email (requires login).
- **`/debug/user/<int:user_id>`**: Admin-only JSON view of a user and their posts.

---

## How It Works

- **Auth:** `Flask-Login` tracks `current_user`. Passwords hashed via `werkzeug.security` (`pbkdf2:sha256`).
- **Admin Gate:** The custom `admin_only` decorator aborts with `403` unless the user is authenticated and `is_admin=True`.
- **Editor:** CKEditor enables rich-text body editing for posts.
- **Comments:** Authenticated users post comments; each comment stores author, post, text, timestamp.
- **Email:** Contact form builds an `EmailMessage` and sends via Gmail SMTP (`smtp.gmail.com:587`) with TLS.
- **UI:** Bootstrap 5 + Jinja templates provide a clean, responsive presentation.

---

## Setup & Run

1. **Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. **Install dependencies**

```bash
pip install flask flask-bootstrap flask-ckeditor flask-gravatar flask-login flask-sqlalchemy python-dotenv
```

3. **Configure environment**

- Create `.env` with `secret_key`, `email`, `pass`, `to_email`.

4. **Initialize the database**

- The app auto-creates tables on startup (`db.create_all()` inside app context).

5. **Run the app**

```bash
python PROJECTS/Blog\ Website/main.py
```

- Access at `http://127.0.0.1:5000/`.

---

## Setting an Admin User

By default, new users are not admins. Mark a user as admin manually (e.g., in a Python shell):

```python
from PROJECTS.Blog_Website.main import app, db, User

with app.app_context():
    user = db.session.execute(db.select(User).where(User.email == "you@example.com")).scalar_one()
    user.is_admin = True
    db.session.commit()
```

Notes:
- The project intentionally avoids any UI to self-promote to admin.

---

## Email Contact Setup

- Use a Gmail account with 2FA and generate an App Password.
- Put the Gmail address in `email`, the App Password in `pass`, and your destination inbox in `to_email`.
- The contact route requires login and will flash success/error messages.

---

## Security Considerations

- **Secrets in `.env`**: Do not commit `.env` to version control.
- **Hashed Passwords**: Uses PBKDF2 with salt via `werkzeug.security`.
- **Admin Restriction**: Critical write routes guarded by `admin_only`.
- **SMTP**: Uses TLS and App Passwords for Gmail.

---

## What I Used & How I Built It

- **Flask + SQLAlchemy**: Set up app factory-like config, defined typed models, and relationships.
- **Auth Flow**: Implemented register/login/logout with password hashing and `Flask-Login` session management.
- **Admin Decorator**: Wrote `admin_only` (`functools.wraps`) to enforce authorization on write routes.
- **Forms + Templates**: Built forms (WTForms/Flask-WTF patterns in `forms.py`) and Jinja templates for pages.
- **CKEditor Integration**: Enabled rich text for `BlogPost.body` fields.
- **Bootstrap Styling**: Wrapped templates with Bootstrap 5 for responsive design.
- **Comments System**: Created `Comments` model and submission logic with validation and user feedback.
- **Email Contact**: Wired `smtplib` with `EmailMessage` for sending contact messages securely.
- **Environment Management**: Used `python-dotenv` to load secrets and `SECRET_KEY` during init.

---

## Next Steps / Ideas

- **requirements.txt**: Capture exact dependencies and versions.
- **Admin UI**: Minimal admin dashboard for user management.
- **Pagination**: Add pagination for posts and comments.
- **Search**: Implement full-text search for posts.
- **Images**: Support local upload or cloud storage for `img_url`.

---

## License

This is an educational project as part of a Python learning journey.
