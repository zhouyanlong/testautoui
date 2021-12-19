import unittest,ddt
from common.myunit import MyUnit
from common.readexcel import ReadExcel
from common.mylog import Log
from time import sleep
from testcase.basepage.cluelistpage import ClueListPage
from common.page import Page
from common.shot import screenshot
#不可不导入By，否则执行eval函数会报错找不到By
from selenium.webdriver.common.by import By
testdata=ReadExcel().read_data("线索中心")
@ddt.ddt
class ClueList(MyUnit):
    @ddt.data(*testdata)
    #线索列表
    def test_xiansuoliebiao(self,testdata):
        Log.info(testdata)
        sleep(0.5)
        #点击线索中心
        ClueListPage(self.driver).cluecenter_page()
        #等待线索列表
        Page(self.driver).wait_until_presence(self.driver,ClueListPage(self.driver).cluelist)
        #点击线索列表
        ClueListPage(self.driver).cluelist_page()
        sleep(1)

        # 如果id大于8，则需要点击详情后操作
        if int(testdata["id"])>8:
            #点击最近30天后点击详情
            ClueListPage(self.driver).last30_btn()
            #等待查询元素
            sleep(1)
            #WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="appMain"]/div/div/form/span/button[1]/span')))
            ClueListPage(self.driver).seach_btn()
            #等待详细元素存在点击详情
            sleep(2)
            ClueListPage(self.driver).detail_btn()
            #等待新页面的元素加载
            sleep(2)
            # 点击excel中的param元素
            Page(self.driver).find_element(*eval(testdata["param"])).click()
            sleep(2)
            assertdata = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            #如果失败，截图
            if str(assertdata) != str(testdata["assertresult"]):
                picname = str(testdata["function"])+"失败"
                screenshot(self.driver, picname)
            self.assertEqual(str(testdata["assertresult"]),str(assertdata))

        else:
            # 如果action，则发送send_keys
            if testdata["action"]:
                if eval(testdata["action"])[0] == "send_keys()":
                    # 先点击元素后最近30天
                    Page(self.driver).find_element(*eval(testdata["param"])).send_keys(eval(testdata["action"])[1])
                    sleep(1)
                    ClueListPage(self.driver).last30_btn()
                    sleep(1)

            else:  #点击excel中的元素
                Page(self.driver).find_element(*eval(testdata["param"])).click()
                sleep(1)
            #查询后断言
            ClueListPage(self.driver).seach_btn()
            sleep(2)
            assertdata = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            #如果失败，截图
            if str(assertdata) != str(testdata["assertresult"]):
                picname = str(testdata["function"])+"失败"
                screenshot(self.driver, picname)
            self.assertEqual(str(testdata["assertresult"]),str(assertdata))




if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(ClueList("test_ui"))
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
