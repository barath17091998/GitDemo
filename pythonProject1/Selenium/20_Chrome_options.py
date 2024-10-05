from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")    # to open the browser in maximized way
chrome_options.add_argument("headless")     # without opening the window
chrome_options.add_argument("--ignore-certificate-erros")      # Ignore the SSL certificate errors of web browser

#driver = webdriver.Chrome(executable_path="C:\\Program Files\\chromedriver_win32\\chromedriver.exe",options=chrome_options)            # when u know the path of the web driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/offers")

print(driver.title)

