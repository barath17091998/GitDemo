import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Method to find the checkbox when attributes are not there
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

# RADIO BUTTONS
radiobuttons = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# Clicking Show & hide buttons
assert driver.find_element(By.ID,"displayed-text").is_displayed()
# Clicking the hide button
driver.find_element(By.ID,"hide-textbox").click()
# Checking the show text is hidden
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
# Clicking the show button
driver.find_element(By.ID,"show-textbox").click()
# Checking the show text is visible
assert driver.find_element(By.ID,"displayed-text").is_displayed()

time.sleep(4)