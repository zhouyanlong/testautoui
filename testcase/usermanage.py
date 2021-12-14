from selenium.webdriver.common.by import By
from commom.page import Page
from commom.shot import screenshot
from commom.mylog import Log
from commom.readexcel import ReadExcel
from commom.myunit import MyUnit
from testcase.basepage.usermanagepage import UserManagePage
from time import sleep
import ddt
testdata=ReadExcel().read_data("用户管理")
@ddt.ddt
class UserManage(MyUnit):
    @ddt.data(*testdata)
    def test_tinghuheimingdan(self,testdata):
        Log.info(testdata)
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击系统设置
        UserManagePage(self.driver).syssetting_page()
        Page(self.driver).wait_until_clickable(self.driver,UserManagePage(self.driver).stopblacklist)
        sleep(0.5)
        #点击停呼黑名单
        UserManagePage(self.driver).stopblacklist_page()
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            sleep(2)
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result) != str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver, testdata["function"] + "失败")
        self.assertEqual(str(testdata["assertresult"]), str(result))
if __name__ == '__main__':
    UserManage().main()