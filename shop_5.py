import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")

My_Account = driver.find_element_by_id("menu-item-50").click()

email = driver.find_element_by_id("username")
email.send_keys("vchera2021@mail.ru")
sleep_timeout = 3
password = driver.find_element_by_id("password")
password.send_keys(";bdjnyjt")
login = driver.find_element_by_css_selector('[value="Login"]').click()

shop = driver.find_element_by_id("menu-item-40").click()
WebApp = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
WebApp.click()
sleep_timeout = 3

basket = driver.find_element_by_id('wpmenucartli')
basket.click()
sleep_timeout = 5

Price = driver.find_element_by_css_selector('[class="amount"]')
Price_get_text = Price.text
assert Price_get_text == "₹180.00"

item = driver.find_element_by_css_selector('[class="cartcontents"]')
item_get_text = item.text
assert item_get_text == ("1 Item")

basket = driver.find_element_by_id('wpmenucartli')
basket.click()

Subtotal = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]>span'), "180.00"))
Total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart_item :nth-child(6)>span'), "180.00"))
