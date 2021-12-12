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
class SmsStrategypage(MyUnit):
    @ddt.data(*testdata)
    def test_duanxincelue(self,testdata):
        pass

