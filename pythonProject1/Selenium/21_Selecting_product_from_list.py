# NOTE: This

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from urllib3.util import wait

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(10)

# //a[contains(@href,'shop')]  --> XPATH used with partial value by using 'contains'
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text  # div/h4/a traversing from //div[@class='card h-100']
    if productName == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR,"a[class*='btn-primary']").click()
time.sleep(30)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

# HANDLING DYNAMIC DROP DOWNS
driver.find_element(By.ID,"country").send_keys("ind")
# Wait till the INDIA is diaplayed after entered the "ind" in the checkbox
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in successText
