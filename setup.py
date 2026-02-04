"""
Complete Setup Script for Job Fraud Detection System
Run this script to verify all dependencies and setup
"""
import sys
import os

def check_dependencies():
    """Check if all required packages are installed"""
    print("=" * 60)
    print("Checking Dependencies...")
    print("=" * 60)
    
    required_packages = {
        'pandas': 'pandas',
        'numpy': 'numpy',
        'sklearn': 'scikit-learn',
        'nltk': 'nltk',
        'streamlit': 'streamlit',
        'joblib': 'joblib'
    }
    
    missing = []
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✅ {package_name} - Installed")
        except ImportError:
            print(f"❌ {package_name} - Missing")
            missing.append(package_name)
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("Run: pip install " + " ".join(missing))
        return False
    return True

def check_nltk_data():
    """Download required NLTK data"""
    print("\n" + "=" * 60)
    print("Downloading NLTK Data...")
    print("=" * 60)
    
    try:
        import nltk
        nltk.download('stopwords', quiet=True)
        print("✅ NLTK stopwords - Downloaded")
        return True
    except Exception as e:
        print(f"❌ NLTK data download failed: {e}")
        return False

def check_directories():
    """Verify project structure"""
    print("\n" + "=" * 60)
    print("Checking Project Structure...")
    print("=" * 60)
    
    required_dirs = ['data', 'model']
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✅ {dir_name}/ - Exists")
        else:
            os.makedirs(dir_name, exist_ok=True)
            print(f"✅ {dir_name}/ - Created")

def check_datasets():
    """Check if datasets are downloaded"""
    print("\n" + "=" * 60)
    print("Checking Datasets...")
    print("=" * 60)
    
    datasets = {
        'data/fake_job_postings.csv': 'Fake Job Postings Dataset',
        'data/phishing_emails.csv': 'Phishing Emails Dataset'
    }
    
    all_present = True
    for path, name in datasets.items():
        if os.path.exists(path):
            size = os.path.getsize(path) / (1024 * 1024)  # MB
            print(f"✅ {name} - Found ({size:.2f} MB)")
        else:
            print(f"❌ {name} - Not found")
            print(f"   Download from Kaggle and place at: {path}")
            all_present = False
    
    return all_present

def main():
    """Main setup function"""
    print("\n" + "🛡" * 30)
    print("Job Fraud & Phishing Detection System - Setup")
    print("🛡" * 30 + "\n")
    
    # Check all components
    deps_ok = check_dependencies()
    nltk_ok = check_nltk_data()
    check_directories()
    data_ok = check_datasets()
    
    # Final status
    print("\n" + "=" * 60)
    print("Setup Summary")
    print("=" * 60)
    
    if deps_ok and nltk_ok and data_ok:
        print("✅ All requirements met!")
        print("\n🚀 Ready to run:")
        print("   1. Train models: python train_model.py")
        print("   2. Run app: streamlit run app.py")
    elif deps_ok and nltk_ok:
        print("⚠️  Dependencies ready, but datasets missing!")
        print("\n📥 Next steps:")
        print("   1. Download datasets (see data/README.md)")
        print("   2. Run: python train_model.py")
        print("   3. Run: streamlit run app.py")
    else:
        print("❌ Setup incomplete. Please resolve the issues above.")

if __name__ == "__main__":
    main()
