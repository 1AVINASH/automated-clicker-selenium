from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from login import Logger
from clicklist_automated_clicker import Clicker

# Launch Chrome in a normal (detached) window
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")

# (Optional) run in background
# options.add_argument("--headless")  # Uncomment if full headless mode is fine

# Adjust path to chromedriver if needed
driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

logger = Logger(driver=driver)
logger.login()
clicker = Clicker(driver=driver)
clicker.click()