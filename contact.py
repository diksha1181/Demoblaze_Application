from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://demoblaze.com/")

elem = driver.find_element(By.XPATH,"//a[normalize-space()='Contact']")
elem.send_keys(Keys.RETURN)

wait = WebDriverWait(driver,10)


elem1 = wait.until(EC.visibility_of_element_located((By.ID ,"recipient-email")))

elem1 = driver.find_element(By.ID ,"recipient-email")
elem1.send_keys("newuser@gmail.com")

elem2 = driver.find_element(By.ID, "recipient-name")
elem2.send_keys("newwwwwwwwwwwwwwwwwwwww_user")

elem3 = driver.find_element(By.ID, "message-text")
elem3.send_keys("Do Fast Delivery of order")





send = driver.find_element(By.CSS_SELECTOR, "button[onclick='send()']")
send.click()


time.sleep(2)

wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print("Alert Text : ", alert.text)

alert.accept()

driver.close()