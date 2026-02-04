@echo off
cls
echo ============================================================
echo Starting Streamlit Web Application...
echo ============================================================
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.
echo ============================================================
cd /d E:\fakejobdetection
E:\fakejobdetection\.venv\Scripts\streamlit.exe run app.py --logger.level=error
pause
