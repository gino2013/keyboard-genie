@echo off
chcp 65001 >nul 2>&1
title Build Valheim Keyboard Genie Executable

echo.
echo ========================================
echo   Build Valheim Keyboard Genie Executable  
echo ========================================
echo.
echo This script builds a working standalone .exe
echo that includes all necessary dependencies for Valheim.
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
if not exist "valheim_keyboard_genie.py" (
    echo.
    echo ❌ Error: valheim_keyboard_genie.py file not found!
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

REM Clean old build files
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
echo 🔨 Building Valheim Keyboard Genie executable...
echo This may take a few minutes, please wait...
echo.

REM Build with the working parameters
python -m PyInstaller --onefile --console --name "ValheimKeyboardGenie" --collect-all pynput --hidden-import=pynput --hidden-import=pynput.keyboard --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse --hidden-import=pynput.mouse._win32 valheim_keyboard_genie.py

if %errorlevel% neq 0 (
    echo ❌ Build failed!
    echo.
    echo Trying alternative method without some optimizations...
    python -m PyInstaller --onefile --name "ValheimKeyboardGenie-Simple" --collect-all pynput valheim_keyboard_genie.py
    
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
    set "exe_name=ValheimKeyboardGenie-Simple.exe"
) else (
    echo ✅ Build completed successfully!
    set "exe_name=ValheimKeyboardGenie.exe"
)

echo.
echo 📄 Copying documentation...
if exist "dist" (
    if exist "user-manual.txt" copy "user-manual.txt" "dist\" >nul
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
echo ✅ Optimized for Valheim gameplay automation
echo.
echo 📁 Ready to distribute files:
if exist "dist" dir /b "dist"
echo.
echo 🎮 Usage for Valheim:
echo   1. Copy the dist folder to target computer
echo   2. Double-click %exe_name%
echo   3. Press F1 to start, F2 to stop
echo   4. Run as Administrator for best Valheim compatibility
echo.
echo ⚠️ Important: Run as Administrator for best compatibility with Valheim
echo.

echo.
echo ========================================
echo      建置 Valheim 鍵盤精靈 執行檔
echo ========================================
echo.
echo 此腳本建置一個可獨立運行的 .exe 檔案
echo 包含所有 Valheim 自動化所需的依賴套件
echo.
echo ✅ 執行檔已創建: dist\%exe_name%
echo ✅ 此檔案可在任何 Windows 電腦上運行，無需安裝 Python
echo ✅ 所有依賴套件 (pynput 等) 已包含
echo ✅ 針對 Valheim 遊戲自動化優化
echo.
echo 🎮 Valheim 使用方法:
echo   1. 將 dist 資料夾複製到目標電腦
echo   2. 雙擊 %exe_name%
echo   3. 按 F1 開始，F2 停止
echo   4. 建議以管理員身分執行以獲得最佳 Valheim 相容性
echo.
echo ⚠️ 重要提醒：建議以管理員身分執行以獲得與 Valheim 的最佳相容性
echo.

pause