@echo off
echo ============================================================
echo Job Fraud Detection System - Quick Start
echo ============================================================
echo.

echo Step 1: Running Setup Check...
E:\fakejobdetection\.venv\Scripts\python.exe setup.py
echo.

echo ============================================================
echo Next Steps:
echo ============================================================
echo.
echo 1. If datasets are missing, download them from:
echo    - Fake Jobs: https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction
echo    - Phishing: https://www.kaggle.com/datasets/akashkr/phishing-email-dataset
echo.
echo 2. Then run: train_model.bat
echo 3. Then run: run_app.bat
echo.
pause
