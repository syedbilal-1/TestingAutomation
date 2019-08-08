from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("https://www.thetestingworld.com/testings/")

driver.maximize_window()
driver.implicitly_wait(20)

element =driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
#act.send_keys(keys.TAB).perform()

#act.send_keys(keys.CONTROL).send_keys("a").perform()
#act.send_keys(keys.SPACE).perform()
#act.send_keys(keys.ENTER).perform()