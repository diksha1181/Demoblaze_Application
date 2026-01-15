from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

driver.get("https://demoblaze.com/")

elem = driver.find_element(By.ID,"signin2")
elem.send_keys(Keys.RETURN)

wait = WebDriverWait(driver,10)


elem1 = wait.until(EC.visibility_of_element_located((By.ID ,"sign-username")))

elem1 = driver.find_element(By.ID ,"sign-username")
elem1.send_keys("newwwwwwwwwwwwwwwwwwwww_user")

elem2 = driver.find_element(By.ID, "sign-password")
elem2.send_keys("userr_____________newwwwww")


signup = driver.find_element(By.CSS_SELECTOR, "#signInModal .btn.btn-primary")
signup.click()


time.sleep(2)

wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print("Alert Text", alert.text)

alert.accept()

driver.close()