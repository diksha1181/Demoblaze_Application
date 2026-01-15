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



e1 = driver.find_element(By.LINK_TEXT, "Monitors").click()
print("Clicked Monitors Category" )


wait = WebDriverWait(driver, 10)

e2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Apple monitor 24']"))).click()

print("Chosen the Monitor" )


e2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success.btn-lg"))).click()


wait.until(EC.alert_is_present())
alert= driver.switch_to.alert
print(alert.text)

alert.accept()




e3 = driver.find_element(By.XPATH, "//a[normalize-space()='Cart']").click()


time.sleep(4) 

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-success"))).click()
print("Place order clicked ")


wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,"#orderModal")))
print("Fill Personal Details")
           
name = driver.find_element(By.ID,"name")
name.send_keys("Shruti")
name.send_keys(Keys.RETURN)

country = driver.find_element(By.ID,"country")
country.send_keys("INDIA")
country.send_keys(Keys.RETURN)

city = driver.find_element(By.ID,"city")
city.send_keys("Hisar")
city.send_keys(Keys.RETURN)

card = driver.find_element(By.ID,"card")
card.send_keys("duy764918HDFC-7tyhgh")
card.send_keys(Keys.RETURN)


month = driver.find_element(By.ID,"month")
month.send_keys("January")
month.send_keys(Keys.RETURN)

year = driver.find_element(By.ID,"year")
year.send_keys("2026")
year.send_keys(Keys.RETURN)


wait.until(EC.element_to_be_clickable((By.XPATH,"//button[normalize-space()='Purchase']"))).click()

print("Item Purchased")


Form = driver.find_elements(By.XPATH,"//div[contains(@class,'showSweetAlert visible')]")
for elem in Form:
       print(elem.text)



wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".confirm.btn.btn-lg.btn-primary"))).click()

driver.find_element(By.CSS_SELECTOR, "body")

print("Return to Home page ")


driver.close()














