import streamlit as st
import random
import string
import re


def check_strength(password):
    score = sum([
        len(password) >= 8,
        any(c.isupper() for c in password),
        any(c.islower() for c in password),
        any(c.isdigit() for c in password),
        any(c in "@$!%*?&" for c in password)
    ])
    return ["🔴 Weak", "🟡 Moderate", "🟢 Strong"][min(score, 2)]

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "@$!%*?&", k=12))

st.title("🔐 Password Strength Meter")
password = st.text_input("Enter password:", type="password")

if st.button("Check Strength"):
    st.success(check_strength(password) if password else "Please enter a password!")

if st.button("Generate Strong Password"):
    st.info(f"Generated: {generate_password()}")