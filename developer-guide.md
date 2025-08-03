# Valheim Keyboard Genie - Developer Guide

## For Different User Groups

### 1. 🚀 Regular Users (Recommended)

**Using Batch Files (.bat)**

#### For English Users:
```
Double-click: start-valheim-keyboard-genie.bat
```

**Advantages:**
- Automatic dependency checking and installation
- User-friendly interface
- Automatic error handling
- Complete usage instructions included

**Requirements:**
- Windows system
- Python 3.6+ installed

---

### 2. 🎯 Complete Non-Technical Users

**Using Standalone Executable (.exe)**

#### Build Steps:
1. Run `build-valheim-keyboard-genie.bat`
2. Wait for build completion
3. Distribute `dist/ValheimKeyboardGenie.exe`

**Advantages:**
- No Python installation required
- Complete standalone operation
- One-click execution

**Requirements:**
- Windows system only

---

### 3. 🛠️ Developers/Advanced Users

**Direct Python Script Execution**

```bash
pip install -r requirements.txt
python valheim_keyboard_genie.py
```

---

## File Structure

```
valheim-keyboard-genie/
├── valheim_keyboard_genie.py          # Main program
├── requirements.txt                   # Python dependencies
├── start-valheim-keyboard-genie.bat   # English batch file
├── build-valheim-keyboard-genie.bat   # Build executable script
├── user-manual.txt                    # User manual file
├── developer-guide.md                 # This file
└── README.md                         # Project description
```

---

## Distribution Recommendations

### For Regular Users:
Provide these files:
- `valheim_keyboard_genie.py`
- `requirements.txt`
- `start-valheim-keyboard-genie.bat`
- `user-manual.txt`

### For Complete Non-Technical Users:
Provide these files:
- `dist/ValheimKeyboardGenie.exe`
- `user-manual.txt`

---

## Building Standalone Executable Details

### Automatic Build (Recommended):
```batch
Double-click: build-valheim-keyboard-genie.bat
```

### Manual Build:
```bash
# Install PyInstaller
pip install pyinstaller

# Build single executable file
pyinstaller --onefile --console --name "ValheimKeyboardGenie" valheim_keyboard_genie.py

# Output file located at: dist/ValheimKeyboardGenie.exe
```

### PyInstaller Parameter Explanation:
- `--onefile`: Package into single executable
- `--console`: Show console window for user feedback
- `--name`: Specify executable name
- `--collect-all`: Comprehensively collect module dependencies

---

## Common Problem Solutions

### Q: Batch file won't execute
A: 
1. Check if Python is correctly installed
2. Ensure files are in the same directory
3. Run as administrator

### Q: Executable build fails
A:
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Ensure PyInstaller is installed: `pip install pyinstaller`
3. Check if antivirus software is interfering

### Q: Executable file too large
A:
- Use `--exclude-module` to exclude unnecessary modules
- Consider using UPX compression (requires additional installation)

---

## Advanced Customization

### Custom Icon:
1. Prepare `.ico` format icon file
2. Modify `build-valheim-keyboard-genie.bat` with `--icon` parameter

### Add Extra Files:
Use `--add-data` parameter:
```bash
--add-data "config.txt;."
```

### Hide Console Window:
- Use `--windowed` parameter (included in build script)
- Or modify program to GUI version

---

## Testing Recommendations

### Batch File Testing:
1. Test on clean Windows system
2. Test with/without Python environment
3. Test normal/abnormal network connection scenarios

### Executable Testing:
1. Test on systems without Python
2. Test different Windows versions
3. Check file size and startup speed

---

## Version Update Process

1. Update `valheim_keyboard_genie.py`
2. Test functionality is normal
3. Update version number and documentation files
4. Rebuild executable
5. Update distribution files

---

# Valheim 鍵盤精靈 - 開發者指南

## 為不同用戶群體提供的執行方案

### 1. 🚀 一般用戶（推薦）

**使用批處理檔案（.bat）**

