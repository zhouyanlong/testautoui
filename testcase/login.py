from selenium import webdriver
from test import sleep
from testcase.basepage.loginpage import LoginPage
class Login():
    #登陆营销系统，返回driver
    def login_market(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(LoginPage(self.driver).get_url())
        LoginPage(self.driver).account_btn("zhouyanlong")
        LoginPage(self.driver).password_btn("Aa123456.")
        LoginPage(self.driver).login_btn()
        LoginPage(self.driver).market_btn()
        sleep(1)
        return self.driver