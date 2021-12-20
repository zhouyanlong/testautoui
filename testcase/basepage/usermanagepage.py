from selenium.webdriver.common.by import By
from common.page import Page
class UserManagePage(Page):
    #系统设置
    syssetting=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/div')
    #用户管理
    usermanage = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/ul/a[3]/li')
    def syssetting_page(self):
        return self.find_element(*self.syssetting).click()
    def usermanage_page(self):
        return self.find_element(*self.usermanage).click()