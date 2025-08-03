@echo off
chcp 65001 >nul 2>&1
title Build Keyboard Genie Executable - FINAL VERSION

echo.
echo ========================================
echo    Build Keyboard Genie Executable  
echo            FINAL VERSION
echo ========================================
echo.
echo This script builds a working standalone .exe
echo that includes all necessary dependencies.
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python not found!
    echo Please install Python first.
    pause
    exit /b 1
)

echo ✅ Python is installed
python --version

REM Check if script file exists
if not exist "keyboard_genie.py" (
    echo.
    echo ❌ Error: keyboard_genie.py file not found!
    echo Please run this script in the project directory.
    pause
    exit /b 1
)

REM Install/check pynput first
echo.
echo 📦 Installing/checking pynput...
pip install pynput==1.7.6
if %errorlevel% neq 0 (
    echo ❌ Failed to install pynput!
    pause
    exit /b 1
)

REM Check if PyInstaller is available and install if needed
python -m PyInstaller --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 📦 Installing PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo ❌ PyInstaller installation failed!
        pause
        exit /b 1
    )
)

echo ✅ PyInstaller is available

REM Clean old build files (try different methods)
echo.
echo 🧹 Cleaning old build files...
if exist "dist" (
    rmdir /s /q dist 2>nul
    rd /s /q dist 2>nul
    if exist "dist" (
        echo ⚠️ Warning: Could not remove old dist directory
        echo Please close any programs using files in dist folder
    )
)
if exist "build" (
    rmdir /s /q build 2>nul
    rd /s /q build 2>nul
)
if exist "*.spec" del /q *.spec 2>nul

echo.
echo 🔨 Building executable with comprehensive pynput support...
echo This may take a few minutes, please wait...
echo.

REM Build with the working parameters
python -m PyInstaller --onefile --console --name "KeyboardGenie" --collect-all pynput --hidden-import=pynput --hidden-import=pynput.keyboard --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse --hidden-import=pynput.mouse._win32 keyboard_genie.py

if %errorlevel% neq 0 (
    echo ❌ Build failed!
    echo.
    echo Trying alternative method without some optimizations...
    python -m PyInstaller --onefile --name "KeyboardGenie-Simple" --collect-all pynput keyboard_genie.py
    
    if %errorlevel% neq 0 (
        echo ❌ Alternative build also failed!
        echo.
        echo Please check:
        echo 1. All files are in the correct directory
        echo 2. No antivirus software is blocking the build
        echo 3. You have write permissions in this directory
        pause
        exit /b 1
    )
    
    echo ✅ Alternative build completed!
    set "exe_name=KeyboardGenie-Simple.exe"
) else (
    echo ✅ Build completed successfully!
    set "exe_name=KeyboardGenie.exe"
)

echo.
echo 📄 Copying documentation...
if exist "dist" (
    if exist "使用說明.txt" copy "使用說明.txt" "dist\" >nul
    if exist "README.md" copy "README.md" "dist\" >nul
    echo Documentation files copied to dist directory
)

echo.
echo ========================================
echo           BUILD COMPLETED!
echo ========================================
echo.
echo ✅ Executable created: dist\%exe_name%
echo ✅ This file works on any Windows computer without Python
echo ✅ All dependencies (pynput, etc.) are included
echo.
echo 📁 Ready to distribute files:
if exist "dist" dir /b "dist"
echo.
echo 🎮 Usage:
echo   1. Copy the dist folder to target computer
echo   2. Double-click %exe_name%
echo   3. Press F1 to start, F2 to stop
echo.
echo ⚠️ Important: Run as Administrator for best compatibility
echo.
pause