from common.page import Page
from common.shot import screenshot
from common.mylog import Log
from common.readexcel import ReadExcel
from testcase.basepage.stopblacklistpage import StopBlacklistPage
from time import sleep
import pytest
from selenium.webdriver.common.by import By
testdata=ReadExcel().read_data("停呼黑名单")
class TestStopBlacklist():
    """
    setup和teardown,默认为function级别的，可以直接在此处配置，也可以在conftest.py做全局配置
    def setup(self):
        self.driver=Login().login_market()

    def teardown(self):
        self.driver.quit()"""
    #使用fixture中的params做数据驱动，相当于ddt
    @pytest.fixture(params=testdata)
    def excel_data(self,request):
        return request.param
    """
    在conftest.py做全局配置时调用登陆接口，返回driver，此处需要将的返回的driver赋值给self.driver
    """
    def test_tinghuheimingdan(self,excel_data,start):
        self.driver=start
        testdata=excel_data
        Log.info(testdata)
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击系统设置
        StopBlacklistPage(self.driver).syssetting_page()
        Page(self.driver).wait_until_clickable(self.driver,StopBlacklistPage(self.driver).stopblacklist)
        sleep(0.5)
        #点击停呼黑名单
        StopBlacklistPage(self.driver).stopblacklist_page()
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result) != str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver, testdata["function"] + "失败")
        assert str(testdata["assertresult"])==str(result)

if __name__ == '__main__':
    #pytest.main()
    pytest.main(["-sv","test_stopblacklist.py","--html=123report.html"])