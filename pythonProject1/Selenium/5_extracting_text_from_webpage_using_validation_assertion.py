import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("barathbas7@gmail.com")
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Bhuna@1974")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Bhuna@1974")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Generating X-path based on the text in the webpage
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()


time.sleep(7)