import joblib
import re
import nltk
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = [w for w in text.split() if w not in stop_words]
    return ' '.join(words)

job_model = joblib.load('model/job_model.pkl')
phish_model = joblib.load('model/phishing_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

# Test 1: Fake Job
print('='*60)
print('TEST 1: Fake Job Detection')
print('='*60)
test_job = 'QUICK MONEY!!! Make $5000 per week from home'
cleaned = clean_text(test_job)
vect_text = vectorizer.transform([cleaned])
result = job_model.predict(vect_text)[0]
prob = job_model.predict_proba(vect_text)[0][result]
print(f'Input: {test_job}')
status = 'FRAUDULENT' if result == 1 else 'GENUINE'
print(f'Result: {status}')
print(f'Confidence: {prob*100:.2f}%')

# Test 2: Real Job
print()
print('='*60)
print('TEST 2: Real Job Posting')
print('='*60)
test_job2 = 'Software Developer needed. Python and JavaScript skills required. Competitive salary.'
cleaned2 = clean_text(test_job2)
vect_text2 = vectorizer.transform([cleaned2])
result2 = job_model.predict(vect_text2)[0]
prob2 = job_model.predict_proba(vect_text2)[0][result2]
print(f'Input: {test_job2}')
status2 = 'FRAUDULENT' if result2 == 1 else 'GENUINE'
print(f'Result: {status2}')
print(f'Confidence: {prob2*100:.2f}%')

# Test 3: Phishing Email
print()
print('='*60)
print('TEST 3: Phishing Email Detection')
print('='*60)
test_phish = 'Your account has been locked. Click here to verify your password.'
cleaned3 = clean_text(test_phish)
vect_text3 = vectorizer.transform([cleaned3])
result3 = phish_model.predict(vect_text3)[0]
prob3 = phish_model.predict_proba(vect_text3)[0][result3]
print(f'Input: {test_phish}')
status3 = 'PHISHING' if result3 == 1 else 'LEGITIMATE'
print(f'Result: {status3}')
print(f'Confidence: {prob3*100:.2f}%')
