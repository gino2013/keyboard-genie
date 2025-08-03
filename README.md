# Valheim Keyboard Genie / Valheim 鍵盤精靈

<table>
<tr>
<td width="50%">

## English Version

Automated keyboard and mouse input simulation program designed specifically for Valheim gameplay automation.

### Features

- Press F1 key to start automation, F2 to stop
- Every 20 minutes: automatically press number keys (1-7 cycling, 10 presses per key)
- Every 2 minutes: double-click left mouse button
- Every 240 minutes: press keys 8 & 9 in cycle (4-hour intervals)
- Automatically ensure English input method and lowercase mode
- Uses Windows API for direct key sending, enhancing Valheim compatibility
- Detailed bilingual logging with UTF-8 support
- Administrator privilege checking
- Graceful shutdown support with F2 key

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

#### Direct Execution:
```bash
python valheim_keyboard_genie.py
```

#### Windows Batch File:
Double-click `start-valheim-keyboard-genie.bat`

#### Standalone Executable:
Use `build-valheim-keyboard-genie.bat` to create `ValheimKeyboardGenie.exe`

#### Ready-to-Use Executable:
Go to `dist/` folder and double-click `ValheimKeyboardGenie.exe` for immediate use

### Controls

1. Program waits for F1 key press after startup
2. Press F1 to start automation
3. Press F2 to stop automation
4. Press `Ctrl+C` to force quit

### How It Works

- **Key Cycling**: Sequentially cycles through number keys 1-7, pressing each key 10 times before switching to the next
- **Mouse Clicking**: Double-clicks left mouse button every 2 minutes with 0.5s interval
- **Long Cycle Keys**: Presses key 8 every 4 hours, then key 9 after another 4 hours
- **Input Method Management**: Automatically switches to English input method and turns off Caps Lock
- **Direct API**: Uses Windows SendInput API to ensure keys work properly in Valheim

### Logging

Program generates `valheim_keyboard_genie.log` file in current directory with bilingual UTF-8 support.

### System Requirements & Notes

- **Windows**: Recommended to run as administrator for best Valheim compatibility
- **Key Mapping**: Uses top number row keys (not numpad) 1-9
- **Input Method**: Program automatically switches to English input method and ensures lowercase mode
- **Foreground Window**: Ensure Valheim is the foreground window to receive key inputs
- **Valheim Specific**: Optimized timing and key sequences for Valheim gameplay

</td>
<td width="50%">

## 中文版 / Chinese

專為 Valheim 遊戲自動化設計的自動按鍵和滑鼠輸入模擬程序。

### 功能

- 按 F1 鍵啟動自動化，F2 鍵停止
- 每20分鐘自動按下數字鍵（1-7依序輪換，每個鍵按10次）
- 每2分鐘點擊滑鼠左鍵兩次
- 每240分鐘按8、9鍵循環（4小時間隔）
- 自動確保英文輸入法和小寫模式
- 使用 Windows API 直接發送按鍵，提升 Valheim 兼容性
- 詳細的雙語日誌記錄（支援UTF-8）
- 管理員權限檢查
- 支持 F2 鍵優雅停止

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 使用方法

#### 直接執行：
```bash
python valheim_keyboard_genie.py
```

#### Windows 批處理檔案：
雙擊 `start-valheim-keyboard-genie.bat`

#### 獨立執行檔：
使用 `build-valheim-keyboard-genie.bat` 創建 `ValheimKeyboardGenie.exe`

#### 即用執行檔：
進入 `dist/` 資料夾，雙擊 `ValheimKeyboardGenie.exe` 即可直接使用

### 操作控制

1. 程序啟動後會等待按下 F1 鍵
2. 按 F1 鍵開始自動化
3. 按 F2 鍵停止自動化
4. 按 `Ctrl+C` 強制退出

### 工作原理

- **按鍵循環**: 依序輪換數字鍵 1-7，每個鍵連續按10次後切換到下一個鍵
- **滑鼠點擊**: 每2分鐘點擊滑鼠左鍵兩次，間隔0.5秒
- **長週期按鍵**: 每4小時按一次8鍵，再4小時後按9鍵
- **輸入法管理**: 自動切換到英文輸入法並關閉 Caps Lock
- **直接API**: 使用 Windows SendInput API 確保按鍵在 Valheim 中正常工作

### 日誌

程序會在當前目錄生成 `valheim_keyboard_genie.log` 文件記錄雙語運行日誌，支援UTF-8。

### 系統要求和注意事項

- **Windows**: 建議以管理員身份運行以確保在 Valheim 中的最佳兼容性
- **按鍵映射**: 使用上方數字列（非數字鍵盤）的 1-9 鍵
- **輸入法**: 程序會自動切換到英文輸入法並確保小寫模式
- **前景窗口**: 確保 Valheim 為前景窗口以接收按鍵輸入
- **Valheim 專用**: 針對 Valheim 遊戲玩法優化的時間和按鍵序列

</td>
</tr>
</table>

## File Structure / 檔案結構

```
valheim-keyboard-genie/
├── .gitignore                         # Git ignore rules
├── CLAUDE.md                          # Project instructions for Claude
├── valheim_keyboard_genie.py          # Main program / 主程式
├── requirements.txt                   # Python dependencies / Python 依賴
├── start-valheim-keyboard-genie.bat   # Startup script / 啟動腳本
├── build-valheim-keyboard-genie.bat   # Build executable / 建置執行檔
├── user-manual.txt                    # User manual / 用戶手冊
├── developer-guide.md                 # Developer guide / 開發者指南
├── README.md                          # This file / 本檔案
└── dist/                              # Distribution folder / 分發資料夾
    ├── ValheimKeyboardGenie.exe       # Ready-to-use executable / 即用執行檔
    ├── user-manual.txt                # User manual copy / 用戶手冊副本
    ├── README.md                      # Documentation copy / 說明文件副本
    └── keyboard_genie.log             # Runtime log / 運行日誌
```

## Distribution Options / 分發選項

### For Regular Users / 一般用戶
- `start-valheim-keyboard-genie.bat` - Automatic setup and launch / 自動設置並啟動

### For Non-Technical Users / 非技術用戶  
- `dist/ValheimKeyboardGenie.exe` - Ready-to-use standalone executable / 即用獨立執行檔

### For Developers / 開發者
- Direct Python execution / 直接執行 Python

## License / 許可證

This project is for educational and research purposes only. Use responsibly and in accordance with game terms of service.

本項目僅供教育和研究目的使用。請負責任地使用並遵守遊戲服務條款。