from common.page import Page
from selenium.webdriver.common.by import By
class LoginPage(Page):
    account = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/input')
    password = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[2]/div/div[2]/input')
    login = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/button/span')
    market = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div')
    url = "https://ai.zhilingsd.com/#/login"
    def account_btn(self,keys):
        return self.find_element(*self.account).send_keys(keys)
    def password_btn(self,keys):
        return self.find_element(*self.password).send_keys(keys)
    def login_btn(self):
        return self.find_element(*self.login).click()
    def market_btn(self):
        return self.find_element(*self.market).click()
    def get_url(self):
        return self.url