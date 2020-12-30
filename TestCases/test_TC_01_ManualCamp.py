from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from BaseFiles import InitiateDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.expected_conditions as EC
from LibraryFiles import ConfigReader
from Pages.Corp_Login import Corporate_Login

driver = InitiateDriver.startBrowser()
corp_login_dtls = Corporate_Login(driver)
corp_login_dtls.enter_username('LowBal_VMISDN')
corp_login_dtls.enter_password('Boss$007')

#ConfigReader.fetchElementLocators('Manual_Campaign','User_Name')
#ConfigReader.fetchElementLocators('Manual_Campaign','Pass_word')

driver.get(ConfigReader.readConfigData('Details','Application_URL'))

driver.implicitly_wait(100)
driver.find_element_by_xpath("//button[@type='button']").click()
driver.find_element_by_xpath("//div[@class='collapse navbar-collapse sidenav']/ul[2]/li[3]/a/p[contains(text(),'Create Campaign')]").click()
driver.find_element_by_name("campaign_name").send_keys("Testing_Manual_Campaign")

sel1 = Select(driver.find_element_by_name("clitype"))
sel1.select_by_visible_text("Non-Masking")

driver.find_element_by_xpath("//textarea[@name='smsmsg']").send_keys("Sample Manual campaign creation")
driver.implicitly_wait(100)
driver.find_element_by_xpath("//*[@id='create-form']/section[4]/div/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div/div/ul/li[4]/label/span").click()
driver.find_element_by_xpath("//div[@class='form-group']/textarea[@name='manualmsisdns']").send_keys("01711176542,01711276542,01711376542,01711476542,01711576542")
driver.implicitly_wait(100)
driver.find_element_by_xpath("//div[@class='btn_cls ']/button[@type='submit']").click()

driver.implicitly_wait(100)
try:
    driver.find_element_by_xpath("//*[@id='create-form']/section[6]/div/div/div/div/button[2]").click()
        #element = WebDriverWait(driver, 100).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='two_btn ng-star-inserted']/button[contains(text(),'SUBMIT')]")))
        #element.click()
finally:
    driver = InitiateDriver.closeBrowse()

















