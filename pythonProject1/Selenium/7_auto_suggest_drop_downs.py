import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")

# Finding the object and giving "ind" in the box
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# .text method cannot be used for auto suggest
#print(driver.find_element(By.ID,"autosuggest").text)

# get_atttribute method is used for verification using  (i) print method
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India")
# 0r get_atttribute method is used for verification using (ii) assert method
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"


