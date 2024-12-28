# ДЗ: Импорт Selenium (Firefox)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("standard_user")

user_password = driver.find_element(By.XPATH, "//*[@id='password']")
user_password.send_keys("secret_sauce")

# time.sleep(10)
# driver.close()
