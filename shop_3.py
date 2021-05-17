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
sleep_timeout = 8
element = driver.find_element_by_css_selector('[class="orderby"]')
select = Select(element)
select.select_by_visible_text(select.options[0].text)
if select.all_selected_options[0].text == ("Default sorting"):
    print("Default sorting")
else:
    print("Ошибка")
sleep_timeout = 5
element = driver.find_element_by_css_selector('[class="orderby"]')
select = Select(element)
select.select_by_visible_text(select.options[5].text)

sleep_timeout = 8
element = driver.find_element_by_css_selector('[class="orderby"]')
select = Select(element)
select.select_by_visible_text(select.options[5].text)
if select.all_selected_options[5].text == ("Sort by price: high to low"):
    print("Sort by price: high to low")
else:
    print("Ошибка")
driver.quit()
