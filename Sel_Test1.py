'''Write code to open Chrome, navigate to Google, search for “Selenium Python” and print the titles of the first 5 results.'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://google.com")
driver.maximize_window()
search = (driver.find_element(By.XPATH, "//textarea[@name='q']"))
search.send_keys('Selenium Python')
search.send_keys(Keys.ENTER)
time.sleep(10)
