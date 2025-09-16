# django-authentication-system
# Django Authentication System

A fully functional **Django Authentication System** that handles user registration, login, logout, and email verification. This project uses Django’s built-in authentication along with custom validations for email, username, and optional Captcha for extra security.

---

## Features

- **User Registration**
  - Username uniqueness validation
  - Email validation (checks for format and duplicates)
  - Password validation using Django's built-in `UserCreationForm`
  - Optional Captcha for bot prevention
  - Sends welcome email after successful registration

- **User Login**
  - Login using username and password
  - Error messages for invalid credentials

- **User Logout**
  - Secure logout functionality

- **Email Functionality**
  - Sends email using Gmail SMTP
  - Configurable for custom sender email
  - Can be extended for password reset or verification links

- **Form Validation**
  - Clean methods for email, username, and passwords
  - Prevents duplicate emails and invalid inputs

---

## Screenshots

*Optional: Add screenshots here of your registration, login, or email sent page*

---

## Technologies Used

- Django 4.x
- Python 3.9+
- HTML5, CSS3
- Bootstrap 5 (for styling)
- Django Captcha (optional)
- Gmail SMTP for email

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/django-authentication-system.git
cd django-authentication-system
