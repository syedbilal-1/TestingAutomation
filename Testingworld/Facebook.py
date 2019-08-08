
from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com")
driver.maximize_window()

driver.implicitly_wait(20)

driver.find_element_by_id("u_0_l").send_keys("Amair")
time.sleep(1)
driver.find_element_by_name("lastname").send_keys("Shah")
time.sleep(1)
driver.find_element_by_id("u_0_q").send_keys("amair.123khan@gmail.com")
time.sleep(1)
driver.find_element_by_id("u_0_t").send_keys("amair.123khan@gmail.com")
time.sleep(1)
driver.find_element_by_id("u_0_x").send_keys("amair.123")
time.sleep(1)
driver.find_element_by_id("day").send_keys("12")
time.sleep(1)
driver.find_element_by_id("month").send_keys("October")
time.sleep(1)
driver.find_element_by_id("year").send_keys("1995")
time.sleep(1)
driver.find_element_by_id("u_0_11").click()
time.sleep(1)
driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()
time.sleep(1)
driver.find_element_by_id("u_0_15").click()
time.sleep(1)

driver.quit()



driver.quit()

