import time
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Barath"
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
# Switching to alert mode from browser mode for respond the java script popup
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
# checking Barath is coming in the displayed popup text
assert name in alertText
alert.accept()
#alert.dismiss()

time.sleep(5)

