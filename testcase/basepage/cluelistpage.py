from selenium.webdriver.common.by import By
from commom.page import Page
from commom.readexcel import ReadExcel
testdata=ReadExcel().read_data("线索中心")
#线索列表page
class ClueListPage(Page):
    #线索中心btn
    cluecenter=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/div/span')
    #线索列表btn
    cluelist=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/ul/a[1]/li')
    #最近30天btn
    last30=(By.XPATH,'//*[@id="appMain"]/div/div/form/div[1]/div/div/div/div/div[1]/label[4]/span')
    #自定义时间框btn
    definetime=(By.XPATH,'//*[@id="appMain"]/div/div/form/div[1]/div/div/div/div/div[2]/input[1]')
    #线索idbtn
    clueid=(By.XPATH,'//*[@id="appMain"]/div/div/form/div[2]/div/div/div/input')
    #查询btn
    seach=(By.XPATH, '//*[@id="appMain"]/div/div/form/span/button[1]/span')
    #下载btn
    duwnload=(By.XPATH, '//*[@id="appMain"]/div/div/form/span/button[1]/span')
    #详情btn
    detail=(By.XPATH, '//*[@id="appMain"]/div/div/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[20]/div/div/button/span')
    def cluecenter_page(self):
        return Page(self.driver).find_element(*self.cluecenter).click()
    #线索列表btn
    def cluelist_page(self):
        return Page(self.driver).find_element(*self.cluelist).click()
    #最近30天按钮
    def last30_btn(self):
        return Page(self.driver).find_element(*self.last30).click()
    #自定义时间框
    def definetime_btn(self):
        return Page(self.driver).find_element(*self.definetime).click()
    #线索id查询按钮
    def clueid_btn(self):
        return Page(self.driver).find_element(*self.clueid).click()
    #查询按钮
    def seach_btn(self):
        return Page(self.driver).find_element(*self.seach).click()
    #下载按钮
    def duwnload_btn(self):
        return Page(self.driver).find_element(*self.duwnload).click()
    #详情按钮
    def detail_btn(self):
        return Page(self.driver).find_element(*self.detail).click()

