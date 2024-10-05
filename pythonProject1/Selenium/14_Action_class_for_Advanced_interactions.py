from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()

action = ActionChains(driver)

#           METHODS IN ACTION CLASS
#action.double_click(driver.find_element(By,))
#action.context_click()                              ==> right click
#action.drag_and_drop()

action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
# perform method at the end to execute the particular action without any fail

#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

