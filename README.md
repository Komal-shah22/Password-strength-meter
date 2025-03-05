# Password Strength Meter

## Overview

This is a **Password Strength Meter** web application built using **Streamlit**. It allows users to check the strength of their passwords and provides feedback on how to improve weak passwords. Additionally, it suggests a strong password and provides AI-based security recommendations.

## Features

- **Password Strength Checker**: Evaluates passwords based on length, uppercase, lowercase, digits, and special characters.
- **Strong Password Generator**: Generates a secure random password.
- **AI-based Feedback**: Uses the Gemini AI model to provide security recommendations.
- **Password History**: Displays the last 5 checked passwords with their strength ratings.
- **User-Friendly Interface**: Built using **Streamlit** for easy interaction.

## Installation & Setup

### Prerequisites

Make sure you have the following installed:

- Python (>= 3.8)
- pip (Python package manager)

### Install Dependencies

```bash
pip install streamlit python-dotenv litellm
```

### Set Up Environment Variables

Create a **.env** file and add your **Gemini API Key**:

```
GEMINI_API_KEY=your_api_key_here
```

### Run the Application

```bash
streamlit run app.py
```

## How It Works

1. **User Input**:
   - The user enters a password in the input field.
   - Clicks on the **Check Strength** button.
2. **Password Strength Analysis**:
   - The password is checked for:
     - Minimum length (>=8 characters)
     - At least one uppercase letter
     - At least one lowercase letter
     - At least one digit (0-9)
     - At least one special character (!@#\$%^&\*)
   - A message is displayed indicating whether the password is **Strong, Moderate, or Weak**.
3. **Password Suggestions**:
   - If the password is weak, a **strong password** is suggested.
   - The user can generate another strong password with a button click.
4. **AI-based Security Recommendations**:
   - The app sends the password to the **Gemini AI model**.
   - It returns a **detailed security analysis and improvement tips**.
5. **Password History**:
   - Stores and displays the last **5 checked passwords** and their strength ratings.

## Technologies Used

- **Python**
- **Streamlit** (for UI)
- **re (Regex)** (for password validation)
- **random & string** (for password generation)
- **dotenv** (for managing API keys securely)
- **litellm** (for integrating with Gemini AI)

## Future Improvements

- Add a real-time password strength indicator.
- Implement a database for storing password history.
- Add an option for users to customize password generation criteria.

---

### Author

**Developed by:** [Komal Shah]

"# Password-strength-meter" 
