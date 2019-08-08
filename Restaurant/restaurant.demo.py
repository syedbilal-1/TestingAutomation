from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome("C:\\Users\\Bilal\\PycharmProjects\\TestAutomation\\Drivers\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("https://www.demo.iscripts.com/netmenus/mrml/vendor")
driver.maximize_window()

driver.implicitly_wait(20)
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("restaurant@netmenus.com")
time.sleep(1)
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("restaurant")
time.sleep(1)
driver.find_element_by_xpath("//input[@class='login_btn']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='venue_name']").send_keys("SYED RESTAURANT")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='venue_alias']").send_keys("www.syedrestaurant.com")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='autocomplete_location']").send_keys("NEAR central BUS STAND,GULBARGA")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='zip']").send_keys("585102")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='phone']").send_keys("9988776600")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='site_url']").send_keys("http://syed.com")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='store_manager']").send_keys("SYED BILAL")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='store_manager_email']").send_keys("syedrestaurant@gmail.com")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='store_manager_password']").send_keys("syedres123")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='delivery_fee']").send_keys("100")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='delivery_time']").send_keys("15")
# time.sleep(1)
# driver.find_element_by_xpath("//textarea[@id='venue_description']").send_keys("SYED RESTAURANT provides best quality food with fast delivery")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='token-input-cuisine']").send_keys("Italian")
# time.sleep(15)
# act = ActionChains(driver)
# act.send_keys(Keys.ENTER).perform()
# time.sleep(5)
# driver.find_element_by_xpath("//input[@id='min_order_amount']").send_keys("1000")
# time.sleep(1)
# driver.find_element_by_xpath("//input[@id='sales_tax']").send_keys("100")
# time.sleep(1)
# driver.find_element_by_id("takout").click()
# time.sleep(5)
# driver.find_element_by_xpath("//input[@name='file_photo1']").send_keys('‪‪C:\\Users\\Bilal\\Desktop\\rest.jpg')
# time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'SYED RESTAURANT - 07 Aug,2019')]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='btnSave']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='addmore_class jQAddServiceFn']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='class_name']").send_keys("Dosa")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='end_time']").click()
time.sleep(6)
driver.find_element_by_link_text("//li[contains(text(),'07:30 am')]")
time.sleep(5)
driver.find_element_by_xpath("//input[@id='end_time']").click()
time.sleep(6)
driver.find_element_by_link_text("//body[@class='classes']//div[@class='row']//div[@class='row']//div[@class='row']//div[@class='row']//div[@class='row']//div[2]//div[1]//span[1]//ul[1]//li[28]")
time.sleep(5)
driver.find_element_by_xpath("//input[@name='add']").click()
time.sleep(5)
driver.find_element_by_xpath("//input[@name='Submit']").click()
time.sleep(10)
driver.find_element_by_link_text("Add Food Item").click()
time.sleep(2)
driver.find_element_by_link_text("//input[@id='activity_name']").send_keys("Noodles")
time.sleep(5)
driver.find_element_by_link_text("//input[@id='fooditem_photo1']").send_keys('‪C:\\Users\\Bilal\\Desktop\\img.jpeg')
time.sleep(10)
driver.find_element_by_link_text("//textarea[contains(@placeholder,'Food Item Description')]").send_keys("One of the best chinese food you have ever eaten")
time.sleep(5)
driver.find_element_by_link_text("//input[@id='price_option']").click()
time.sleep(6)
driver.find_element_by_link_text("//input[@id='activity_price']").send_keys("600")
time.sleep(2)
driver.find_element_by_link_text("//div[11]//ul[1]").send_keys("Noodles")
time.sleep(15)
driver.find_element_by_link_text("//input[@name='Submit']").click()