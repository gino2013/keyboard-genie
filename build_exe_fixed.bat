@echo off
chcp 65001 >nul 2>&1
title Build Keyboard Genie Executable

echo.
echo ========================================
echo      Build Keyboard Genie Executable
echo ========================================
echo.
echo This script will build a standalone .exe file
echo Users will not need to install Python to use it
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found!
    echo Please install Python first.
    pause
    exit /b 1
)

echo Python is installed
python --version

REM Check if PyInstaller is available and install if needed
python -m PyInstaller --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo Installing PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo PyInstaller installation failed!
        pause
        exit /b 1
    )
)

echo PyInstaller is available

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

REM Clean old build files
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build
if exist "*.spec" del /q *.spec

echo.
echo Starting build process...
echo This may take a few minutes, please wait...
echo.

REM Build using PyInstaller with Python module syntax for better compatibility
python -m PyInstaller --onefile --windowed --name "KeyboardGenie" --hidden-import=pynput --hidden-import=pynput.keyboard --hidden-import=pynput.mouse keyboard_genie.py

if %errorlevel% neq 0 (
    echo Build failed!
    echo.
    echo Trying alternative build method...
    
    REM Alternative method without --windowed (shows console)
    python -m PyInstaller --onefile --name "KeyboardGenie" --hidden-import=pynput --hidden-import=pynput.keyboard --hidden-import=pynput.mouse keyboard_genie.py
    
    if %errorlevel% neq 0 (
        echo Alternative build also failed!
        pause
        exit /b 1
    )
)

echo.
echo Build completed successfully!
echo.
echo Executable location: dist\KeyboardGenie.exe
echo.
echo You can now copy dist\KeyboardGenie.exe to any Windows computer
echo and use it without installing Python or other dependencies.
echo.

REM Copy documentation to dist directory
if exist "dist" (
    if exist "使用說明.txt" copy "使用說明.txt" "dist\"
    if exist "README.md" copy "README.md" "dist\"
    echo Documentation files copied to dist directory
)

echo.
echo Build process completed!
pause