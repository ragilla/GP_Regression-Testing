from selenium.webdriver import Chrome
from LibraryFiles import ConfigReader

def startBrowser():
    global driver
    chrome = "../Driver/chromedriver.exe"
    driver = Chrome(executable_path=chrome)
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))

    driver.maximize_window()
    return driver

def closeBrowse():
    driver.quit()