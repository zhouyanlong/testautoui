from selenium.webdriver.common.by import By
from common.page import Page
from common.shot import screenshot
from common.mylog import Log
from common.readexcel import ReadExcel
from testcase.basepage.stopblacklistpage import StopBlacklistPage
from time import sleep
from selenium import webdriver
from common.login import Login
import pytest

class TestStopBlacklist():

    """@pytest.fixture(scope="function")
    def setup(self,request):
        def teardown():
            self.driver.quit()
        request.addfinalizer(teardown())

        url = "https://ai.zhilingsd.com/#/login"
        # 账号、密码、登陆、选择营销
        account = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/input')
        password = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[2]/div/div[2]/input')
        login = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/button/span')
        market = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        Page(self.driver).find_element(*account).send_keys("zhouyanlong")
        Page(self.driver).find_element(*password).send_keys("Aa123456.")
        Page(self.driver).find_element(*login).click()
        Page(self.driver).find_element(*market).click()
        sleep(1)"""


    #
    testdata1=ReadExcel().read_data("停呼黑名单")
    @pytest.fixture(params=testdata1)
    def excel_data(self,request):
        return request.param

    def test_tinghuheimingdan(self,excel_data):
        self.driver=Login().login_s()
        testdata=excel_data
        Log.info(testdata)
        # 等待页面菜单加载，否则容易出现菜单点击不到
        sleep(1)
        #点击系统设置
        StopBlacklistPage(self.driver).syssetting_page()
        Page(self.driver).wait_until_clickable(self.driver,StopBlacklistPage(self.driver).stopblacklist)
        sleep(0.5)
        #点击停呼黑名单
        StopBlacklistPage(self.driver).stopblacklist_page()
        for i in range(len(eval(testdata["param"]))):
            Page(self.driver).wait_until_clickable(self.driver, eval(testdata["param"])[i])
            Page(self.driver).find_element_action(eval(testdata["action"])[i],*eval(testdata["param"])[i])
        Page(self.driver).wait_until_presence(self.driver, eval(testdata["assertparam"]))
        sleep(0.5)
        result = Page(self.driver).find_element(*eval(testdata["assertparam"])).text
        if str(result) != str(testdata["assertresult"]):
            Log.info("用例{}:{}执行失败".format(testdata["id"], testdata["function"]))
            screenshot(self.driver, testdata["function"] + "失败")
        assert (testdata["assertresult"])==str(result)

if __name__ == '__main__':
    #pytest.main()
    pytest.main(["-sv","test_stopblacklist.py"])