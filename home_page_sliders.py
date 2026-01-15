from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver,10)


driver.get("https://demoblaze.com/")
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME,"carousel-item")
print("No. of Sliders on Home Page are " ,len(sliders))

print("Current Phone Slider1 Appears")


wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"carousel-control-next-icon"))).click()
print("Phone Slider2 Appears on clicking next button")
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"carousel-control-next-icon"))).click()
print("Laptop Slider3 Appears on clicking next button ")      
time.sleep(3)


wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"carousel-control-prev-icon"))).click()
print("Phone Slider1 Appears on clicking previous button")
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"carousel-control-prev-icon"))).click()
print("Phone Slider2 Appears on clicking previous button")      
time.sleep(3)


driver.close()
