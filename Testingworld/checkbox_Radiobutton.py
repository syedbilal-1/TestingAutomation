import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.get("https://jqueryui.com/checkboxradio/")
driver.maximize_window()
driver.set_page_load_timeout(10)

#frame
driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))
#Radio button
driver.find_element_by_xpath("//label[contains(text(),'New York')]").click()
time.sleep(1)


#Checkbox
driver.find_element_by_xpath("//label[contains(text(),'2 Star')]").click()
time.sleep(1)

driver.find_element_by_xpath("//label[contains(text(),'3 Star')]").click()
time.sleep(1)

driver.find_element_by_xpath("//label[contains(text(),'4 Star')]").click()
time.sleep(1)

driver.find_element_by_xpath("//label[contains(text(),'5 Star')]").click()
time.sleep(1)