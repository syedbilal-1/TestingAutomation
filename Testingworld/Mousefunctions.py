from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("https://www.thetestingworld.com/")
driver.maximize_window()
driver.implicitly_wait(10)

act = ActionChains(driver)

#click operation
act.click().perform()
act.click(driver.find_element_by_xpath("//a[contains(text(),'Registration')]")).perform()

#Context click
#act.context_click().perform()
#act.click(driver.find_element_by_xpath("//div[@class='ja-ss-item animate curr active']//img")).perform()

#Double click
#act.double_click().perform()
#act.click(driver.find_element_by_xpath("//div[@class='ja-ss-item animate curr active']//h3[contains(text(),'Selenium Training BY Industry Experts')]")).perform()

#Moving control to the required webelement
#act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'ABOUT US')]")).perform()


