from common.page import Page
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
    """
    excel中元素属性说明：
    1查询存在的字段名称,第一个元素为查询字段名称btn，第二个为查询btn
    2查询不存在的字段名称，第一个元素为查询字段名称btn，第二个为查询btn
    3查询文本字段类型，第一个元素为查询文本字段类型下拉，第二个元素为文本，第三个为查询btn
    4查询金额字段类型，第一个元素为查询文本字段类型下拉，第二个元素为金额，第三个为查询btn
    5查询日期字段类型，第一个元素为查询文本字段类型下拉，第二个元素为日期，第三个为查询btn
    6查询是否必填是，第一个元素为查询必填字段类型下拉，第二个元素为是，第三个为查询btn
    7查询是否必填否，第一个元素为查询必填字段类型下拉，第二个元素为是，第三个为查询btn
    8新增名称为空，第一个元素为新增btn，第二个元素确定
    9新增编码为空，第一个元素为新增btn，第二个元素确定
    10新增数据，第一个元素为新增btn，后面一次为元素名称、编码、备注、确定
    11查看总计，元素为查看总计btn
    12编辑数据，第一个元素为 跳转至第三页，第二个为编辑btn，第三个为确定
    13删除第一个元素为 跳转至第三页，第二个为删除btn，第三个为确定
    """

