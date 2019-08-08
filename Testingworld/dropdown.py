
from selenium.webdriver.support.select import Select

from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.theTestingWorld.com/testings")
driver.maximize_window()
driver.find_element_by_xpath("//input[@placeholder='myusername']").send_keys("SyedSammer")
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) > input.field:nth-child(5)").send_keys("sammer123@gmail.com")
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) > input.field:nth-child(7)").send_keys("samer123")
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) > input.field:nth-child(9)").send_keys("sammer123")
driver.find_element_by_xpath("//input[@id='datepicker']").send_keys("21/10/1996")
driver.find_element_by_xpath("//input[@placeholder='Phone']").send_keys("9988776655")
driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys("HighcourtGulbarga")
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) > input:nth-child(16)").Click_keys("Home")
driver.find_element_by_xpath("//select[@name='sex']").value_of_css_property("1")
driver.find_element_by_xpath("//select[@id='countryId']").send_keys("India")
driver.find_element_by_css_selector("#stateId").send_keys("Karnataka")
driver.find_element_by_css_selector("#cityId").send_keys("Gulbarga")
driver.find_element_by_css_selector("div.container:nth-child(7) section.tabblue.center ul.tabs.blue li:nth-child(1) div.tab-content:nth-child(3) form:nth-child(3) > input:nth-child(23)").send_keys(585103)




driver.quit()
