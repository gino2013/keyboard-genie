@echo off
chcp 65001 >nul
title 鍵盤精靈 - Keyboard Genie

echo.
echo ========================================
echo          鍵盤精靈 - Keyboard Genie
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
if not exist "keyboard_genie.py" (
    echo.
    echo ❌ 錯誤：找不到 keyboard_genie.py 檔案！
    echo 請確保此批處理檔案與 keyboard_genie.py 在同一目錄下。
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
echo    • 請以管理員身分執行以確保在遊戲中正常工作
echo    • 程式運行時請勿移動或關閉此視窗
echo.
echo ========================================

pause

echo.
echo 🚀 正在啟動鍵盤精靈...
echo.

REM 啟動Python腳本
python keyboard_genie.py

REM 如果程式異常退出
echo.
echo 程式已結束。
echo.
pause