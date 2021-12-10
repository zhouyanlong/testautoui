from commom.mylog import Log
from commom.myunit import MyUnit
from commom.readexcel import ReadExcel
from testcase.basepage.fieldmanagepage import FieldManagePage
from commom.page import Page
from time import sleep
from commom.shot import screenshot
from selenium.webdriver.common.by import By
import ddt
testdata=ReadExcel().read_data("字段管理")
@ddt.ddt
class FieldManage(MyUnit):
    @ddt.data(*testdata)
    def test_ziduanguanli(self,testdata):
        Log.info(testdata)
        sleep(0.3)
        #点击线索中心
        FieldManagePage(self.driver).cluecenter_page()
        #sleep(1)
        Page(self.driver).wait_until_presence(self.driver,FieldManagePage(self.driver).fieldmanagebtn)
        #点击字段管理
        FieldManagePage(self.driver).fieldmanage_page()
        sleep(0.5)
        #循环执行excel中的元素和action
        for i in range(len(eval(testdata["param"]))):
            print(eval(testdata["action"])[i],*(eval(testdata["param"])[i]))
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*(eval(testdata["param"])[i]))
            sleep(0.5)
        #元素点击完毕后开始断言
        assertdata = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(assertdata) != testdata["assertresult"]:
            screenshot(self.driver, testdata["function"] + "失败")
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
        else:
            Log.info("用例{}:{}执行成功".format(testdata["id"],testdata["function"]))
        self.assertEqual(testdata["assertresult"], str(assertdata))







if __name__ == '__main__':
    FieldManage().main()
