from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("http://wikipedia.org")
driver.maximize_window()
driver.implicitly_wait(10)

element =driver.find_element_by_xpath("//a[@id='js-link-box-fr']")
hover = ActionChains(driver).move_to_element(element)
hover.perform()