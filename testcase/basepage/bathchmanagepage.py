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
    1查询不存在的批次名称:外呼批次名称、查询
2查询存在的批次名称：外呼批次名称、查询
3查询批次状态暂停中：批次状态下拉、状态值（暂停）、查询
4查询批次状态进行中：批次状态下拉、状态值（进行）、查询
5查询批次状态已完成：批次状态下拉、状态值（完成）、查询
6查询批次状态已取消：批次状态下拉、状态值（取消）、查询
7查询批次状态等待中：批次状态下拉、状态值（等待）、查询
8创建批次：下一步、批次名称、话术策略下拉、话术策略、时效（clear）、时效（传值0）、线路分组下拉、线路分组、日期、确定
9暂停批次：选择序号1的数据、暂停、确定
10执行批次：选择序号1的数据、执行、确定
11取消批次：选择序号1的数据、取消、确定
12下载外呼明细：下载外呼明细、确定
13批次详情查询存在的线索id：序号1的批次详情、线索id、确定
14批次详情查询不存在的线索id：序号1的批次详情、线索id、确定
15批次详情查询存在的电话：序号1的批次详情、号码、确定
16批次详情查询不存在的电话：序号1的批次详情、号码、确定
17批次详情查询存在的姓名：序号1的批次详情、姓名、确定
18批次详情查询不存在的姓名：序号1的批次详情、姓名、确定
19批次详情查询状态命中停呼：序号1的批次详情、状态下拉、状态（停呼）、确定
20批次详情查询状态去重：序号1的批次详情、状态下拉、状态（去重）、确定
21批次详情查询状态正常：序号1的批次详情、状态下拉、状态（正常）、确定
    """
