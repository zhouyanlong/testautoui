from commom.page import Page
from commom.myunit import MyUnit
from commom.shot import screenshot
from commom.readexcel import ReadExcel
from selenium.webdriver.common.by import By
from commom.mylog import Log
from testcase.basepage.callrecordpage import CallRecordPage
import ddt
from time import sleep
testdata=ReadExcel().read_data("呼出记录")
@ddt.ddt
class CallRecord(MyUnit):
    @ddt.data(*testdata)
    def test_huchujilu(self,testdata):
        Log.info(testdata)
        #等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        Page(self.driver).wait_until_presence(self.driver,CallRecordPage(self.driver).recordcenter)
        #点击记录中心
        CallRecordPage(self.driver).recordcenter_page()
        Page(self.driver).wait_until_presence(self.driver,CallRecordPage(self.driver).callrecord)
        sleep(0.5)
        # 点击呼出记录
        CallRecordPage(self.driver).callrecord_page()
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result)!=str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver, testdata["function"] + "失败")
        self.assertEqual(str(testdata["assertresult"]),str(result))
if __name__ == '__main__':
    CallRecord().main()
