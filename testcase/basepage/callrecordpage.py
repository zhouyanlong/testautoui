from commom.page import Page
from selenium.webdriver.common.by import By
class CallRecordPage(Page):
    #记录中心
    recordcenter=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[4]/div')
    #呼出记录
    callrecord=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[4]/ul/a[1]/li')
    def recordcenter_page(self):
        return Page(self.driver).find_element(*self.recordcenter)
    def callrecord_page(self):
        return Page(self.driver).find_element(*self.callrecord)