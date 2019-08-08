import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("https://jqueryui.com/draggable/#sortable")

driver.maximize_window()
driver.implicitly_wait(10)
driver.switch_to.frame(driver.find_element_by_css_selector(".demo-frame"))
source =driver.find_element_by_id('draggable')
target =driver.find_element_by_css_selector("body:nth-child(2) ul.ui-sortable:nth-child(2) > li.ui-state-default.ui-sortable-handle:nth-child(4)")

mouse = ActionChains(driver).drag_and_drop(source,target)
mouse.perform()

time.sleep(5)