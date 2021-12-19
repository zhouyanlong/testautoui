import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from commom.page import Page
from time import sleep

@pytest.fixture()
def aabb(self):
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
    sleep(1)
    # 后置
    yield
    self.driver.quit()

@pytest.fixture(scope="class")
def ccdd():
    print("test 就要开始啦啦啦啦啦")
    # 后置
    yield
    print("test 已经结束了啦啦啦啦")

@pytest.fixture(scope="function",autouse=True)
def eeff():
    print("123123123")
    # 后置
    yield
    print("333222111")
