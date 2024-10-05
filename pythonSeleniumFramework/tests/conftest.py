import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.rahulshettyacademy.com/client")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()