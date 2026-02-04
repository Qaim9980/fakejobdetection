@echo off
TITLE Fraud Detection System - New Laptop Setup
color 0A

echo ============================================
echo  FRAUD DETECTION SYSTEM - AUTO SETUP
echo ============================================
echo.
echo This script will:
echo  1. Clone the GitHub repository
echo  2. Install Python dependencies
echo  3. Download required NLTK data
echo  4. Verify model files
echo  5. Launch the application
echo.
echo ============================================
pause

:: Check if Git is installed
echo.
echo [Step 1/5] Checking Git installation...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)
echo Git found!

:: Check if Python is installed
echo.
echo [Step 2/5] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo Please install Python from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo Python found!

:: Clone Repository
echo.
echo [Step 3/5] Cloning repository from GitHub...
set REPO_URL=https://github.com/Qaim9980/fakejobdetection.git
set FOLDER_NAME=fakejobdetection

if exist %FOLDER_NAME% (
    echo Folder already exists. Pulling latest changes...
    cd %FOLDER_NAME%
    git pull
) else (
    echo Cloning repository...
    git clone %REPO_URL%
    cd %FOLDER_NAME%
)

echo Repository ready!

:: Create virtual environment
echo.
echo [Step 4/5] Creating virtual environment...
if not exist .venv (
    python -m venv .venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists!
)

:: Activate virtual environment
echo.
echo Activating virtual environment...
call .venv\Scripts\activate.bat

:: Install dependencies
echo.
echo [Step 5/5] Installing Python packages...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Installing NLTK data...
python download_nltk_data.py

:: Check if models exist
echo.
echo Checking model files...
if not exist "model\job_model.pkl" (
    echo.
    echo WARNING: Model files not found!
    echo You need to train the models first.
    echo.
    echo Please:
    echo  1. Download datasets from Kaggle (see README.md)
    echo  2. Place them in the data\ folder
    echo  3. Run: train_model.bat
    echo.
    pause
) else (
    echo Model files found!
)

:: Setup complete
echo.
echo ============================================
echo  SETUP COMPLETE!
echo ============================================
echo.
echo To run the application:
echo  1. Double-click RUN_ME.bat
echo  OR
echo  2. Run: streamlit run app.py
echo.
echo Project location: %CD%
echo ============================================
pause

:: Ask if user wants to launch now
echo.
set /p LAUNCH="Do you want to launch the app now? (Y/N): "
if /i "%LAUNCH%"=="Y" (
    echo.
    echo Launching application...
    streamlit run app.py
)

exit /b 0
