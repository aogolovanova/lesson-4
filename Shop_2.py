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
sleep_timeout = 3
HTML = driver.find_element_by_css_selector('[href="http://practice.automationtesting.in/product-category/html/"]').click()
sleep_timeout = 3
product = driver.find_elements_by_css_selector(".masonry-done .type-product")
print(product)
if len(product) == 3:
    print("В корзине 3 товара")
else:
    print("Ошибка!")
