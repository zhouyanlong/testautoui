from common.shot import screenshot
from common.page import Page
from common.myunit import MyUnit
from common.mylog import Log
from common.readexcel import ReadExcel
from testcase.basepage.bathchmanagepage import BatchManagePage
from time import sleep
import time
from common import setting
from selenium.webdriver.common.by import By
import ddt,os
testdata=ReadExcel().read_data("批次管理")
@ddt.ddt
class BatchManage(MyUnit):
    @ddt.data(*testdata)
    def test_piciguanli(self,testdata):
        Log.info(testdata)
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击外呼管理
        BatchManagePage(self.driver).callmanage_page()
        Page(self.driver).wait_until_presence(self.driver,BatchManagePage(self.driver).batchmanage)
        #点击批次管理
        BatchManagePage(self.driver).batchmanage_page()
        sleep(0.5)
        #如果是创建批次
        if testdata["function"]=="创建批次":
            BatchManagePage(self.driver).createbatch_page()
            sleep(0.5)
            BatchManagePage(self.driver).uploadfile_page()
            sleep(0.5)
            #使用os上传文件
            os.system(setting.batchuploadfile)
            sleep(1)
            # 参数化批次名称
            testdata["action"] = testdata["action"].replace(eval(testdata["action"])[1][1], "test" + str(time.strftime("%Y%m%d_%H:%M:%S")))
            for i in range(len(eval(testdata["param"]))):
                if i ==5:
                    #滚动
                    target = Page(self.driver).find_element(*(BatchManagePage(self.driver).ok))
                    self.driver.execute_script("arguments[0].scrollIntoView();", target)
                    sleep(1)
                    Page(self.driver).find_element_action(eval(testdata["action"])[i], *eval(testdata["param"])[i])
                    sleep(0.5)
                else:
                    Page(self.driver).find_element_action(eval(testdata["action"])[i], *eval(testdata["param"])[i])
                    sleep(0.5)
            Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
            sleep(0.5)
            result=Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            if str(result) != str(testdata["assertresult"]):
                Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
                screenshot(self.driver, testdata["function"] + "失败")
            self.assertEqual(str(testdata["assertresult"]),str(result))
        #其他情况，直接执行元素和action
        else:
            for i in range(len(eval(testdata["param"]))):
                Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
                Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])
            Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
            sleep(0.5)
            result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
            if str(result) != str(testdata["assertresult"]):
                Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
                screenshot(self.driver, testdata["function"] + "失败")
            self.assertEqual(str(testdata["assertresult"]),str(result))
if __name__ == '__main__':
    BatchManage().main()

