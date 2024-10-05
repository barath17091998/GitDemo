import time
from selenium import webdriver

# Headless method - the browser window wouldn't be visible
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
# Ignore webpage certificate errors
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# "execute_script" method is to execute the javascript method,
# inside parenthesis of "execute_script" method, the javascript command is provided
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
# "get_screenshot_as_file" method is to take screenshot of the page
driver.get_screenshot_as_file("bottom_of_page.png")

time.sleep(4)

