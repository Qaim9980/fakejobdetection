# 🛡 Intelligent Job Fraud & Phishing Detection System

A machine learning-based system that detects fake job postings and phishing messages using NLP and Naive Bayes classification.

## 📁 Project Structure

```
fakejobdetection/
│
├── data/
│   ├── fake_job_postings.csv    (download from Kaggle)
│   └── phishing_emails.csv      (download from Kaggle)
│
├── model/
│   ├── job_model.pkl            (generated after training)
│   ├── phishing_model.pkl       (generated after training)
│   └── vectorizer.pkl           (generated after training)
│
├── train_model.py
├── app.py
├── requirements.txt
└── README.md
```

## 📊 Datasets

### Fake Job Posting Dataset
**Kaggle:** https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction
- Download and place as `data/fake_job_postings.csv`
- Target column: `fraudulent` (0 = Genuine, 1 = Fake)

### Phishing Email Dataset
**Kaggle:** https://www.kaggle.com/datasets/akashkr/phishing-email-dataset
- Download and place as `data/phishing_emails.csv`
- Target column: `label` (0 = Safe, 1 = Phishing)

## 🚀 Installation & Setup

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Download Datasets
1. Download both datasets from the Kaggle links above
2. Place them in the `data/` folder with the exact names shown above

### Step 3: Train Models
```bash
python train_model.py
```
This will create three files in the `model/` folder:
- `job_model.pkl`
- `phishing_model.pkl`
- `vectorizer.pkl`

### Step 4: Run the Application
```bash
streamlit run app.py
```

The web application will open in your browser at `http://localhost:8501`

## 🎯 How to Use

1. Select detection type (Fake Job Detection or Phishing Message Detection)
2. Paste the job posting or email text
3. Click "Analyze"
4. View the results with confidence score

## 🧠 Technical Details

**NLP Techniques:**
- Text preprocessing (lowercasing, removing special characters)
- Stopword removal
- TF-IDF vectorization (5000 features)

**Machine Learning:**
- Algorithm: Multinomial Naive Bayes
- Two separate models for job fraud and phishing detection
- Shared vectorizer for consistent text processing

## 📝 Viva Explanation

> "This system uses NLP and machine learning to analyze textual patterns in job postings and emails. TF-IDF converts text into numerical features, and Naive Bayes classifies content as genuine or fraudulent with confidence scores. The system works offline and provides real-time scam detection."

## 🎓 Project Features

✅ Offline ML model  
✅ Real-time detection  
✅ Confidence scoring  
✅ User-friendly GUI  
✅ Dual detection capability (jobs + phishing)  
✅ Production-ready code  

---

**Developed for BS Level Final Year Project**
