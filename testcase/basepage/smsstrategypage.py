from common.page import Page
from selenium.webdriver.common.by import By
class SmsStrategyPage(Page):
    #外呼管理
    callmanage=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/div')
    #短信策略
    smsstrategy=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[3]/ul/a[2]/li')

    def callmanage_page(self):
        return Page(self.driver).find_element(*self.callmanage).click()
    def smsstrategy_page(self):
        return Page(self.driver).find_element(*self.smsstrategy).click()
    """"
    excel中的元素:
1	短信策略	查询存在的策略名称：策略名称、查询
2	短信策略	查询不存在的策略名称：策略名称、查询
3	短信策略	查询短信类型：短信类型下拉、类型值（挂机短信）、查询
4	短信策略	查询状态启用：状态下拉、状态值（启用）、查询
5	短信策略	查询状态禁用：状态下拉、状态值（禁用）、查询
6	短信策略	查询创建时间无：开始时间、结束时间、查询
7	短信策略	查询创建时间有：开始时间、结束时间、查询
8	短信策略	新增名称为空：新增、确定
9	短信策略	新增模板为空：新增、确定
10	短信策略	新增名称已存在：新增、名称、模板下拉、模板、确定
11	短信策略	新增变量名称为空：新增、新增变量、确定
12	短信策略	新增变量条件为空：新增、新增变量、确定
13	短信策略	新增变量表达式为空：新增、新增变量、确定
14	短信策略	删除变量：新增、新增变量、删除变量
15	短信策略	新增逻辑符号为空：新增、新增变量1、新增变量2、变量1名称下拉、变量1名称、变量2名称下拉、变量2、确定
16	短信策略	正常新增：新增、名称、模板下拉、模板、确定
17	短信策略	编辑：编辑、确定
18	短信策略	删除：删除、确定

    """