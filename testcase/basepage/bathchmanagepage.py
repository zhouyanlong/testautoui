from commom.page import Page
from selenium.webdriver.common.by import By
class BatchManagePage(Page):
    #外呼管理
    callmanage=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div/span')
    #批次管理
    batchmanage = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[1]/li/span')
    #创建批次
    createbatch=(By.XPATH, '//*[@id="appMain"]/div/div/div[2]/div[1]/div[1]/button[1]/span')
    #上传文件的btn，span定位不到
    uploadfile=(By.XPATH,'//*[@id="appMain"]/div/div/div/div[2]/form/div[2]/div/div/div/div[1]/button')
    #确定
    ok=[By.XPATH,'//*[@id="appMain"]/div/div/div/div[3]/div[2]/button[2]/span']
    def callmanage_page(self):
        return Page(self.driver).find_element(*self.callmanage).click()
    def batchmanage_page(self):
        return Page(self.driver).find_element(*self.batchmanage).click()
    def createbatch_page(self):
        return Page(self.driver).find_element(*self.createbatch).click()
    def uploadfile_page(self):
        return Page(self.driver).find_element(*self.uploadfile).click()

    """excel中的元素：
    
    """
