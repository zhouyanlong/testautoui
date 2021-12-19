from common.mylog import Log
from common.myunit import MyUnit
from common.readexcel import ReadExcel
from testcase.basepage.fieldmanagepage import FieldManagePage
from common.page import Page
from time import sleep
from common.shot import screenshot
from selenium.webdriver.common.by import By
import ddt
testdata=ReadExcel().read_data("字段管理")
@ddt.ddt
class FieldManage(MyUnit):
    @ddt.data(*testdata)
    def test_ziduanguanli(self,testdata):
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
        assertdata = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(assertdata) != testdata["assertresult"]:
            screenshot(self.driver, testdata["function"] + "失败")
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
        else:
            Log.info("用例{}:{}执行成功".format(testdata["id"],testdata["function"]))
        self.assertEqual(testdata["assertresult"], str(assertdata))







if __name__ == '__main__':
    FieldManage().main()
