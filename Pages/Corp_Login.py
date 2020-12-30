
class Corporate_Login():
    def __init__(self,obj):
        global  driver
        driver = obj
    def enter_username(self,username):
        driver.find_element_by_xpath("//div[@class='user']/input[@name='Username']").send_keys(username)
    def enter_password(self,password):
        driver.find_element_by_xpath("//div[@class='pass ']/input[@id='password']").send_keys(password)