import re
import streamlit as st
import os
import random
import string
from dotenv import load_dotenv, find_dotenv
from litellm import completion

# Load environment variables
_: bool = load_dotenv(find_dotenv())
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# Initialize session state for password history and generated password
if "password_history" not in st.session_state:
    st.session_state.password_history = []
if "generated_password" not in st.session_state:
    st.session_state.generated_password = ""

def check_password_strength(password: str) -> str:
    score = 0
    feedback = []
    
    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase length to at least 8 characters.")
    
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Use at least one special character (!@#$%^&*).")
    
    # Assigning strength level
    if score == 5:
        return "Strong Password! ✅"
    elif score >= 3:
        return "Moderate Password. Consider improving: " + ", ".join(feedback)
    else:
        return "Weak Password! ❌ Improve: " + ", ".join(feedback)

def generate_strong_password() -> str:
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))

def get_llm_feedback(password: str) -> str:
    prompt = f"Analyze the security of the password '{password}' and provide detailed recommendations for improvement."
    try:
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": prompt}],
            api_key=GEMINI_API_KEY
        )
        
        if "choices" in response and response["choices"]:
            return response["choices"][0].get("message", {}).get("content", "Could not generate feedback.").strip()
        return "Could not generate feedback. Please try again."
    except Exception as e:
        return f"Error generating feedback: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")
st.title("🔐 Password Strength Meter")
st.markdown("### Check how secure your password is! 🔍")

password = st.text_input("Enter your password:", type="password")
if st.button("Check Strength", key="check"):
    if password:
        result = check_password_strength(password)
        
        # Save to history
        st.session_state.password_history.append({"password": password, "result": result})
        
        st.success(result)
        
        # Show suggestion and Generate button if weak password
        if "Weak Password" in result:
            st.session_state.generated_password = generate_strong_password()
            st.markdown("### Suggested Strong Password 🔒")
            st.code(st.session_state.generated_password, language="text")
            if st.button("Generate Strong Password"):
                st.session_state.generated_password = generate_strong_password()
                st.experimental_rerun()
        
        # Get LLM feedback
        st.markdown("### AI Security Recommendations 🧠")
        llm_feedback = get_llm_feedback(password)
        st.info(llm_feedback)
    else:
        st.warning("Please enter a password to check.")

# Show password history
st.markdown("### 🔄 Previous Password Checks")
if st.session_state.password_history:
    for entry in reversed(st.session_state.password_history[-5:]):  # Show last 5 entries
        st.write(f"🔑 **{entry['password']}** → {entry['result']}")
else:
    st.write("No password history yet.")
    




