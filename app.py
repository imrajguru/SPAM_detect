import streamlit as st
import pickle
import numpy as np

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Spam Detector",
    page_icon="📧",
    layout="centered"
)

# ----------------------------
# Load Model & Vectorizer
# ----------------------------
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ----------------------------
# Custom Styling
# ----------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-size: 16px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.title("📌 About Project")
st.sidebar.info("""
This Spam Detection system uses Machine Learning 
to classify messages as Spam or Not Spam.

Model trained using NLP techniques.
""")

st.sidebar.markdown("### 🛠 Tech Stack")
st.sidebar.write("• Python")
st.sidebar.write("• Scikit-learn")
st.sidebar.write("• Streamlit")
st.sidebar.write("• NLP (TF-IDF)")

# ----------------------------
# Main UI
# ----------------------------
st.title("📧 Spam Message Detector")
st.write("Enter a message below to check whether it is Spam or Not Spam.")

user_input = st.text_area("✍️ Enter your message here:", height=150)

if st.button("🔍 Analyze Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message before analyzing.")
    else:
        transformed_input = vectorizer.transform([user_input])
        prediction = model.predict(transformed_input)
        probability = model.predict_proba(transformed_input)

        confidence = np.max(probability) * 100

        st.markdown("---")

        if prediction[0] == 1:
            st.error(f"🚨 Spam Detected!")
            st.write(f"Confidence: **{confidence:.2f}%**")
        else:
            st.success(f"✅ This message is Not Spam.")
            st.write(f"Confidence: **{confidence:.2f}%**")

        st.progress(int(confidence))

st.markdown("---")
st.caption("Developed by Rajguru Thevar | ML Internship Project")