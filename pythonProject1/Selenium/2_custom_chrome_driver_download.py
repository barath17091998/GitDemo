from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# METHOD 1 - MANUAL METHOD TO USE THE CHROME WEBDRIVER
# user needs to give the name of the executable with extension(.exe)
service_obj = Service("path_of_downloaded_webdriver_exe")
driver = webdriver.Chrome(service=service_obj)

# METHOD 2 - AUTOMATIC METHOD TO USE THE CHROME WEBDRIVER
driver=webdriver.chrome()
driver.get("https://www.youtube.com")

