from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# --- Login credentials ---

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")


class Logger:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def login(self):
        # --- Go to login page ---
        self.driver.get("https://pokeheroes.com/login")  # 🔁 Replace with the actual login URL

        # --- Wait for the page to load ---
        time.sleep(3)

        # --- Fill in login form ---
        self.driver.find_element(By.NAME, "username_login").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password_login").send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Log In']").click()  # Or submit the form

        # --- Wait for login to process ---
        time.sleep(5)

        # ✅ Now logged in, ready to start game automation!
