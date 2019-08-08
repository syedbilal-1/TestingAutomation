from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {"download.default_directory":"‪‪C:\\Users\\Bilal\\Desktop\\Download"})

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("https://pypi.org/project/selenium/")

driver.maximize_window()
driver.implicitly_wait(10)


driver.find_element_by_xpath("//a[@id='files-tab']").click()


driver.find_element_by_xpath("//a[contains(text(),'selenium-3.141.0-py2.py3-none-any.whl')]").click()