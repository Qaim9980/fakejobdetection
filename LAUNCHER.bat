@echo off
setlocal enabledelayedexpansion
title Job Fraud Detection System - Launcher
color 0A
cls

:start
echo.
echo ============================================================
echo   JOB FRAUD DETECTION SYSTEM v1.0
echo   Production-Ready Launcher
echo ============================================================
echo.
echo Choose an option:
echo.
echo   1 - Run System Diagnostics (CHECK SETUP)
echo   2 - Train Models (RE-TRAIN ON DATA)
echo   3 - Launch Web Application (START APP)
echo   4 - Run Tests (VERIFY MODELS)
echo   5 - Open Model Folder
echo   6 - Exit
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto diagnose
if "%choice%"=="2" goto train
if "%choice%"=="3" goto app
if "%choice%"=="4" goto test
if "%choice%"=="5" goto explore
if "%choice%"=="6" goto end

echo Invalid choice. Please try again.
timeout /t 2 /nobreak
goto start

:diagnose
echo.
echo Running diagnostics...
echo.
cd /d E:\fakejobdetection
E:\fakejobdetection\.venv\Scripts\python.exe diagnose.py
pause
goto start

:train
echo.
echo Training models (this may take a moment)...
echo.
cd /d E:\fakejobdetection
E:\fakejobdetection\.venv\Scripts\python.exe train_model.py
echo.
pause
goto start

:app
echo.
echo Starting web application...
echo.
echo * URL: http://localhost:8501
echo * Press Ctrl+C to stop
echo.
cd /d E:\fakejobdetection
E:\fakejobdetection\.venv\Scripts\streamlit.exe run app.py --logger.level=error
goto start

:test
echo.
echo Running model tests...
echo.
cd /d E:\fakejobdetection
E:\fakejobdetection\.venv\Scripts\python.exe test_model.py
pause
goto start

:explore
explorer E:\fakejobdetection\model
goto start

:end
echo.
echo Goodbye!
echo.
exit /b 0
