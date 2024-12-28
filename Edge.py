# ДЗ: Импорт Selenium (Edge)
import time

from selenium import webdriver

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options)
base_url = 'https://www.saucedemo.com/'
driver.get(base_url)
driver.set_window_size(1920, 1080)

time.sleep(10)
driver.close()
