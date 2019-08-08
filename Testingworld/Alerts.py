from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element_by_tag_name("cusid").send_Keys("56432")
driver.find_element_by_tag_name("submit").click()

driver.switch_to.alert.accept()
time.sleep(2)
driver.switch_to.alert.accept()

# driver.quit()
