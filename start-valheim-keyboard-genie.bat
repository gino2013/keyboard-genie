@echo off
chcp 65001 >nul 2>&1
title Valheim Keyboard Genie

echo.
echo ========================================
echo        Valheim Keyboard Genie
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
if not exist "valheim_keyboard_genie.py" (
    echo.
    echo ❌ Error: valheim_keyboard_genie.py file not found!
    echo Please make sure this batch file is in the same directory as valheim_keyboard_genie.py
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
echo    • Run as Administrator for best Valheim compatibility
echo    • Do not close this window while program is running
echo.
echo ========================================

pause

echo.
echo 🚀 Starting Valheim Keyboard Genie...
echo.

REM Start Python script
python valheim_keyboard_genie.py

REM If program exits unexpectedly
echo.
echo Program has ended.
echo.
pause

REM Chinese version below
echo.
echo ========================================
echo           Valheim 鍵盤精靈
echo ========================================
echo.
echo 正在檢查系統環境...
echo.

REM 檢查Python是否已安裝
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤：未找到Python！
    echo.
    echo 請先安裝Python：
    echo 1. 前往 https://www.python.org/downloads/
    echo 2. 下載並安裝最新版本的Python
    echo 3. 安裝時請勾選 "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo ✅ Python 已安裝
python --version

REM 檢查並安裝依賴套件
echo.
echo 正在檢查依賴套件...

python -c "import pynput" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 📦 正在安裝必要的套件 pynput...
    pip install pynput
    if %errorlevel% neq 0 (
        echo ❌ 套件安裝失敗！請檢查網路連接。
        pause
        exit /b 1
    )
)

echo ✅ 所有依賴套件已就緒

REM 檢查腳本文件是否存在
if not exist "valheim_keyboard_genie.py" (
    echo.
    echo ❌ 錯誤：找不到 valheim_keyboard_genie.py 檔案！
    echo 請確保此批處理檔案與 valheim_keyboard_genie.py 在同一目錄下。
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo              使用說明
echo ========================================
echo.
echo 📍 操作說明：
echo    F1 鍵 - 開始自動化
echo    F2 鍵 - 停止自動化  
echo    Ctrl+C - 強制結束程式
echo.
echo 📍 功能說明：
echo    • 每20分鐘按1-7鍵輪換（每個鍵按10次）
echo    • 每2分鐘點擊滑鼠左鍵兩次
echo    • 每240分鐘（4小時）按鍵8，再240分鐘按鍵9
echo.
echo ⚠️  重要提醒：
echo    • 請以管理員身分執行以確保在Valheim中正常工作
echo    • 程式運行時請勿移動或關閉此視窗
echo.
echo ========================================

pause

echo.
echo 🚀 正在啟動 Valheim 鍵盤精靈...
echo.

REM 啟動Python腳本
python valheim_keyboard_genie.py

REM 如果程式異常退出
echo.
echo 程式已結束。
echo.
pause