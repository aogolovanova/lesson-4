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
sleep_timeout = 3
Android = driver.find_element_by_css_selector(".products.masonry-done :nth-child(1) :nth-child(1) :nth-child(2)").click()
Price = driver.find_element_by_css_selector(".price>del>span")
Price_get_text = Price.text
assert Price_get_text == "₹600.00"

Price_new = driver.find_element_by_css_selector(".price>ins>span")
Price_new_get_text = Price_new.text
assert Price_new_get_text == "₹450.00"

img = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".images :nth-child(1) :nth-child(1)")) )
img.click()

close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="pp_close"]')) )
close.click()
driver.quit()