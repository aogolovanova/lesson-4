import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
HTML5 = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product/html5-forms/"]').click()

element = driver.find_element_by_css_selector('[class="product_title entry-title"]')
element_get_text = element.text
assert element_get_text == "HTML5 Forms"
if element_get_text == str("HTML5 Forms"):
    print("заголовок: HTML5 Forms")
else:
    print("Ошибка!")
driver.quit()
