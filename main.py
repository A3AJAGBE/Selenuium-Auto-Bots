import os
import time

from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys

load_dotenv()

ACCOUNT_EMAIL = os.environ.get('EMAIL')
ACCOUNT_PASSWORD = os.environ.get('PASSWORD')

CHROME_DRIVER_PATH = "/Users/a3ajagbe/Documents/chromedriver"
sl = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
sl.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=103810046&keywords=python%20developer&location=County"
       "%20Dublin%2C%20Ireland")

sign_in_button = sl.find_element_by_link_text("Sign in")
sign_in_button.click()

# Wait for the next page to load.
time.sleep(5)

email_field = sl.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = sl.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)
