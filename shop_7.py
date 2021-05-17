import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
basket = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.wpmenucartli>a')))
basket.click()
sleep_timeout=60


PROCEED = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href="http://practice.automationtesting.in/checkout/"]')))
PROCEED.click()

First_Name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'billing_first_name')))
First_Name.send_keys("Any")

Last_Name = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'billing_last_name')))
Last_Name.send_keys("Star")

email = driver.find_element_by_id("billing_email")
email.send_keys("vchera2021@mail.ru")

Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys(+79025566777)
select = driver.find_element_by_css_selector(".select2-container.country_to_state.country_select>a :nth-child(3)>b").click()
Country = driver.find_element_by_id("s2id_autogen1_search")
Country.send_keys("Italy")
sleep_timeout=10
Italy = driver.find_element_by_css_selector('[class="select2-match"]').click()
sleep_timeout=10
Address = driver.find_element_by_id('billing_address_1')
Address.send_keys("Rome")
ZIP = driver.find_element_by_id('billing_postcode')
ZIP.send_keys("00119")
City = driver.find_element_by_id('billing_city')
City.send_keys("Roma")
select2 = driver.find_element_by_css_selector('.select2-container.state_select>a :nth-child(3)>b').click()
sleep_timeout=10
Province = driver.find_element_by_id('s2id_autogen2_search')
Province.send_keys("Roma")
Roma = driver.find_element_by_css_selector('[class="select2-match"]').click()
driver.execute_script("window.scrollBy(0, 600);")
sleep_timeout=10
Check_Payments = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id('place_order').click()
texst = WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))
Payment_Method  = WebDriverWait(driver, 60).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce>ul :nth-child(4)>strong'), "Check Payments"))
driver.quit()