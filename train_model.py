import pandas as pd
import re
import joblib
import nltk
import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

print("Downloading NLTK stopwords...")
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

stop_words = stopwords.words('english')

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)

print("Loading datasets...")
try:
    # ================= JOB SCAM DATA =================
    job_df = pd.read_csv("data/fake_job_postings.csv")
    job_df['text'] = job_df['title'].fillna('') + " " + job_df['description'].fillna('')
    job_df['text'] = job_df['text'].apply(clean_text)

    X_job = job_df['text']
    y_job = job_df['fraudulent']

    # ================= PHISHING DATA =================
    phish_df = pd.read_csv("data/Phishing_Email.csv")
    phish_df['text'] = phish_df['Email Text'].apply(clean_text)
    phish_df['label'] = (phish_df['Email Type'] == 'Phishing Email').astype(int)

    X_phish = phish_df['text']
    y_phish = phish_df['label']

    print("✅ Datasets loaded successfully")
    print(f"   Job postings: {len(job_df)} samples")
    print(f"   Phishing emails: {len(phish_df)} samples")

except Exception as e:
    print(f"❌ Error loading datasets: {e}")
    print("Make sure data/fake_job_postings.csv and data/phishing_emails.csv exist")
    exit(1)

print("\nVectorizing text...")
try:
    # ================= VECTORIZE =================
    vectorizer = TfidfVectorizer(max_features=5000)

    X_job_vec = vectorizer.fit_transform(X_job)
    X_phish_vec = vectorizer.transform(X_phish)
    
    print("✅ Vectorization complete")
    print(f"   Features extracted: {X_job_vec.shape[1]}")

except Exception as e:
    print(f"❌ Error during vectorization: {e}")
    exit(1)

print("\nTraining models...")
try:
    # ================= TRAIN MODELS =================
    job_model = MultinomialNB()
    phish_model = MultinomialNB()

    job_model.fit(X_job_vec, y_job)
    phish_model.fit(X_phish_vec, y_phish)

    print("✅ Models trained successfully")

except Exception as e:
    print(f"❌ Error during training: {e}")
    exit(1)

print("\nSaving models...")
try:
    # ================= SAVE MODELS =================
    # Create model directory if it doesn't exist
    os.makedirs("model", exist_ok=True)
    
    joblib.dump(job_model, "model/job_model.pkl")
    joblib.dump(phish_model, "model/phishing_model.pkl")
    joblib.dump(vectorizer, "model/vectorizer.pkl")

    print("✅ Models saved successfully")
    print("   job_model.pkl saved")
    print("   phishing_model.pkl saved")
    print("   vectorizer.pkl saved")

except Exception as e:
    print(f"❌ Error saving models: {e}")
    exit(1)

print("\n" + "="*60)
print("✅ MODEL TRAINING COMPLETE!")
print("="*60)
print("\nNext step: Run the Streamlit app")
print("Command: streamlit run app.py")
print("Or double-click: run_app.bat")

