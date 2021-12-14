from selenium.webdriver.common.by import By
from commom.page import Page
class UserManagePage(Page):
    #系统设置
    syssetting=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/div')
    #用户管理
    stopblacklist = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/ul/a[3]/li')
    def syssetting_page(self):
        return Page(self.driver).find_element(*self.syssetting).click()
    def stopblacklist_page(self):
        return Page(self.driver).find_element(*self.stopblacklist).click()