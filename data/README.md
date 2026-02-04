# Dataset Instructions

## 📥 Download Required Datasets

You need to download two datasets from Kaggle and place them in this folder.

### 1. Fake Job Posting Dataset
- **Link:** https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction
- **File to download:** `fake_job_postings.csv`
- **Place it here as:** `data/fake_job_postings.csv`
- **Size:** ~3 MB
- **Records:** ~18,000 job postings

### 2. Phishing Email Dataset
- **Link:** https://www.kaggle.com/datasets/akashkr/phishing-email-dataset
- **File to download:** `phishing_emails.csv` or similar
- **Place it here as:** `data/phishing_emails.csv`
- **Note:** The dataset might be named differently - rename it to `phishing_emails.csv`

## 🔑 Kaggle Account Required

If you don't have a Kaggle account:
1. Go to https://www.kaggle.com
2. Sign up for free
3. Download the datasets

## ✅ Verification

After downloading, this folder should contain:
- `fake_job_postings.csv`
- `phishing_emails.csv`
- `README.md` (this file)

Then you can run:
```bash
python train_model.py
```
