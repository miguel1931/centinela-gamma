@echo off
SETLOCAL EnableDelayedExpansion
SET PYTHONUTF8=1

echo ===================================================
echo   CENTINELA-GAMMA | AUTOMATED VIGILANCE SYSTEM
echo ===================================================
echo.

:: Check for Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python to continue.
    pause
    exit /b
)

:: Install requirements if needed
echo [1/4] Checking dependencies...
pip install -r requirements.txt -q

:: Step 1: Data Extraction
echo [2/4] Starting data extraction (centinela_gamma_maximized.py)...
cd src
python centinela_gamma_maximized.py
if %errorlevel% neq 0 (
    echo [WARNING] Extraction script exited with an error. Continuing to processing...
)

:: Step 2: Data Processing
echo [3/4] Processing metrics for dashboard (palestine_tweets_processor.py)...
python palestine_tweets_processor.py
if %errorlevel% neq 0 (
    echo [ERROR] Processing failed.
    cd ..
    pause
    exit /b
)

:: Step 3: Open Dashboard
echo [4/4] Opening dashboard...
cd ..
start "" "dashboard\palestine_war_crimes_dashboard_optimized.html"

echo.
echo ===================================================
echo   SYSTEM UPDATED SUCCESSFULLY
echo ===================================================
echo.
pause
