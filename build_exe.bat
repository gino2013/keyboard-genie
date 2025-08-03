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

REM 檢查Python是否已安裝
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 錯誤：未找到Python！
    echo 請先安裝Python後再執行此腳本。
    pause
    exit /b 1
)

echo ✅ Python 已安裝

REM 檢查PyInstaller是否已安裝
python -c "import PyInstaller" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo 📦 正在安裝 PyInstaller...
    pip install pyinstaller
    if %errorlevel% neq 0 (
        echo ❌ PyInstaller 安裝失敗！
        pause
        exit /b 1
    )
)

echo ✅ PyInstaller 已安裝

REM 檢查依賴套件
echo.
echo 📦 正在安裝依賴套件...
pip install -r requirements.txt

REM 清理舊的建置檔案
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build
if exist "*.spec" del /q *.spec

echo.
echo 🔨 開始建置執行檔...
echo 這可能需要幾分鐘時間，請耐心等待...
echo.

REM 使用PyInstaller建置
pyinstaller --onefile ^
            --windowed ^
            --name "鍵盤精靈" ^
            --icon=keyboard.ico ^
            --add-data "README.md;." ^
            --hidden-import=pynput ^
            --hidden-import=pynput.keyboard ^
            --hidden-import=pynput.mouse ^
            keyboard_genie.py

if %errorlevel% neq 0 (
    echo ❌ 建置失敗！
    pause
    exit /b 1
)

echo.
echo ✅ 建置完成！
echo.
echo 執行檔位置：dist\鍵盤精靈.exe
echo.
echo 您現在可以將 dist\鍵盤精靈.exe 檔案
echo 複製到任何 Windows 電腦上使用，
echo 無需安裝 Python 或其他依賴套件。
echo.

REM 複製說明檔案到dist目錄
if exist "dist" (
    copy "使用說明.txt" "dist\"
    copy "README.md" "dist\"
    echo 📄 說明檔案已複製到 dist 目錄
)

echo.
pause