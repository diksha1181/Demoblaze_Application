from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoblaze.com/")

time.sleep(3)

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))


for link in links :
 print(link.text)
 

time.sleep(2)
driver.close()

