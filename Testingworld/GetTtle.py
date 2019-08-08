from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("https://www.thetestingworld.com/testings/")
driver.maximize_window()
time.sleep(1)

#Fetching Title
print("Title of page is "+ driver.title)


#Fetch URL of page
print("page url is "+ driver.current_url)


#Fetch complete page HTML
print("**************************************************************************")
print(driver.page_source)
