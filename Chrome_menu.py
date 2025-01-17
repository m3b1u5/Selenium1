# ДЗ: Selenium (Chrome)
import time

# importing requirements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# setting up driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'  # URL to test
driver.get(base_url)
driver.set_window_size(1920, 1080)

# USERNAME input
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")
print("Input login")

# PASSWORD input
user_password = driver.find_element(By.XPATH, "//*[@id='password']")
user_password.send_keys("secret_sauce")
print("Input password")

# LOGIN button click
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print("Click on Login Button")
print(f"Current URLS is: {driver.current_url}")

# Menu and Logout click
menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]').click()
print('Menu button click')
time.sleep(1)
logout_button = driver.find_element(By.ID, 'logout_sidebar_link').click()
print('Logout button click')

# URL check
get_url = driver.current_url
target_url = "https://www.saucedemo.com/"
assert target_url == get_url, "URL not correct"
print("URL correct")

driver.close()
