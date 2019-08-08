from selenium .webdriver.support.select import Select

from selenium import webdriver

import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.maximize_window()
time.sleep(1)
driver.quit()
