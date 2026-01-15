from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoblaze.com/")

elem = driver.find_element(By.XPATH,"//a[normalize-space()='About us']")
elem.send_keys(Keys.RETURN)

time.sleep(3)

wait = WebDriverWait(driver,10)
wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='videoModal']//button[@type='button'][normalize-space()='Close']"))).click()



print ("Page closes Sucessfully")



