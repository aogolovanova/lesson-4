import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(chrome_options=options)
driver.get("http://practice.automationtesting.in/")

shop = driver.find_element_by_id("menu-item-40").click()
sleep_timeout=60
driver.execute_script("window.scrollBy(0, 300);")

WebApp = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
WebApp.click()
sleep_timeout=60

JS = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]')
JS.click()
sleep_timeout=60

basket = driver.find_element_by_css_selector('.wpmenucartli>a')
basket.click()
sleep_timeout=60

delete = driver.find_element_by_css_selector('[data-product_id="182"]').click()
sleep_timeout=60

Undo = driver.find_element_by_css_selector(".woocommerce-message>a").click()
sleep_timeout=60

Quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]').clear()
Quantity = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
Quantity.send_keys("3")

UPDATE = driver.find_element_by_css_selector('.actions>[type="submit"]').click()
sleep_timeout=60

JS3 = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
JS3_value = JS3.get_attribute("value")
assert JS3_value == ("3")
sleep_timeout =90
apply = driver.find_element_by_css_selector('[name="apply_coupon"]')
apply.click()
sleep_timeout=60
texst = WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-error>li'), "Please enter a coupon code."))
driver.quit()