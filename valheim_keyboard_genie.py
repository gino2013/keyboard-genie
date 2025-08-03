#!/usr/bin/env python3
"""
Valheim Keyboard Genie - Automated Key Pressing Program
Press F1 to start, F2 to stop, keys 1-7 rotate every 20 minutes (10 times each), mouse click every 2 minutes, keys 8 & 9 rotate every 240 minutes

Valheim 鍵盤精靈 - 自動按鍵程序
按F1鍵開始，F2鍵停止，每20分鐘按1-7鍵依序輪換（每個鍵按10次），每2分鐘點擊滑鼠，240分鐘輪換按8、9鍵
"""

import time
import threading
import logging
from datetime import datetime
from pynput.keyboard import Key, Controller, Listener
from pynput.mouse import Button, Controller as MouseController
import ctypes
from ctypes import wintypes
import os
import sys


class ValheimKeyboardGenie:
    def __init__(self):
        self.keyboard = Controller()
        self.mouse = MouseController()
        self.running = False
        self.timer_30min = None
        self.timer_3min = None
        self.timer_240min_8 = None
        self.timer_240min_9 = None
        self.key_8_pressed = False  # 追踪key 8是否已按過
        self.started = False
        self.global_listener = None  # 全局按鍵監聽器
        
        # 按鍵計數器
        self.current_key_index = 0  # 當前按鍵索引 (0-6 對應 1-7)
        self.key_press_count = 0    # 當前按鍵的按壓次數
        self.keys_list = ['1', '2', '3', '4', '5', '6', '7']
        
        # 設置日誌，指定UTF-8編碼避免中文字符錯誤
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('valheim_keyboard_genie.log', encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        
        # 檢查是否以管理員身份運行
        self.check_admin_privileges()
    
    def check_admin_privileges(self):
        """Check if running as administrator / 檢查是否以管理員身份運行"""
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                self.logger.warning("建議以管理員身份運行程式以確保在Valheim中正常工作")
                self.logger.warning("請右鍵點擊程式選擇'以管理員身分執行'")
                self.logger.warning("Recommend running as Administrator for best Valheim compatibility")
                self.logger.warning("Right-click the program and select 'Run as administrator'")
            else:
                self.logger.info("程式正以管理員身份運行 / Program running as Administrator")
        except:
            self.logger.warning("無法檢查管理員權限 / Cannot check administrator privileges")
    
    def send_key_direct(self, key_code):
        """使用Windows SendInput API直接發送按鍵（確保使用上方數字列）"""
        """Use Windows SendInput API to send keys directly (ensure using top number row)"""
        try:
            # 定義Windows結構
            PUL = ctypes.POINTER(ctypes.c_ulong)
            class KeyBdInput(ctypes.Structure):
                _fields_ = [("wVk", ctypes.c_ushort),
                           ("wScan", ctypes.c_ushort),
                           ("dwFlags", ctypes.c_ulong),
                           ("time", ctypes.c_ulong),
                           ("dwExtraInfo", PUL)]

            class HardwareInput(ctypes.Structure):
                _fields_ = [("uMsg", ctypes.c_ulong),
                           ("wParamL", ctypes.c_short),
                           ("wParamH", ctypes.c_ushort)]

            class MouseInput(ctypes.Structure):
                _fields_ = [("dx", ctypes.c_long),
                           ("dy", ctypes.c_long),
                           ("mouseData", ctypes.c_ulong),
                           ("dwFlags", ctypes.c_ulong),
                           ("time", ctypes.c_ulong),
                           ("dwExtraInfo", PUL)]

            class Input_I(ctypes.Union):
                _fields_ = [("ki", KeyBdInput),
                           ("mi", MouseInput),
                           ("hi", HardwareInput)]

            class Input(ctypes.Structure):
                _fields_ = [("type", ctypes.c_ulong),
                           ("ii", Input_I)]
            
            # 上方數字列的VK代碼和Scan Code映射
            # 使用Scan Code確保是上方數字列，不是數字鍵盤
            key_map = {
                '1': {'vk': 0x31, 'scan': 0x02},  # 上方數字列1
                '2': {'vk': 0x32, 'scan': 0x03},  # 上方數字列2
                '3': {'vk': 0x33, 'scan': 0x04},  # 上方數字列3
                '4': {'vk': 0x34, 'scan': 0x05},  # 上方數字列4
                '5': {'vk': 0x35, 'scan': 0x06},  # 上方數字列5
                '6': {'vk': 0x36, 'scan': 0x07},  # 上方數字列6
                '7': {'vk': 0x37, 'scan': 0x08},  # 上方數字列7
                '8': {'vk': 0x38, 'scan': 0x09},  # 上方數字列8
                '9': {'vk': 0x39, 'scan': 0x0A},  # 上方數字列9
            }
            
            if key_code in key_map:
                vk_code = key_map[key_code]['vk']
                scan_code = key_map[key_code]['scan']
                
                self.logger.info(f"發送按鍵 {key_code} (VK: 0x{vk_code:02X}, Scan: 0x{scan_code:02X})")
                self.logger.info(f"Sending key {key_code} (VK: 0x{vk_code:02X}, Scan: 0x{scan_code:02X})")
                
                # 按下按鍵 - 使用Scan Code確保是正確的按鍵
                extra = ctypes.c_ulong(0)
                ii_ = Input_I()
                # KEYEVENTF_SCANCODE = 0x0008, 使用Scan Code而不Virtual Key
                ii_.ki = KeyBdInput(0, scan_code, 0x0008, 0, ctypes.pointer(extra))
                x = Input(ctypes.c_ulong(1), ii_)
                result1 = ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
                
                time.sleep(0.05)
                
                # 釋放按鍵 - KEYEVENTF_KEYUP | KEYEVENTF_SCANCODE = 0x0002 | 0x0008 = 0x000A
                ii_.ki = KeyBdInput(0, scan_code, 0x000A, 0, ctypes.pointer(extra))
                x = Input(ctypes.c_ulong(1), ii_)
                result2 = ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
                
                success = result1 > 0 and result2 > 0
                self.logger.info(f"按鍵 {key_code} 發送結果: {success} (down: {result1}, up: {result2})")
                self.logger.info(f"Key {key_code} send result: {success} (down: {result1}, up: {result2})")
                return success
            return False
            
        except Exception as e:
            self.logger.error(f"直接發送按鍵失敗: {e}")
            self.logger.error(f"Direct key send failed: {e}")
            return False
    
    def send_mouse_click_direct(self):
        """使用Windows API直接發送滑鼠點擊"""
        """Use Windows API to send mouse clicks directly"""
        try:
            # 滑鼠左鍵按下
            ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTDOWN
            time.sleep(0.05)
            # 滑鼠左鍵釋放
            ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)  # MOUSEEVENTF_LEFTUP
            return True
        except Exception as e:
            self.logger.error(f"直接發送滑鼠點擊失敗: {e}")
            self.logger.error(f"Direct mouse click failed: {e}")
            return False
    
    def ensure_english_input(self):
        """確保輸入法為英文小寫"""
        """Ensure input method is English lowercase"""
        try:
            # 取得當前前景視窗
            user32 = ctypes.windll.user32
            kernel32 = ctypes.windll.kernel32
            
            # 取得當前活動視窗
            hwnd = user32.GetForegroundWindow()
            if hwnd == 0:
                self.logger.warning("無法取得前景視窗 / Cannot get foreground window")
                return
                
            # 取得視窗的輸入法資訊
            thread_id = user32.GetWindowThreadProcessId(hwnd, None)
            hkl = user32.GetKeyboardLayout(thread_id)
            
            # 檢查是否為英文輸入法 (0x04090409 為美式英文)
            if hkl & 0xFFFF != 0x0409:  # 不是英文
                self.logger.info("切換到英文輸入法 / Switching to English input")
                # 嘗試切換到英文輸入法
                # 方法1: 使用Alt+Shift
                self.keyboard.press(Key.alt)
                self.keyboard.press(Key.shift)
                self.keyboard.release(Key.shift)
                self.keyboard.release(Key.alt)
                time.sleep(0.5)
                
                # 方法2: 如果還是不行，嘗試Ctrl+Space（常用於中英切換）
                self.keyboard.press(Key.ctrl)
                self.keyboard.press(Key.space)
                self.keyboard.release(Key.space)
                self.keyboard.release(Key.ctrl)
                time.sleep(0.5)
            
            # 確保Caps Lock關閉（小寫）
            caps_state = user32.GetKeyState(0x14)  # VK_CAPITAL = 0x14
            if caps_state & 1:  # Caps Lock開啟
                self.logger.info("關閉Caps Lock / Turning off Caps Lock")
                self.keyboard.press(Key.caps_lock)
                self.keyboard.release(Key.caps_lock)
                time.sleep(0.2)
                
            self.logger.info("輸入法狀態檢查完成 / Input method check completed")
            
        except Exception as e:
            self.logger.error(f"切換輸入法時發生錯誤: {e}")
            self.logger.error(f"Error switching input method: {e}")
            # 備用方案：直接嘗試常見的切換組合鍵
            try:
                self.keyboard.press(Key.alt)
                self.keyboard.press(Key.shift)
                self.keyboard.release(Key.shift)
                self.keyboard.release(Key.alt)
                time.sleep(0.5)
            except:
                pass
    
    def press_single_key(self):
        """按下當前鍵（依序輪換1-7，每個鍵按10次）"""
        """Press current key (rotate 1-7, press each key 10 times)"""
        try:
            # 確保輸入法正確
            self.ensure_english_input()
            time.sleep(0.5)
            
            # 取得當前要按的鍵
            current_key = self.keys_list[self.current_key_index]
            self.key_press_count += 1
            
            self.logger.info(f"按鍵 {current_key}（第 {self.key_press_count}/10 次）")
            self.logger.info(f"Pressing key {current_key} ({self.key_press_count}/10 times)")
            
            # 嘗試使用直接API，如果失敗則使用pynput
            if not self.send_key_direct(current_key):
                self.logger.info(f"直接API失敗，使用pynput按鍵 {current_key}")
                self.logger.info(f"Direct API failed, using pynput for key {current_key}")
                self.keyboard.press(current_key)
                self.keyboard.release(current_key)
            
            # 檢查是否需要切換到下一個鍵
            if self.key_press_count >= 10:
                self.key_press_count = 0
                self.current_key_index = (self.current_key_index + 1) % len(self.keys_list)
                next_key = self.keys_list[self.current_key_index]
                self.logger.info(f"切換到下一個鍵: {next_key}")
                self.logger.info(f"Switching to next key: {next_key}")
            
            self.logger.info(f"按鍵 {current_key} 完成")
            self.logger.info(f"Key {current_key} completed")
            
        except Exception as e:
            self.logger.error(f"按鍵時發生錯誤: {e}")
            self.logger.error(f"Error during key press: {e}")
        finally:
            if self.running:
                self.schedule_20min_task()
    
    def click_mouse(self):
        """點擊滑鼠左鍵兩次"""
        """Click left mouse button twice"""
        try:
            # 點擊滑鼠左鍵兩次，間隔更長
            self.logger.info("正在點擊滑鼠第1次")
            self.logger.info("Clicking mouse 1st time")
            if not self.send_mouse_click_direct():
                self.mouse.click(Button.left, 1)
            time.sleep(0.5)
            self.logger.info("正在點擊滑鼠第2次")
            self.logger.info("Clicking mouse 2nd time")
            if not self.send_mouse_click_direct():
                self.mouse.click(Button.left, 1)
            
            self.logger.info("滑鼠點擊完成")
            self.logger.info("Mouse clicking completed")
            
        except Exception as e:
            self.logger.error(f"滑鼠點擊時發生錯誤: {e}")
            self.logger.error(f"Error during mouse clicking: {e}")
        finally:
            if self.running:
                self.schedule_2min_task()
    
    def schedule_20min_task(self):
        """安排20分鐘定時任務"""
        """Schedule 20-minute timer task"""
        if self.running:
            self.timer_30min = threading.Timer(20 * 60, self.press_single_key)  # 20分鐘 = 1200秒
            self.timer_30min.daemon = True
            self.timer_30min.start()
    
    def schedule_2min_task(self):
        """安排2分鐘定時任務"""
        """Schedule 2-minute timer task"""
        if self.running:
            self.timer_3min = threading.Timer(2 * 60, self.click_mouse)  # 2分鐘 = 120秒
            self.timer_3min.daemon = True
            self.timer_3min.start()
    
    def schedule_240min_task_8(self):
        """安排240分鐘定時任務按鍵8"""
        """Schedule 240-minute timer task for key 8"""
        if self.running:
            self.timer_240min_8 = threading.Timer(240 * 60, self.press_key_8)  # 240分鐘 = 14400秒
            self.timer_240min_8.daemon = True
            self.timer_240min_8.start()
    
    def schedule_240min_task_9(self):
        """安排240分鐘定時任務按鍵9"""
        """Schedule 240-minute timer task for key 9"""
        if self.running:
            self.timer_240min_9 = threading.Timer(240 * 60, self.press_key_9)  # 240分鐘 = 14400秒
            self.timer_240min_9.daemon = True
            self.timer_240min_9.start()
    
    def press_key_8(self):
        """按下數字鍵8"""
        """Press number key 8"""
        try:
            self.ensure_english_input()
            time.sleep(0.5)
            
            self.logger.info("按下數字鍵8 (240分鐘定時任務)")
            self.logger.info("Pressing number key 8 (240-minute timer task)")
            
            if not self.send_key_direct('8'):
                self.logger.info("直接API失敗，使用pynput按鍵8")
                self.logger.info("Direct API failed, using pynput for key 8")
                self.keyboard.press('8')
                self.keyboard.release('8')
            
            self.key_8_pressed = True
            self.logger.info("數字鍵8按下完成")
            self.logger.info("Number key 8 press completed")
            
        except Exception as e:
            self.logger.error(f"按鍵8時發生錯誤: {e}")
            self.logger.error(f"Error pressing key 8: {e}")
        finally:
            if self.running:
                self.schedule_240min_task_9()
    
    def press_key_9(self):
        """按下數字鍵9"""
        """Press number key 9"""
        try:
            self.ensure_english_input()
            time.sleep(0.5)
            
            self.logger.info("按下數字鍵9 (240分鐘定時任務)")
            self.logger.info("Pressing number key 9 (240-minute timer task)")
            
            if not self.send_key_direct('9'):
                self.logger.info("直接API失敗，使用pynput按鍵9")
                self.logger.info("Direct API failed, using pynput for key 9")
                self.keyboard.press('9')
                self.keyboard.release('9')
            
            self.logger.info("數字鍵9按下完成")
            self.logger.info("Number key 9 press completed")
            
        except Exception as e:
            self.logger.error(f"按鍵9時發生錯誤: {e}")
            self.logger.error(f"Error pressing key 9: {e}")
        finally:
            if self.running:
                # 重新開始240分鐘循環，從鍵8開始
                self.key_8_pressed = False
                self.schedule_240min_task_8()
    
    def start_global_listener(self):
        """開始全局按鍵監聽器（監聽F2停止鍵）"""
        """Start global key listener (listen for F2 stop key)"""
        def on_press(key):
            try:
                if key == Key.f2 and self.running:
                    self.logger.info("檢測到F2鍵，停止程式")
                    self.logger.info("F2 key detected, stopping program")
                    self.stop()
                    return False  # 停止監聽
            except AttributeError:
                pass
        
        self.global_listener = Listener(on_press=on_press)
        self.global_listener.daemon = True
        self.global_listener.start()
    
    def wait_for_f1_key(self):
        """等待按下F1鍵"""
        """Wait for F1 key press"""
        def on_press(key):
            try:
                if key == Key.f1 and not self.started:
                    self.started = True
                    self.logger.info("檢測到F1鍵，開始執行自動化")
                    self.logger.info("F1 key detected, starting automation")
                    self.start_automation()
                    return False  # 停止監聽
            except AttributeError:
                pass
        
        self.logger.info("等待按下F1鍵開始自動化...")
        self.logger.info("Waiting for F1 key to start automation...")
        self.logger.info("或按F2鍵停止程序")
        self.logger.info("Or press F2 key to stop program")
        with Listener(on_press=on_press) as listener:
            listener.join()
    
    def start_automation(self):
        """啟動自動化程序"""
        """Start automation program"""
        if self.running:
            self.logger.warning("Valheim鍵盤精靈已在運行中")
            self.logger.warning("Valheim Keyboard Genie is already running")
            return
        
        self.running = True
        self.logger.info("Valheim鍵盤精靈啟動")
        self.logger.info("Valheim Keyboard Genie started")
        
        # 啟動全局按鍵監聽器（監聽F2停止鍵）
        self.start_global_listener()
        
        # 確保輸入法為英文小寫
        self.ensure_english_input()
        time.sleep(1)
        
        # 按F1鍵後立即執行一次：先按當前鍵，再點擊滑鼠
        self.press_single_key()
        time.sleep(3)  # 等待3秒再執行下一個動作
        self.click_mouse()
        
        # 開始240分鐘定時任務循環
        self.schedule_240min_task_8()
        
        self.logger.info("定時任務已設置:")
        self.logger.info("Timer tasks have been set:")
        self.logger.info("- 每20分鐘按一個數字鍵（1-7依序輪換，每個鍵按10次）")
        self.logger.info("- Press number keys every 20 minutes (1-7 in rotation, 10 times each)")
        self.logger.info("- 每2分鐘點擊滑鼠左鍵兩次")
        self.logger.info("- Click left mouse button twice every 2 minutes")
        self.logger.info("- 240分鐘後按鍵8，再240分鐘後按鍵9（循環）")
        self.logger.info("- Press key 8 after 240 minutes, then key 9 after another 240 minutes (loop)")
    
    def stop(self):
        """停止鍵盤精靈"""
        """Stop keyboard genie"""
        self.running = False
        
        if self.timer_30min:
            self.timer_30min.cancel()
        if self.timer_3min:
            self.timer_3min.cancel()
        if self.timer_240min_8:
            self.timer_240min_8.cancel()
        if self.timer_240min_9:
            self.timer_240min_9.cancel()
        
        # 停止全局按鍵監聽器
        if self.global_listener:
            self.global_listener.stop()
        
        self.logger.info("Valheim鍵盤精靈已停止")
        self.logger.info("Valheim Keyboard Genie stopped")


def main():
    genie = ValheimKeyboardGenie()
    
    try:
        print("Valheim Keyboard Genie is ready")
        print("Press F1 key to start automation")
        print("Press F2 key to stop program")
        print("Press Ctrl+C to force quit")
        print("")
        print("Valheim鍵盤精靈已準備就緒")
        print("按下F1鍵開始自動化")
        print("按下F2鍵停止程序")
        print("或按 Ctrl+C 停止程序")
        
        # 等待F1鍵
        genie.wait_for_f1_key()
        
        # 保持程序運行
        while genie.running:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nReceived stop signal")
        print("收到停止信號")
        genie.stop()
        print("Program stopped")
        print("程序已停止")


if __name__ == "__main__":
    main()