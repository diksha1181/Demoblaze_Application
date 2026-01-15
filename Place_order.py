from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoblaze.com/")


# Adding Phones to the cart

e1 = driver.find_element(By.LINK_TEXT, "Phones").click()
print("Clicked Phones Category" )
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Nokia lumia 1520']"))).click()
print("Chosen the Phone")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.btn-lg"))).click()

wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print(alert.text)
alert.accept()


enter = driver.find_element(By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link']")
enter.send_keys(Keys.RETURN)

# Adding Laptop to cart

e2 = driver.find_element(By.LINK_TEXT, "Laptops").click()
print("Clicked Laptops Category" )


wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='MacBook Pro']"))).click()

print("Chosen the Laptop")

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.btn-lg"))).click()


wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print(alert.text)

alert.accept()


# Viewing items in the cart

e3 = driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()
print("Viewing items in the cart")


time.sleep(6)
wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"col-lg-8")))

print("Printing the details of items in the cart")

elements = driver.find_elements(By.CLASS_NAME,"col-lg-8")

for element in elements :
  print(element.text)



e4 = driver.find_elements(By.CLASS_NAME,"col-lg-1")
for text in e4 :
  price = driver.find_element(By.CLASS_NAME,"panel-title")
  print("Total Price is : " , price.text)


wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success"))).click()
print("Place order clicked ")
