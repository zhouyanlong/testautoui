from commom.mylog import Log
from commom.myunit import MyUnit
from commom.readexcel import ReadExcel
from testcase.basepage.fieldmanagepage import FieldManagePage
from commom.page import Page
from time import sleep
from selenium.webdriver.common.by import By
import ddt
testdata=ReadExcel().read_data("字段管理")
@ddt.ddt
class FieldManage(MyUnit):
    @ddt.data(*testdata)
    def test_ziduanguanli(self,testdata):
        Log.info(testdata)
        #点击线索中心
        FieldManagePage(self.driver).cluecenter_page()
        Page(self.driver).wait_until_presence(self.driver,FieldManagePage(self.driver).fieldmanagebtn)
        #点击字段管理
        FieldManagePage(self.driver).fieldmanage_page()
        sleep(1)
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])






if __name__ == '__main__':
    FieldManage().main()
