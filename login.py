from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoblaze.com/")

wait = WebDriverWait(driver,10)


elem = driver.find_element(By.ID,"login2")
elem.send_keys(Keys.RETURN)


elem1 = wait.until(EC.visibility_of_element_located((By.ID ,"loginusername")))

elem1 = driver.find_element(By.ID ,"loginusername")
elem1.send_keys("newwwwwwwwwwwwwwwwwwwww_user")


elem2 = wait.until(EC.visibility_of_element_located((By.ID, "loginpassword")))

elem2 = driver.find_element(By.ID, "loginpassword")
elem2.send_keys("userr_____________newwwwww")

time.sleep(3)
login = driver.find_element(By.CSS_SELECTOR, "#logInModal .btn.btn-primary")
login.click()


time.sleep(6)

Success=driver.find_element(By.ID , "nameofuser")
wait.until(EC.visibility_of_element_located((By.ID , "nameofuser")))

print(Success.text)
driver.close()

