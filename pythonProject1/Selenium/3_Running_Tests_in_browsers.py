import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.google.in")
# METHOD "MAXIMIZE_WINDOW" TO MAXIMIZE THE BROWSER WINDOW
driver.maximize_window()
# METHOD "TITLE" TO GRAB THE TITLE OF THE WEBPAGE
print(driver.title)
# METHOD "CURRENT_URL" TO GET THE CURRENT URL OF THE WEBPAGE
print(driver.current_url)

time.sleep(3)

