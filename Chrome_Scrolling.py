# ДЗ: Selenium (Chrome)
import time

# importing requirements
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# setting up driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = 'https://www.saucedemo.com/'  # URL to test
driver.get(base_url)
# driver.maximize_window()
driver.set_window_size(1920, 1080)

# USERNAME input
user_name = driver.find_element(By.XPATH, "//*[@id='user-name']")
user_name.send_keys("admin")  # incorrect
print("Input login")

# PASSWORD input
user_password = driver.find_element(By.XPATH, "//*[@id='password']")
user_password.send_keys("qwerty")  # incorrect
print("Input password")

# Form clear and correct input
time.sleep(2)
# user_name.clear()
user_name.send_keys(Keys.CONTROL + 'a')
user_name.send_keys(Keys.DELETE)
print('Clear username')
time.sleep(1)
user_password.send_keys(Keys.CONTROL + 'a')
user_password.send_keys(Keys.DELETE)
print('Clear password')
time.sleep(1)
user_name.send_keys('standard_user')
user_password.send_keys('secret_sauce')
time.sleep(1)
print('Input correct username and password')

# LOGIN button click
button_login = driver.find_element(By.ID, "login-button")
button_login.click()
print("Click on Login Button")
print(f"Current URLS is: {driver.current_url}")

# URL check
get_url = driver.current_url
target_url = "https://www.saucedemo.com/inventory.html"
assert target_url == get_url, "URL not correct"
print("URL correct")

# Adding items to shop cart
button_add_backpack = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']").click()
button_add_bike = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']").click()
button_add_t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
button_add_jacket = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
button_add_onesie = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']").click()
button_add_t_shirt_red = driver.find_element(By.XPATH, "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
print('All items added to shop cart')

# Open Shop cart
button_cart_link = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
print('Shop cart opened')

# Scrolling to last item in cart
actions = ActionChains(driver)
element = driver.find_element(By.ID, "item_3_title_link")
actions.move_to_element(element).perform()
print('Scrolling to the last item in cart')
time.sleep(3)
driver.execute_script("window/scrollTo(0,0)")

driver.close()
