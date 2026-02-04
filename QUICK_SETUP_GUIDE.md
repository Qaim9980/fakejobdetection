# 🚀 Quick Setup Guide for New Laptop

## Automatic Setup (Recommended)

### Prerequisites
1. **Git** - Download from: https://git-scm.com/download/win
2. **Python 3.8+** - Download from: https://www.python.org/downloads/

### One-Click Setup

1. Download the setup file:
   ```
   https://raw.githubusercontent.com/Qaim9980/fakejobdetection/main/SETUP_NEW_LAPTOP.bat
   ```

2. Right-click and select "Run as Administrator"

3. Follow the on-screen instructions

The script will automatically:
- ✅ Clone the repository
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Download NLTK data
- ✅ Verify setup
- ✅ Launch the application

---

## Manual Setup

If you prefer manual installation:

### Step 1: Clone Repository
```bash
git clone https://github.com/Qaim9980/fakejobdetection.git
cd fakejobdetection
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
python download_nltk_data.py
```

### Step 4: Run Application
```bash
streamlit run app.py
```

---

## Training Models (Optional)

If model files are missing, you need to train them:

### Step 1: Download Datasets

Download these datasets from Kaggle:
- [Fake Job Postings](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)
- [Phishing Emails](https://www.kaggle.com/datasets/akashkr/phishing-email-dataset)

### Step 2: Place Datasets
- Place `fake_job_postings.csv` in `data/` folder
- Place `Phishing_Email.csv` in `data/` folder

### Step 3: Train Models
```bash
python train_model.py
```
OR
```bash
train_model.bat
```

---

## Troubleshooting

### Git Not Found
```bash
# Install Git from: https://git-scm.com/download/win
```

### Python Not Found
```bash
# Install Python from: https://www.python.org/downloads/
# Make sure to check "Add Python to PATH" during installation
```

### Model Files Missing
```bash
# Download datasets and run:
python train_model.py
```

### Port Already in Use
```bash
# Run app on different port:
streamlit run app.py --server.port 8502
```

---

## File Structure After Setup

```
fakejobdetection/
│
├── .venv/                      (Virtual environment)
├── data/
│   ├── fake_job_postings.csv  (Download from Kaggle)
│   └── Phishing_Email.csv     (Download from Kaggle)
│
├── model/
│   ├── job_model.pkl          (Generated after training)
│   ├── phishing_model.pkl     (Generated after training)
│   └── vectorizer.pkl         (Generated after training)
│
├── app.py                      (Main application)
├── train_model.py             (Model training script)
├── requirements.txt           (Dependencies)
├── RUN_ME.bat                 (Quick launcher)
└── SETUP_NEW_LAPTOP.bat       (This setup script)
```

---

## Quick Commands Reference

| Action | Command |
|--------|---------|
| Run App | `streamlit run app.py` |
| Train Models | `python train_model.py` |
| Install Packages | `pip install -r requirements.txt` |
| Update Code | `git pull` |
| Check Python | `python --version` |
| Check Git | `git --version` |

---

## Support

For issues or questions:
- Check [README.md](README.md) for detailed documentation
- Review [ERROR_RESOLUTION.md](ERROR_RESOLUTION.md) for common issues
- GitHub: https://github.com/Qaim9980/fakejobdetection

---

**Happy Detecting! 🛡️**
