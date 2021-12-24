import unittest,ddt
from common.readexcel import ReadExcel
from common.mylog import Log
from time import sleep
from testcase.basepage.cluelistpage import ClueListPage
from common.page import Page
from common.shot import screenshot
import pytest
#不可不导入By，否则执行eval函数会报错找不到By
from selenium.webdriver.common.by import By
testdata=ReadExcel().read_data("线索中心")
# 使用fixture中的params做数据驱动，相当于ddt
@pytest.fixture(params=testdata)
def excel_data(request):
    return request.param
import pytest
class TestClueList():
    """
                setup和teardown,默认为function级别的，可以直接在此处配置，也可以在conftest.py做全局配置
                def setup(self):
                    self.driver=Login().login_market()

                def teardown(self):
                    self.driver.quit()"""

    """
    在conftest.py做全局配置时调用登陆接口，返回driver，此处需要将的返回的driver赋值给self.driver
    """
    def test_xiansuoliebiao(self,excel_data,start):
        testdata=excel_data
        self.driver=start
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
            result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            #如果失败，截图
            if str(result) != str(testdata["assertresult"]):
                picname = str(testdata["function"])+"失败"
                screenshot(self.driver, picname)
            assert str(testdata["assertresult"])==str(result)

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
            result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            #如果失败，截图
            if str(result) != str(testdata["assertresult"]):
                picname = str(testdata["function"])+"失败"
                screenshot(self.driver, picname)
            assert str(testdata["assertresult"])==str(result)




if __name__ == '__main__':
    """suite=unittest.TestSuite()
    suite.addTest(ClueList("test_ui"))
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)"""
    pytest.main(["-sv","test_cluelist.py"])