#### 英文用戶：
```
雙擊：start-valheim-keyboard-genie.bat
```

**優點：**
- 自動檢查和安裝依賴
- 用戶友好的介面
- 自動錯誤處理
- 包含完整使用說明

**需求：**
- Windows 系統
- 安裝 Python 3.6+

---

### 2. 🎯 完全無程式背景用戶

**使用獨立執行檔（.exe）**

#### 建置步驟：
1. 執行 `build-valheim-keyboard-genie.bat`
2. 等待建置完成
3. 分發 `dist/ValheimKeyboardGenie.exe`

**優點：**
- 無需安裝 Python
- 完全獨立運行
- 一鍵執行

**需求：**
- 僅需 Windows 系統

---

### 3. 🛠️ 開發者/進階用戶

**直接執行 Python 腳本**

```bash
pip install -r requirements.txt
python valheim_keyboard_genie.py
```

---

## 檔案結構說明

```
valheim-keyboard-genie/
├── valheim_keyboard_genie.py          # 主程式
├── requirements.txt                   # Python 依賴
├── start-valheim-keyboard-genie.bat   # 英文版批處理檔案
├── build-valheim-keyboard-genie.bat   # 建置執行檔腳本
├── user-manual.txt                    # 用戶說明檔案
├── developer-guide.md                 # 本檔案
└── README.md                         # 專案說明
```

---

## 分發建議

### 給一般用戶：
提供以下檔案：
- `valheim_keyboard_genie.py`
- `requirements.txt`
- `start-valheim-keyboard-genie.bat`
- `user-manual.txt`

### 給完全無程式背景用戶：
提供以下檔案：
- `dist/ValheimKeyboardGenie.exe`
- `user-manual.txt`

---

## 建置獨立執行檔詳細說明

### 自動建置（推薦）：
```batch
雙擊：build-valheim-keyboard-genie.bat
```

### 手動建置：
```bash
# 安裝 PyInstaller
pip install pyinstaller

# 建置單一執行檔
pyinstaller --onefile --console --name "ValheimKeyboardGenie" valheim_keyboard_genie.py

# 輸出檔案位於：dist/ValheimKeyboardGenie.exe
```

### PyInstaller 參數說明：
- `--onefile`: 打包成單一執行檔
- `--console`: 顯示控制台視窗供用戶回饋
- `--name`: 指定執行檔名稱
- `--collect-all`: 全面收集模組依賴

---

## 常見問題解決

### Q: 批處理檔案無法執行
A: 
1. 檢查 Python 是否正確安裝
2. 確保檔案位於同一目錄
3. 以系統管理員身分執行

### Q: 執行檔建置失敗
A:
1. 確保所有依賴已安裝：`pip install -r requirements.txt`
2. 確保 PyInstaller 已安裝：`pip install pyinstaller`
3. 檢查是否有防毒軟體干擾

### Q: 執行檔過大
A:
- 使用 `--exclude-module` 排除不必要的模組
- 考慮使用 UPX 壓縮（需額外安裝）

---

## 進階自訂

### 自訂圖標：
1. 準備 `.ico` 格式圖標檔案
2. 修改 `build-valheim-keyboard-genie.bat` 中的 `--icon` 參數

### 加入額外檔案：
使用 `--add-data` 參數：
```bash
--add-data "config.txt;."
```

### 隱藏命令提示字元：
- 使用 `--windowed` 參數（已包含在建置腳本中）
- 或修改程式為 GUI 版本

---

## 測試建議

### 批處理檔案測試：
1. 在乾淨的 Windows 系統上測試
2. 測試有/無 Python 環境
3. 測試網路連接正常/異常情況

### 執行檔測試：
1. 在沒有 Python 的系統上測試
2. 測試不同 Windows 版本
3. 檢查檔案大小和啟動速度

---

## 版本更新流程

1. 更新 `valheim_keyboard_genie.py`
2. 測試功能正常
3. 更新版本號和說明檔案
4. 重新建置執行檔
5. 更新分發檔案