# 鍵盤精靈 / Keyboard Genie

<table>
<tr>
<td width="50%">

## 中文版 / Chinese

自動按鍵程序，定時模擬鍵盤和滑鼠輸入。

### 功能

- 按 F1 鍵啟動自動化
- 每30分鐘自動按下數字鍵（1-9依序輪換，每個鍵按10次）
- 每1分鐘點擊滑鼠左鍵兩次
- 自動確保英文輸入法和小寫模式
- 使用 Windows API 直接發送按鍵，提升遊戲兼容性
- 詳細日誌記錄（支援UTF-8中文）
- 管理員權限檢查
- 支持優雅停止

### 安裝依賴

```bash
pip install -r requirements.txt
```

### 使用方法

```bash
python keyboard_genie.py
```

1. 程序啟動後會等待按下 F1 鍵
2. 按下 F1 鍵後立即開始自動化
3. 按 `Ctrl+C` 停止程序

### 工作原理

- **按鍵循環**: 依序輪換數字鍵 1-9，每個鍵連續按10次後切換到下一個鍵
- **滑鼠點擊**: 每分鐘點擊滑鼠左鍵兩次，間隔0.5秒
- **輸入法管理**: 自動切換到英文輸入法並關閉 Caps Lock
- **直接API**: 使用 Windows SendInput API 確保按鍵在遊戲中正常工作

### 日誌

程序會在當前目錄生成 `keyboard_genie.log` 文件記錄運行日誌，支援中文字符。

### 系統要求和注意事項

- **Windows**: 建議以管理員身份運行以確保在遊戲中正常工作
- **按鍵映射**: 使用上方數字列（非數字鍵盤）的 1-7 鍵
- **輸入法**: 程序會自動切換到英文輸入法並確保小寫模式
- **前景窗口**: 確保目標應用程序為前景窗口以接收按鍵輸入

</td>
<td width="50%">

## English Version

Automated keyboard and mouse input simulation program with timed scheduling.

### Features

- Press F1 key to start automation
- Every 30 minutes: automatically press number keys (1-9 cycling, 10 presses per key)
- Every 1 minute: double-click left mouse button
- Automatically ensure English input method and lowercase mode
- Uses Windows API for direct key sending, enhancing game compatibility
- Detailed logging with UTF-8 Chinese character support
- Administrator privilege checking
- Graceful shutdown support

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Usage

```bash
python keyboard_genie.py
```

1. Program waits for F1 key press after startup
2. Automation starts immediately after pressing F1
3. Press `Ctrl+C` to stop the program

### How It Works

- **Key Cycling**: Sequentially cycles through number keys 1-9, pressing each key 10 times before switching to the next
- **Mouse Clicking**: Double-clicks left mouse button every minute with 0.5s interval
- **Input Method Management**: Automatically switches to English input method and turns off Caps Lock
- **Direct API**: Uses Windows SendInput API to ensure keys work properly in games

### Logging

Program generates `keyboard_genie.log` file in current directory with UTF-8 Chinese character support.

### System Requirements & Notes

- **Windows**: Recommended to run as administrator to ensure proper functionality in games
- **Key Mapping**: Uses top number row keys (not numpad) 1-7
- **Input Method**: Program automatically switches to English input method and ensures lowercase mode
- **Foreground Window**: Ensure target application is the foreground window to receive key inputs

</td>
</tr>
</table>