from commom.page import Page
from commom.readexcel import ReadExcel
from commom.shot import screenshot
from commom.mylog import Log
from commom.myunit import MyUnit
from testcase.basepage.smsstrategypage import SmsStrategyPage
from selenium.webdriver.common.by import By
import ddt
from time import sleep
testdata=ReadExcel().read_data("短信策略")
@ddt.ddt
class SmsStrategy(MyUnit):
    @ddt.data(*testdata)
    def test_duanxincelue(self,testdata):
        Log.info(testdata)
        sleep(0.3)
        #点击外呼管理
        SmsStrategyPage(self.driver).callmanage_page()
        Page(self.driver).wait_until_presence(self.driver,SmsStrategyPage(self.driver).smsstrategy)
        sleep(0.5)
        #点击短信策略
        SmsStrategyPage(self.driver).smsstrategy_page()
        sleep(0.5)
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*(eval(testdata["param"])[i]))
            sleep(0.5)
        result=Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result)!=str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver,testdata["function"]+"失败")
        self.assertEqual(str(result),str(testdata["assertresult"]))
if __name__ == '__main__':
    SmsStrategy.main()

