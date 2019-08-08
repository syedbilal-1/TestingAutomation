from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)

driver.get("http://lms.latitudelearning.com")
driver.maximize_window()
driver.implicitly_wait(20)

driver.get_screenshot_as_file("E:\\screenshot\\sb.png")

element =driver.find_element_by_id('ctlTemplate_regMainBody_ctlLogin_sID').send_keys("Syed Bilal")
element =driver.find_element_by_name("ctlTemplate$regMainBody$ctlLogin$sPassword").send_keys("minds123")
element =driver.find_element_by_id('ctlTemplate_regMainBody_ctlLogin_cmdLogin').click()

driver.get_screenshot_as_file("E:\\screenshot\\sb.png")