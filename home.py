import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
sleep_timeout = 3
Selenium_Ruby = driver.find_element_by_css_selector("[id='text-22-sub_row_1-0-2-0-0'] .woocommerce-LoopProduct-link").click()
REVIEW = driver.find_element_by_css_selector('[href="#tab-reviews"]').click()
star = driver.find_element_by_css_selector('[class="star-5"]').click()
Review_texst = driver.find_element_by_id("comment")
Review_texst.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("Any")
email = driver.find_element_by_id("email")
email.send_keys("vchera2021@mail.ru")
submit = driver.find_element_by_id("submit").click()
driver.quit()