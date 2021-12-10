from commom.page import Page
from selenium.webdriver.common.by import By
class BatchManagePage(Page):
    #外呼管理
    callmanage=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div/span')
    #批次管理
    batchmanage = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[1]/li/span')

    def callmanage_page(self):
        return Page(self.driver).find_element(*self.callmanage)
    def batchmanage_page(self):
        return Page(self.driver).find_element(*self.batchmanage)
    """excel中的元素：
    
    """