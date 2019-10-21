from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import pytest



@pytest.fixture(scope="module")  # Comment this block of code while running on local
def driver():  # To run on linux server 

    driver = webdriver.Chrome("../drivers/chrome/chromedriver.exe") #add .exe extension on windows
    # browser = webdriver.Firefox()
    driver.maximize_window()
    
    yield driver 
    driver.back() 
    driver.quit()


@pytest.fixture(scope="module")
def base_url_live():
    base_url = "http://www.sjinnovation.com"
    return base_url



