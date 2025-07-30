# 鍵盤精靈 (Keyboard Genie)

自動按鍵程序，定時模擬鍵盤輸入。

## 功能

- 每30分鐘自動按下1、2、3鍵
- 每3分鐘自動按下4鍵
- 支持日誌記錄
- 支持優雅停止

## 安裝依賴

```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python keyboard_genie.py
```

按 `Ctrl+C` 停止程序。

## 日誌

程序會在當前目錄生成 `keyboard_genie.log` 文件記錄運行日誌。

## 注意事項

- macOS 用戶需要在「系統偏好設置」→「安全性與隱私」→「輔助功能」中給予 Terminal 或 Python 權限
- Windows 用戶可能需要以管理員身份運行