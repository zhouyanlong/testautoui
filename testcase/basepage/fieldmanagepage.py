from commom.page import Page
from selenium.webdriver.common.by import By
#字段管理
class FieldManagePage(Page):
    # 线索中心btn
    cluecenterbtn = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/div/span')
    #字段管理btn
    fieldmanagebtn=(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/ul/a[2]/li/span')
    def cluecenter_page(self):
        return Page(self.driver).find_element(*self.cluecenterbtn).click()
    def fieldmanage_page(self):
        return Page(self.driver).find_element(*self.fieldmanagebtn).click()


