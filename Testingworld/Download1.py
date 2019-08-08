from selenium import webdriver
import time

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
time.sleep(5)

#Download Textfile
driver.find_element_by_xpath("//textarea[@id='textbox']").send_keys("test")
time.sleep(5)

#Generate File button
driver.find_element_by_xpath("//button[@id='createTxt']").click()
time.sleep(2)

#Download File button
driver.find_element_by_xpath("//a[@id='link-to-download']").click()
time.sleep(2)

#Download PDF File
driver.find_element_by_xpath("//textarea[@id='pdfbox']").send_keys("Text")
time.sleep(3)

driver.find_element_by_xpath("//button[@id='createPdf']").click()
time.sleep(5)

#Download Filebutton
driver.find_element_by_xpath("//a[@id='pdf-link-to-download']").click()
time.sleep(2)


