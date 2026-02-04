"""
Complete error handling and troubleshooting guide for the app
"""

import os
import sys

def diagnose_system():
    """Diagnose system setup"""
    print("="*70)
    print("SYSTEM DIAGNOSTICS")
    print("="*70)
    
    issues = []
    
    # Check Python
    print(f"\n✓ Python: {sys.version}")
    
    # Check venv
    if os.path.exists(".venv"):
        print("✓ Virtual Environment: Present")
    else:
        issues.append("Virtual environment not found")
    
    # Check data files
    print("\nData Files:")
    data_files = {
        "data/fake_job_postings.csv": "Fake Job Postings Dataset",
        "data/phishing_emails.csv": "Phishing Emails Dataset"
    }
    
    for path, name in data_files.items():
        if os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  ✓ {name} ({size} bytes)")
        else:
            print(f"  ✗ {name} - NOT FOUND")
            issues.append(f"Missing: {path}")
    
    # Check model files
    print("\nModel Files:")
    model_files = {
        "model/job_model.pkl": "Job Fraud Model",
        "model/phishing_model.pkl": "Phishing Detection Model",
        "model/vectorizer.pkl": "TF-IDF Vectorizer"
    }
    
    for path, name in model_files.items():
        if os.path.exists(path):
            size = os.path.getsize(path) / 1024  # KB
            print(f"  ✓ {name} ({size:.2f} KB)")
        else:
            print(f"  ✗ {name} - NOT FOUND")
            issues.append(f"Missing: {path}")
    
    # Check Python packages
    print("\nPython Packages:")
    packages = ['pandas', 'numpy', 'sklearn', 'nltk', 'streamlit', 'joblib']
    for pkg in packages:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg}")
        except ImportError:
            print(f"  ✗ {pkg}")
            issues.append(f"Missing package: {pkg}")
    
    # Summary
    print("\n" + "="*70)
    if issues:
        print("⚠️  ISSUES FOUND:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        return False
    else:
        print("✅ ALL SYSTEMS READY!")
        return True

if __name__ == "__main__":
    success = diagnose_system()
    sys.exit(0 if success else 1)
