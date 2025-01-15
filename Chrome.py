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
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'  # URL to test
driver.get(base_url)
# driver.maximize_window()
# driver.set_window_size(1920, 1080)

# USERNAME input
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")
print("Input login")

# PASSWORD input
user_password = driver.find_element(By.XPATH, "//*[@id='password']")
user_password.send_keys("secret_sau")  # worng password
print("Input password")

# LOGIN button click
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print("Click on Login Button")
print(f"Current URLS is: {driver.current_url}")
get_url = driver.current_url
target_url = "https://www.saucedemo.com/inventory.html"

# TESTS #

# URL check
# assert target_url == get_url, "URL not correct"
# print("URL correct")

# WRONG PASSWORD input check
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert value_warning_text == "Epic sadface: Username and password do not match any user in this service", "Wrong message"
print('Error message correct')
error_button = driver.find_element(By.XPATH, "//button[@class='error-button']")
error_button.click()
print('Error button click')

# TITLE check
# text_products = driver.find_element(By.XPATH, "//span[@class='title']")
# print(f"Title is: {text_products.text}")
# value_text_products = text_products.text
# assert value_text_products == "Products", "Title not correct"
# print("Title correct")

print(f"{' All tests passed! ':=^50}")

driver.close()
