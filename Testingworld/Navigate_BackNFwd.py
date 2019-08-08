from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://jqueryui.com/checkboxradio/')
time.sleep(3)

ele =driver.find_element_by_xpath("//a[contains(text(),'Themes')]")
time.sleep(4)
ele.click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()