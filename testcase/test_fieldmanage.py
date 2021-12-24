from common.mylog import Log
from common.readexcel import ReadExcel
from testcase.basepage.fieldmanagepage import FieldManagePage
from common.page import Page
from time import sleep
from common.shot import screenshot
from selenium.webdriver.common.by import By
import pytest
testdata=ReadExcel().read_data("字段管理")
# 使用fixture中的params做数据驱动，相当于ddt
@pytest.fixture(params=testdata)
def excel_data(request):
    return request.param
class TestFieldManage():
    """
            setup和teardown,默认为function级别的，可以直接在此处配置，也可以在conftest.py做全局配置
            def setup(self):
                self.driver=Login().login_market()

            def teardown(self):
                self.driver.quit()"""

    """
    在conftest.py做全局配置时调用登陆接口，返回driver，此处需要将的返回的driver赋值给self.driver
    """
    def test_ziduanguanli(self,excel_data,start):
        self.driver = start
        testdata = excel_data
        Log.info(testdata)
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击线索中心
        Page(self.driver).wait_until_presence(self.driver, FieldManagePage(self.driver).cluecenterbtn)
        FieldManagePage(self.driver).cluecenter_page()
        #sleep(1)
        Page(self.driver).wait_until_presence(self.driver,FieldManagePage(self.driver).fieldmanagebtn)
        sleep(0.5)
        #点击字段管理
        FieldManagePage(self.driver).fieldmanage_page()
        #循环执行excel中的元素和action
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*(eval(testdata["param"])[i]))
        #元素点击完毕后开始断言
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result) != testdata["assertresult"]:
            screenshot(self.driver, testdata["function"] + "失败")
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
        else:
            Log.info("用例{}:{}执行成功".format(testdata["id"],testdata["function"]))
        assert str(testdata["assertresult"])==str(result)







if __name__ == '__main__':
    pytest.main(["-sv","test_fieldmanage.py"])
