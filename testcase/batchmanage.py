from commom.shot import screenshot
from commom.page import Page
from commom.myunit import MyUnit
from commom.mylog import Log
from commom.readexcel import ReadExcel
from testcase.basepage.bathchmanagepage import BatchManagePage
from time import sleep
from selenium.webdriver.common.by import By
import ddt
testdata=ReadExcel.read_data("批次管理")
@ddt.ddt
class BatchManage(MyUnit):
    @ddt.data(*testdata)
    def test_piciguanli(self):
        Log.info(testdata)
        sleep(0.3)
        #点击外呼管理
        Page(self.driver).find_element(BatchManagePage(self.driver).callmanage)
        Page(self.driver).wait_until_presence(BatchManagePage(self.driver).batchmanage)
        #点击批次管理
        Page(self.driver).find_element(BatchManagePage(self.driver).batchmanage)
        sleep(0.5)


