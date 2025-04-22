import streamlit as st
from detector.predict import detect_ai_text
from converter.convert import convert_to_human

st.set_page_config(page_title="AI Detector & Humanizer", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stTextInput>div>div>input { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Content Detector & 🧠 Humanizer")

menu = st.radio("Choose Tool:", ("Detect AI Content", "Humanize Content"))
text = st.text_area("Paste your content here:", height=300)

if menu == "Detect AI Content" and text:
    label, prob = detect_ai_text(text)
    st.success(f"Prediction: {label} ({prob*100:.2f}% confidence)")

elif menu == "Humanize Content" and text:
    rewritten = convert_to_human(text)
    st.text_area("Humanized Content:", rewritten, height=300)