from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT,"Click Here").click()
# window_handles --> gives the list of all the tab names opened in the chrome at that particular session
windows_opened = driver.window_handles
# 0 index is parent window and index 1 is child window
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
driver.close()  # To close the child window

driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text

