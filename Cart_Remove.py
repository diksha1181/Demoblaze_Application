from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoblaze.com/")


e1 = driver.find_element(By.LINK_TEXT, "Laptops").click()
print("Clicked Laptops Category" )


wait = WebDriverWait(driver, 10)

e2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='MacBook Pro']"))).click()

print("Chosen the Laptop")


e2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.btn-lg"))).click()


wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print(alert.text)

alert.accept()

e3 = driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
print("Viewing items in the cart")


time.sleep(6)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"col-lg-8")))

print("Printing the details of items in the cart")

elements = driver.find_elements(By.CLASS_NAME,"col-lg-8")

for element in elements :
  print(element.text)

print("Removing the item from the cart")


e4 = driver.find_elements(By.CLASS_NAME,"col-lg-8")

for element in e4:
  wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Delete"))).click()

print("Item is Removed from the cart ")


time.sleep(6)



driver.close()

