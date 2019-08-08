from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://www.google.com/')

driver.implicitly_wait(1)
element =driver.find_element_by_xpath("//img[@id='hplogo']").click()
driver.implicitly_wait(10)

act =ActionChains(driver)
act.double_click(element).perform()


#http://only-testing-blog-blogspot.in/2014/09/selectable.html