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

Logout = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "body"), "Logout"))

