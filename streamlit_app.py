import streamlit as st
import joblib
import re
import string

# Load model and vectorizer
model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

# App UI
st.set_page_config(page_title="Fake SMS Detector", page_icon="📱")
st.title("📩 Fake SMS Detector")
st.markdown("Enter an SMS message below to check if it's spam or not.")

sms = st.text_area("📨 Enter SMS text here:", height=150)

if st.button("🔍 Predict"):
    if sms.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(sms)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)[0]
        if prediction == 1:
            st.error("🚨 This is a SPAM message!")
        else:
            st.success("✅ This is a legitimate (HAM) message.")
