from selenium.webdriver.common.by import By
from common.page import Page
class StopBlacklistPage(Page):
    #系统设置
    syssetting=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/div')
    #停呼黑名单
    stopblacklist = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[6]/ul/a[2]/li')
    def syssetting_page(self):
        return self.find_element(*self.syssetting).click()
    def stopblacklist_page(self):
        return self.find_element(*self.stopblacklist).click()