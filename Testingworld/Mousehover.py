from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("https://www.amazon.com/")
driver.maximize_window()

driver.implicitly_wait(10)

ele =driver.find_element_by_xpath("//span[@class='nav-line-2'][contains(text(),'Account & Lists')]")
hover = ActionChains(driver).move_to_element(ele)
hover.perform()

driver.implicitly_wait(20)

#driver.quit()