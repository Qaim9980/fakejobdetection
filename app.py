import streamlit as st
import joblib
import re
import nltk
import os
from nltk.corpus import stopwords

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

# Set up NLTK data
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

stop_words = stopwords.words('english')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

# Set page config
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="🛡",
    layout="wide"
)

# Load Models with error handling
@st.cache_resource
def load_models():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        job_model = joblib.load(os.path.join(base_path, "model/job_model.pkl"))
        phish_model = joblib.load(os.path.join(base_path, "model/phishing_model.pkl"))
        vectorizer = joblib.load(os.path.join(base_path, "model/vectorizer.pkl"))
        return job_model, phish_model, vectorizer
    except Exception as e:
        st.error(f"Error loading models: {e}")
        st.stop()

job_model, phish_model, vectorizer = load_models()

# Title and description
st.title("🛡 Intelligent Job Fraud & Phishing Detection System")
st.markdown("---")
st.write("Detect fraudulent job postings and phishing emails using Machine Learning")

# Two columns layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Settings")
    option = st.radio(
        "Detection Type:",
        ("Fake Job Detection", "Phishing Message Detection"),
        help="Choose what type of content to analyze"
    )

with col2:
    st.subheader("Analyzer")
    user_input = st.text_area(
        "Paste job post / email / message here:",
        height=200,
        placeholder="Enter text to analyze..."
    )

# Analysis button
if st.button("🔍 Analyze", use_container_width=True):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            cleaned = clean_text(user_input)
            vect_text = vectorizer.transform([cleaned])

            if option == "Fake Job Detection":
                result = job_model.predict(vect_text)[0]
                prob = job_model.predict_proba(vect_text)[0]
            else:
                result = phish_model.predict(vect_text)[0]
                prob = phish_model.predict_proba(vect_text)[0]

            # Results display
            st.markdown("---")
            
            if result == 1:
                # FRAUD/PHISHING detected
                col1, col2 = st.columns(2)
                with col1:
                    st.error(f"🚨 FRAUD DETECTED" if option == "Fake Job Detection" else f"🚨 PHISHING DETECTED")
                with col2:
                    st.metric("Confidence Score", f"{max(prob)*100:.2f}%", delta="High Risk")
                    
                st.markdown("""
                ### ⚠️ Warning
                This content appears to be fraudulent. 
                - Do not engage with this posting/email
                - Report it to the platform
                - Do not share personal information
                """)
            else:
                # GENUINE
                col1, col2 = st.columns(2)
                with col1:
                    st.success(f"✅ GENUINE" if option == "Fake Job Detection" else f"✅ LEGITIMATE")
                with col2:
                    st.metric("Confidence Score", f"{max(prob)*100:.2f}%", delta="Safe")
                    
                st.markdown("""
                ### ✓ Safe
                This content appears to be legitimate.
                You can proceed with caution and verify details.
                """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>🧠 Powered by Machine Learning | TF-IDF + Naive Bayes</p>
    <small>Job Fraud & Phishing Detection System v1.0</small>
</div>
""", unsafe_allow_html=True)
