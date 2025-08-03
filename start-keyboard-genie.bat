@echo off
chcp 65001 >nul
title Keyboard Genie

echo.
echo ========================================
echo           Keyboard Genie
echo ========================================
echo.
echo Checking system environment...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python not found!
    echo.
    echo Please install Python first:
    echo 1. Go to https://www.python.org/downloads/
    echo 2. Download and install the latest Python version
    echo 3. Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version

REM Check and install dependencies
echo.
echo Checking dependencies...

python -c "import pynput" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 📦 Installing required package pynput...
    pip install pynput
    if %errorlevel% neq 0 (
        echo ❌ Package installation failed! Please check your internet connection.
        pause
        exit /b 1
    )
)

echo ✅ All dependencies are ready

REM Check if script file exists
if not exist "keyboard_genie.py" (
    echo.
    echo ❌ Error: keyboard_genie.py file not found!
    echo Please make sure this batch file is in the same directory as keyboard_genie.py
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo              Instructions
echo ========================================
echo.
echo 📍 Controls:
echo    F1 Key - Start automation
echo    F2 Key - Stop automation  
echo    Ctrl+C - Force quit program
echo.
echo 📍 Features:
echo    • Press keys 1-7 every 20 minutes (10 times each)
echo    • Click mouse every 2 minutes (twice)
echo    • Press key 8 every 240 minutes, then key 9 every 240 minutes
echo.
echo ⚠️  Important:
echo    • Run as Administrator for best game compatibility
echo    • Do not close this window while program is running
echo.
echo ========================================

pause

echo.
echo 🚀 Starting Keyboard Genie...
echo.

REM Start Python script
python keyboard_genie.py

REM If program exits unexpectedly
echo.
echo Program has ended.
echo.
pause