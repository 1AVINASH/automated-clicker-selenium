# safe_clicker.py (no sudo needed!)
import pyautogui
from pynput import keyboard
import threading
import time

running = True

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping...")
        running = False
        return False

def click_loop():
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"Clicking at ({x}, {y})")
    while running:
        pyautogui.click(x, y)
        time.sleep(0.01)

listener = keyboard.Listener(on_press=on_press)
listener.start()

click_thread = threading.Thread(target=click_loop)
click_thread.start()

click_thread.join()
