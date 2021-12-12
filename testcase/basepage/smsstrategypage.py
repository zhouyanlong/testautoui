from commom.page import Page
from selenium.webdriver.common.by import By
class SmsStrategyPage(Page):
    #外呼管理
    callmanage=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div/span')
    #短信策略
    smsstrategy=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[2]/li/span')

    def callmanage_page(self):
        return Page(self.driver).find_element(*self.callmanage).click()
    def smsstrategy_page(self):
        return Page(self.driver).find_element(*self.smsstrategy).click()