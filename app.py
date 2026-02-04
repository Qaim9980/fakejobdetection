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
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
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

# Custom CSS for better UI
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    }
    .info-box {
        background: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class='main-header'>
    <h1>🛡️ Intelligent Fraud Detection System</h1>
    <p style='font-size: 1.2rem; margin-top: 0.5rem;'>AI-Powered Job Fraud & Phishing Email Detection</p>
</div>
""", unsafe_allow_html=True)

# Info cards
col_info1, col_info2, col_info3 = st.columns(3)
with col_info1:
    st.markdown("""
    <div class='info-box'>
        <h3>🎯 Accurate</h3>
        <p>Machine Learning powered detection with high accuracy</p>
    </div>
    """, unsafe_allow_html=True)
with col_info2:
    st.markdown("""
    <div class='info-box'>
        <h3>⚡ Fast</h3>
        <p>Real-time analysis in seconds</p>
    </div>
    """, unsafe_allow_html=True)
with col_info3:
    st.markdown("""
    <div class='info-box'>
        <h3>🔒 Secure</h3>
        <p>Your data stays private</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Two columns layout
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### ⚙️ Detection Settings")
    option = st.radio(
        "Select Detection Type:",
        ("Fake Job Detection", "Phishing Message Detection"),
        help="Choose what type of content to analyze",
        index=0
    )
    
    st.markdown("---")
    st.markdown("""
    **💡 Tips:**
    - Paste the complete text
    - Include all details for better accuracy
    - Results are instant
    """)

with col2:
    st.markdown("### 📝 Text Analyzer")
    user_input = st.text_area(
        "Paste your job posting or email message here:",
        height=250,
        placeholder="📋 Example:\n\nJob Title: Software Developer\nCompany: ABC Tech\nDescription: We are looking for...\n\nOR\n\nDear User,\nYour account requires verification..."
    )

# Analysis button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("🔍 Analyze Now", use_container_width=True):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        with st.spinner("🔄 Analyzing content..."):
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
            st.markdown("### 📊 Analysis Results")
            
            if result == 1:
                # FRAUD/PHISHING detected
                st.markdown("""
                <div style='background: linear-gradient(135deg, #ff6b6b, #ee5a6f); 
                            padding: 2rem; border-radius: 10px; color: white;'>
                    <h2 style='margin:0;'>🚨 WARNING: FRAUD DETECTED!</h2>
                    <p style='font-size: 1.3rem; margin-top: 1rem;'>
                        Confidence: <strong>{:.1f}%</strong>
                    </p>
                </div>
                """.format(max(prob)*100), unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Risk Level", "🔴 High", delta="Dangerous")
                with col2:
                    st.metric("Threat Type", "Fraud" if option == "Fake Job Detection" else "Phishing")
                with col3:
                    st.metric("Action", "⛔ Block", delta="Required")
                    
                st.error("""
                ### ⚠️ Security Recommendations
                - ❌ **DO NOT** engage with this content
                - ❌ **DO NOT** share personal information
                - ❌ **DO NOT** click any links
                - ✅ Report to the platform immediately
                - ✅ Delete and block sender
                """)
            else:
                # GENUINE
                st.markdown("""
                <div style='background: linear-gradient(135deg, #11998e, #38ef7d); 
                            padding: 2rem; border-radius: 10px; color: white;'>
                    <h2 style='margin:0;'>✅ CONTENT APPEARS LEGITIMATE</h2>
                    <p style='font-size: 1.3rem; margin-top: 1rem;'>
                        Confidence: <strong>{:.1f}%</strong>
                    </p>
                </div>
                """.format(max(prob)*100), unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Risk Level", "🟢 Low", delta="Safe")
                with col2:
                    st.metric("Status", "Legitimate")
                with col3:
                    st.metric("Action", "✅ Proceed", delta="With Caution")
                    
                st.success("""
                ### ✓ Content Verified
                - ✅ This content appears to be genuine
                - ⚠️ Still verify details independently
                - ⚠️ Check company/sender reputation
                - ⚠️ Never share sensitive data hastily
                """)

# Footer
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
            padding: 2rem; border-radius: 10px; text-align: center; color: white;'>
    <h3>🧠 Powered by Advanced Machine Learning</h3>
    <p style='font-size: 1.1rem;'>TF-IDF Vectorization + Naive Bayes Classification</p>
    <hr style='border-color: rgba(255,255,255,0.3);'>
    <p><strong>Fraud Detection System v2.0</strong> | Protecting Users Worldwide 🌍</p>
    <small>© 2026 - Built with ❤️ using Python & Streamlit</small>
</div>
""", unsafe_allow_html=True)
