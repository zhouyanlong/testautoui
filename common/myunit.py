import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.mylog import Log
from time import sleep
from common.page import Page
class MyUnit(unittest.TestCase):
    def setUp(self) -> None:
        url = "https://ai.zhilingsd.com/#/login"
        #账号、密码、登陆、选择营销
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
        sleep(1)
    @classmethod
    def setUpClass(cls) -> None:
        Log.info("开始执行测试用例")
    def tearDown(self) -> None:
        self.driver.quit()
    @classmethod
    def tearDownClass(cls) -> None:
        Log.info("测试用例执行完成")