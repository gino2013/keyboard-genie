#!/usr/bin/env python3
"""
鍵盤精靈 - 自動按鍵程序
每30分鐘按1,2,3鍵，每3分鐘按4鍵
"""

import time
import threading
import logging
from datetime import datetime
from pynput.keyboard import Key, Controller


class KeyboardGenie:
    def __init__(self):
        self.keyboard = Controller()
        self.running = False
        self.timer_30min = None
        self.timer_3min = None
        
        # 設置日誌
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('keyboard_genie.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def press_keys_123(self):
        """按下1,2,3鍵"""
        try:
            keys = ['1', '2', '3']
            for key in keys:
                self.keyboard.press(key)
                self.keyboard.release(key)
                time.sleep(0.3)
            
            self.logger.info("按下鍵盤: 1, 2, 3")
            
        except Exception as e:
            self.logger.error(f"按鍵1,2,3時發生錯誤: {e}")
        finally:
            if self.running:
                self.schedule_30min_task()
    
    def press_key_4(self):
        """按下4鍵"""
        try:
            self.keyboard.press('4')
            self.keyboard.release('4')
            self.logger.info("按下鍵盤: 4")
            
        except Exception as e:
            self.logger.error(f"按鍵4時發生錯誤: {e}")
        finally:
            if self.running:
                self.schedule_3min_task()
    
    def schedule_30min_task(self):
        """安排30分鐘定時任務"""
        if self.running:
            self.timer_30min = threading.Timer(30 * 60, self.press_keys_123)  # 30分鐘 = 1800秒
            self.timer_30min.daemon = True
            self.timer_30min.start()
    
    def schedule_3min_task(self):
        """安排3分鐘定時任務"""
        if self.running:
            self.timer_3min = threading.Timer(3 * 60, self.press_key_4)  # 3分鐘 = 180秒
            self.timer_3min.daemon = True
            self.timer_3min.start()
    
    def start(self):
        """啟動鍵盤精靈"""
        if self.running:
            self.logger.warning("鍵盤精靈已在運行中")
            return
        
        self.running = True
        self.logger.info("鍵盤精靈啟動")
        
        # 立即執行一次，然後開始定時
        self.press_keys_123()
        self.press_key_4()
        
        self.logger.info("定時任務已設置:")
        self.logger.info("- 每30分鐘按1,2,3鍵")
        self.logger.info("- 每3分鐘按4鍵")
    
    def stop(self):
        """停止鍵盤精靈"""
        self.running = False
        
        if self.timer_30min:
            self.timer_30min.cancel()
        if self.timer_3min:
            self.timer_3min.cancel()
        
        self.logger.info("鍵盤精靈已停止")


def main():
    genie = KeyboardGenie()
    
    try:
        genie.start()
        
        print("鍵盤精靈正在運行...")
        print("按 Ctrl+C 停止程序")
        
        # 保持程序運行
        while genie.running:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n收到停止信號")
        genie.stop()
        print("程序已停止")


if __name__ == "__main__":
    main()