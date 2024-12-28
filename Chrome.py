# ДЗ: Импорт Selenium (Chrome)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.maximize_window()
# driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")

user_password = driver.find_element(By.ID, "password")
user_password.send_keys("secret_sauce")

# time.sleep(10)
# driver.close()
