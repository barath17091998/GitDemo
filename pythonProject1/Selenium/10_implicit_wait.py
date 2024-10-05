import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# IMPLICIT WAIT: it is declared globally, so this implicit wait is applicable to all the selenium commands
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    # Chaining of web elements, parent web element with child web element
    # full XPATH = "//div[@class='products']/div/div/button"
    # Parent xpath results = "//div[@class='products']/div"
    # Child xpath results = "/div/button"
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)