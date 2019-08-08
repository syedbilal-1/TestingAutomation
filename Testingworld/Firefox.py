from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False
driver = webdriver.Firefox(capabilities=cap,  executable_path="C:\\Users\\Bilal\\PycharmProjects\\TestingAutomation\\Drivers\\geckodriver.exe")
driver.maximize_window()
time.sleep(10)


driver.get('http://google.com/')
time.sleep(5)
# driver.quit()

