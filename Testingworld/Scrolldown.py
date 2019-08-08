from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("https://www.thetestingworld.com/testings/")
driver.maximize_window()
time.sleep(2)

eln = driver.find_element_by_tag_name('html')
eln.send_keys(Keys.PAGE_DOWN)
time.sleep(4)

eln.send_Keys(Keys.HOME)

# driver.quit()

