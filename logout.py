from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()

driver.get("https://demoblaze.com/")

driver.maximize_window()

wait = WebDriverWait(driver,10)


elem = driver.find_element(By.ID,"login2")
elem.send_keys(Keys.RETURN)

wait.until(EC.visibility_of_element_located((By.ID ,"loginusername")))

elem1 = driver.find_element(By.ID ,"loginusername")
elem1.send_keys("newwwwwwwwwwwwwwwwwwwww_user")



elem2 = driver.find_element(By.ID, "loginpassword")
elem2.send_keys("userr_____________newwwwww")


login = driver.find_element(By.CSS_SELECTOR, "#logInModal .btn.btn-primary")
login.click()


time.sleep(2)

Success=driver.find_element(By.ID , "nameofuser")
wait.until(EC.visibility_of_element_located((By.ID , "nameofuser")))

print(Success.text)

print("User wants to log out ")


logout = driver.find_element(By.CSS_SELECTOR,"#logout2")
logout.click()

time.sleep(2)

driver.find_element(By.ID , "narvbarx")
wait.until(EC.visibility_of_element_located((By.ID , "narvbarx")))


print("Log out Successful")