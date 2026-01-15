from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoblaze.com/")

wait = WebDriverWait(driver,10)

time.sleep(3)

e1 = driver.find_element(By.LINK_TEXT, "Laptops").click()
print("Clicked Laptops Category" )

time.sleep(3)

e2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='MacBook Pro']"))).click()

print("Chosen the Laptop")


time.sleep(3)

e2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.btn-lg"))).click()


wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print(alert.text)

alert.accept()


driver.close()

