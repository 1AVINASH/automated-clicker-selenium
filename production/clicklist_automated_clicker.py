from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import threading
from pynput import keyboard


class Clicker:
    # --- Clicker Control Variables ---
    is_clicking = True
    stop_flag = False
    # 2029 483
    CLICK_X, CLICK_Y = 2029, 483
    CLICK_INTERVAL = 0.1

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click(self):
        # Open the game page
        self.driver.get("https://pokeheroes.com/pokemon_lite?cl_type=random")  # ← Replace with your actual game URL
        # driver.get("https://example.com/your-game")  # ← Replace with your actual game URL

        time.sleep(5)  # Wait for game to load manually or automate login


        # --- Click Logic ---
        def click_loop():

            click_js = f"""
            var evt = new MouseEvent('click', {{
                bubbles: true,
                cancelable: true,
                clientX: {self.CLICK_X},
                clientY: {self.CLICK_Y}
            }});
            document.elementFromPoint({self.CLICK_X}, {self.CLICK_Y}).dispatchEvent(evt);
            """

            while not self.stop_flag:
                if self.is_clicking:
                    self.driver.execute_script(click_js)
                    time.sleep(self.CLICK_INTERVAL)
                else:
                    time.sleep(0.1)

        # --- Hotkey Listener Logic ---
        def on_press(key):
            try:
                if key.char == 's':
                    self.is_clicking = True
                    print("▶️ Started clicking.")
                elif key.char == 'p':
                    self.is_clicking = False
                    print("⏸️ Paused.")
            except AttributeError:
                pass  # Ignore special keys

        # --- Start Threads ---
        click_thread = threading.Thread(target=click_loop)
        click_thread.daemon = True
        click_thread.start()

        print("Controls: [s] Start | [p] Pause | [q] Quit")
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

        # --- Cleanup ---
        self.driver.quit()


        """
        document.addEventListener("click", function(e) {
        console.log("Clicked at:", e.clientX, e.clientY);
        });
        """