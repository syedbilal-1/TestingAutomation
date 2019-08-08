import time
import os
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/upload")
time.sleep(5)
driver.find_element_by_id("file-upload").send_keys('C:\\Users\\Bilal\\Desktop\\Python_dwnds\\3.jpg')
time.sleep(5)
driver.find_element_by_id("file-submit").click()

time.sleep(3)
