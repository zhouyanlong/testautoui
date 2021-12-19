from common.page import Page
from common.readexcel import ReadExcel
from common.shot import screenshot
from common.mylog import Log
from common.myunit import MyUnit
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
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击外呼管理
        Page(self.driver).wait_until_presence(self.driver, SmsStrategyPage(self.driver).callmanage)
        SmsStrategyPage(self.driver).callmanage_page()
        Page(self.driver).wait_until_presence(self.driver,SmsStrategyPage(self.driver).smsstrategy)
        sleep(0.5)
        #点击短信策略
        SmsStrategyPage(self.driver).smsstrategy_page()
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*(eval(testdata["param"])[i]))
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result=Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result)!=str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver,testdata["function"]+"失败")
        self.assertEqual(str(testdata["assertresult"]),str(result))
if __name__ == '__main__':
    SmsStrategy.main()

