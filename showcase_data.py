"""
Showcase of Sample Data with Test Cases
Run this to see how the system performs on various inputs
"""

import joblib
import re
import nltk
from nltk.corpus import stopwords

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

# Load models
job_model = joblib.load('model/job_model.pkl')
phish_model = joblib.load('model/phishing_model.pkl')
vectorizer = joblib.load('model/vectorizer.pkl')

print("="*70)
print("SAMPLE DATA DEMONSTRATION")
print("="*70)

# Sample test cases
test_cases = [
    {
        "category": "Fake Job - Money Promise",
        "type": "job",
        "text": "QUICK MONEY GUARANTEED!!! Make 5000 dollars per week from home! No experience needed whatsoever. Send 50 dollars for starter kit.",
        "expected": "FRAUDULENT"
    },
    {
        "category": "Real Job - Software Engineer",
        "type": "job",
        "text": "Software Engineer position at Amazon Seattle office. 10+ years experience. Work on cloud infrastructure. Salary 180k-220k plus stock options.",
        "expected": "GENUINE"
    },
    {
        "category": "Fake Job - Nigerian Scam",
        "type": "job",
        "text": "SPECIAL OFFER FROM BANK NIGERIA. Dear Friend You have been chosen for a special job opportunity. You will earn 500000 naira monthly. Send registration fee of 200 dollars now.",
        "expected": "FRAUDULENT"
    },
    {
        "category": "Real Job - Healthcare",
        "type": "job",
        "text": "Healthcare Professional - Healthcare clinic seeking nurses and doctors. Competitive benefits package. Sign-on bonus available. Flexible scheduling.",
        "expected": "GENUINE"
    },
    {
        "category": "Fake Job - Investment Scam",
        "type": "job",
        "text": "MAKE 100K GUARANTEED. Invest just 1000 dollars and make 10000 dollars in 30 days. Guaranteed returns with our proven investment system. No risk involved!",
        "expected": "FRAUDULENT"
    },
    {
        "category": "Real Job - Accountant",
        "type": "job",
        "text": "CPA accountant needed for medium sized firm. 5+ years experience required. Tax preparation and audit experience needed. 75k-95k salary. Benefits included.",
        "expected": "GENUINE"
    },
    {
        "category": "Phishing - Bank Account",
        "type": "phishing",
        "text": "URGENT Your bank account has been locked Please confirm your password immediately to unlock your account",
        "expected": "PHISHING"
    },
    {
        "category": "Legitimate - Order Confirmation",
        "type": "phishing",
        "text": "Thank you for your purchase Your order has been confirmed and will ship within 2-3 business days",
        "expected": "LEGITIMATE"
    },
    {
        "category": "Phishing - PayPal",
        "type": "phishing",
        "text": "URGENT action required Your PayPal account will be closed in 24 hours if you do not verify your identity immediately",
        "expected": "PHISHING"
    },
    {
        "category": "Legitimate - Package Delivery",
        "type": "phishing",
        "text": "Your package is ready for pickup at the nearest location Please visit within 5 days",
        "expected": "LEGITIMATE"
    },
    {
        "category": "Phishing - Security Alert",
        "type": "phishing",
        "text": "Apple security alert Someone tried to access your account from an unknown location Verify it was you",
        "expected": "PHISHING"
    },
    {
        "category": "Legitimate - Flight Confirmation",
        "type": "phishing",
        "text": "Your flight booking confirmation number is attached Your flight departs tomorrow at 2pm",
        "expected": "LEGITIMATE"
    }
]

print()
correct = 0
total = len(test_cases)

for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*70}")
    print(f"TEST {i}: {test['category']}")
    print(f"{'='*70}")
    print(f"Type: {test['type'].upper()}")
    print(f"\nInput Text:")
    print(f"{test['text'][:100]}...")
    
    cleaned = clean_text(test['text'])
    vect_text = vectorizer.transform([cleaned])
    
    if test['type'] == 'job':
        result = job_model.predict(vect_text)[0]
        prob = job_model.predict_proba(vect_text)[0]
        prediction = "FRAUDULENT" if result == 1 else "GENUINE"
    else:
        result = phish_model.predict(vect_text)[0]
        prob = phish_model.predict_proba(vect_text)[0]
        prediction = "PHISHING" if result == 1 else "LEGITIMATE"
    
    confidence = max(prob) * 100
    
    print(f"\nExpected:  {test['expected']}")
    print(f"Predicted: {prediction}")
    print(f"Confidence: {confidence:.2f}%")
    
    is_correct = prediction == test['expected']
    status = "✅ CORRECT" if is_correct else "❌ INCORRECT"
    print(f"Result: {status}")
    
    if is_correct:
        correct += 1

print()
print("="*70)
print(f"OVERALL ACCURACY: {correct}/{total} ({correct*100/total:.1f}%)")
print("="*70)

if correct == total:
    print("✅ ALL TESTS PASSED - System is working perfectly!")
elif correct >= total * 0.8:
    print("✅ GOOD PERFORMANCE - System is working well (80%+ accuracy)")
else:
    print("⚠️ NEEDS IMPROVEMENT - Consider adding more training data")

print()
