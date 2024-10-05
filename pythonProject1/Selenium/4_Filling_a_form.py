import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")

# Methods to Identify the particular box "email" and fill it with email ID
driver.find_element(By.NAME,"email").send_keys("barathbas7@gmail.com")
# Methods to Identify the particular box "Password" and fill it with password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345678")
# Method to click on the checkbox
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH ==>  //tagname[@attribute=’value’] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# CSS Selector - tagname[attribute='value'] -> //input[@type='submit']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Barath")

# To grab the apllication successful message in webpage
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# Assertion to check the word success in the message after successful completion
assert "Success" in message

# To click on the radio button "student"
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Indexes in X-path to identify the particular element when multiple elements are identified with same name
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")

# To clear the edit box
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

time.sleep(3)