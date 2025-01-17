# ДЗ: Selenium (Chrome)
import time

# importing requirements
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# setting up driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument("--headless")

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'  # URL to test
driver.get(base_url)
driver.set_window_size(1920, 1080)

# USERNAME input
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
print('Input Login')

# Select and remove input from User login form
user_name.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
user_name.send_keys(Keys.BACKSPACE)
time.sleep(1)
print('User Name input removed')

# PASSWORD input
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys('secret_sauce')
print('Input Password')

# Select and remove input from password form
password.send_keys(Keys.CONTROL + 'a')
time.sleep(1)
password.send_keys(Keys.BACKSPACE)
time.sleep(1)
print('Password input removed')

# LOGIN button click
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print('Click Login Button')

time.sleep(3)
# driver.refresh() # refresh page

driver.close()
