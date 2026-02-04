@echo off
title Job Fraud Detection System - START HERE
color 0A
cls

echo.
echo ============================================================
echo   JOB FRAUD DETECTION SYSTEM - QUICK START
echo ============================================================
echo.
echo Step 1: Checking system setup...
echo.

cd /d E:\fakejobdetection

REM Check if venv exists
if not exist ".venv" (
    echo ERROR: Virtual environment not found!
    echo Please run setup.py first
    pause
    exit /b 1
)

echo [OK] Virtual environment found
echo.

REM Check if model files exist
if not exist "model\job_model.pkl" (
    echo WARNING: Model files not found
    echo Running training...
    call train_model.bat
)

echo [OK] All checks passed
echo.
echo ============================================================
echo Step 2: Starting Web Application...
echo ============================================================
echo.
echo * Opening: http://localhost:8501
echo * Database: models/data loaded
echo * Status: READY
echo.
echo Press Ctrl+C to stop the server
echo.

E:\fakejobdetection\.venv\Scripts\streamlit.exe run app.py --logger.level=error

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to start application
    echo Please check the error messages above
    pause
    exit /b 1
)

pause
