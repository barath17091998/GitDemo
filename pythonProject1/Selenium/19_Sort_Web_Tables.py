from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/offers")


# STEP 1 - CLICK ON COLOUMN HEADER
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# STEP 2 - COLLECT ALL VEGGIE NAMES (BROWSER SORTED VEGGIELIST)
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortedVeggies.append(ele.text)

# TAKE THE COPY OF THE LIST BEFORE SORTING
originalBrowserSortedList = browserSortedVeggies.copy()  # copy or slice method to make copy of list

# STEP 3 - SORT THE BROWSER SORTED VEGGIELIST ==> (NEW SORTED LIST)
browserSortedVeggies.sort()

assert browserSortedVeggies == originalBrowserSortedList



