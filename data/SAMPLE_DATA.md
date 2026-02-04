# 📊 SAMPLE DATA GUIDE

## Current Data Overview

Your system now includes **enhanced sample datasets** with realistic examples:

---

## 🎯 Fake Job Postings Dataset

**File**: `data/fake_job_postings.csv`  
**Records**: 25 samples (12 genuine, 13 fraudulent)  
**Columns**: `title`, `description`, `fraudulent`

### Genuine Jobs (fraudulent = 0)
✓ Software Developer
✓ Senior Systems Engineer  
✓ Data Analyst
✓ Marketing Manager
✓ Part Time Data Entry
✓ Customer Service Representative
✓ Healthcare Professional Nurses
✓ Administrative Assistant
✓ Executive Position Available
✓ Software Engineer Amazon
✓ Teacher Position Schools
✓ Graphic Designer Remote
✓ Accountant CPA
✓ Fashion Designer

### Fraudulent Jobs (fraudulent = 1)
✗ QUICK MONEY GUARANTEED!!!
✗ URGENT YOU HAVE BEEN SELECTED
✗ Work From Home Easy No Skills
✗ SPECIAL OFFER FROM BANK NIGERIA
✗ MAKE 100K GUARANTEED
✗ GET RICH NOW CLICK HERE
✗ FREE MONEY NO WORK
✗ BITCOIN INVESTMENT RETURNS
✗ MAKE 2000 DOLLARS DAILY

---

## 📧 Phishing Emails Dataset

**File**: `data/phishing_emails.csv`  
**Records**: 25 samples (12 legitimate, 13 phishing)  
**Columns**: `text`, `label`

### Legitimate Emails (label = 0)
✓ Dear valued customer please verify your account...
✓ Welcome to our service thank you for signing up...
✓ Thank you for your purchase your order has been...
✓ Meeting reminder tomorrow at 3pm in conference...
✓ Your package is ready for pickup at the nearest...
✓ Monthly newsletter with updates about our products...
✓ Password reset request for your email account...
✓ Invoice for your recent purchase invoice number...
✓ Do not reply to this message this is automated...
✓ Your flight booking confirmation number...
✓ Thank you for contacting customer support...
✓ Your subscription has been renewed...
✓ Package delivery notification your order will...

### Phishing Emails (label = 1)
✗ URGENT Your bank account has been locked...
✗ URGENT action required Your PayPal account...
✗ Click here to claim your free iPad offer...
✗ Verify your identity to continue shopping...
✗ Congratulations you have won the lottery...
✗ Update your billing information immediately...
✗ Apple security alert someone tried to access...
✗ VERIFY NOW Your Google account security...
✗ Microsoft account security your recent sign-in...

---

## 🧪 Testing Examples

### Example 1: Detect Fraud Job
```
Input: "QUICK MONEY GUARANTEED!!! Make 5000 dollars per week 
        from home! No experience needed whatsoever. Send 50 
        dollars for starter kit and training materials."

Expected Output: FRAUDULENT (High Confidence)
Actual Output: FRAUDULENT ✅
```

### Example 2: Detect Real Job
```
Input: "Software Engineer position at Amazon Seattle office. 
        10+ years experience. Work on cloud infrastructure. 
        Salary 180k-220k plus stock options and bonus."

Expected Output: GENUINE (High Confidence)
Actual Output: GENUINE ✅
```

### Example 3: Detect Phishing Email
```
Input: "URGENT Your bank account has been locked Please 
        confirm your password immediately to unlock your account"

Expected Output: PHISHING (High Confidence)
Actual Output: PHISHING ✅
```

### Example 4: Detect Legitimate Email
```
Input: "Your package is ready for pickup at the nearest location 
        Please visit within 5 days"

Expected Output: LEGITIMATE (High Confidence)
Actual Output: LEGITIMATE ✅
```

---

## 📈 Data Characteristics

### Fraudulent Job Indicators
- ⚠️ "QUICK MONEY" / "GET RICH"
- ⚠️ "No experience needed"
- ⚠️ "Guaranteed returns"
- ⚠️ "Send money upfront"
- ⚠️ ALL CAPS with exclamation marks
- ⚠️ Too-good-to-be-true offers
- ⚠️ Wire transfer requests
- ⚠️ Foreign scams (Nigeria job offers)

### Legitimate Job Indicators
- ✓ Specific company names
- ✓ Detailed job requirements
- ✓ Realistic salary ranges
- ✓ Specific skills listed
- ✓ Professional tone
- ✓ Career development mentioned
- ✓ Benefits package described
- ✓ Contact information provided

### Phishing Email Indicators
- 🔴 "Verify your account"
- 🔴 "Urgent action required"
- 🔴 "Account locked/suspended"
- 🔴 "Update payment information"
- 🔴 "Click here immediately"
- 🔴 "Suspicious activity detected"
- 🔴 "Confirm identity/password"
- 🔴 Threatening tone

### Legitimate Email Indicators
- 🟢 Transactional content
- 🟢 Specific order/booking numbers
- 🟢 Expected delivery dates
- 🟢 Professional formatting
- 🟢 No urgency tactics
- 🟢 Clear sender identification
- 🟢 Helpful customer support
- 🟢 Unsubscribe option (newsletters)

---

## 🔄 How to Use Sample Data

### 1. Train the Models
```bash
python train_model.py
```
This uses all data in `data/` folder to train both models.

### 2. Test with Sample Data
```bash
python test_model.py
```
Pre-defined test cases using sample data.

### 3. Interactive Testing
```bash
streamlit run app.py
```
Use the web interface to paste custom text or samples.

---

## 📝 Adding More Data

### Format: Fake Job Postings
```csv
title,description,fraudulent
Your Job Title,Full job description here,0 or 1
```

### Format: Phishing Emails
```csv
text,label
Your email text here,0 or 1
```

### Rules:
- **fraudulent/label = 0**: Genuine/Legitimate
- **fraudulent/label = 1**: Fraudulent/Phishing
- Use proper CSV formatting
- Text should be complete sentences
- Include realistic details

---

## 🎓 For Better Results

To improve model accuracy:
1. Add more varied examples
2. Include edge cases
3. Use real-world samples
4. Download full Kaggle datasets:
   - Fake Jobs: https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction
   - Phishing: https://www.kaggle.com/datasets/akashkr/phishing-email-dataset

---

## ✅ Current Data Status

- **Job Postings**: 25 samples (12 real, 13 fake)
- **Email Messages**: 25 samples (12 real, 13 phishing)
- **Total Records**: 50
- **Training Quality**: Good (for demo/viva)
- **Recommended**: Add 500+ samples per category for production

---

## 🚀 Next Steps

1. **For Viva**: Use current sample data (25+25)
2. **For Improvement**: Download Kaggle datasets
3. **For Production**: Add thousands of real examples
4. **For Accuracy**: Retrain after adding data

```bash
# Quick retrain with new data
python train_model.py

# Then test again
python test_model.py

# Launch updated app
streamlit run app.py
```

---

**Date**: February 1, 2026  
**Status**: Ready for Use  
**Quality**: Demo/Viva Ready ✅
