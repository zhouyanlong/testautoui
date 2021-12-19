import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from commom.page import Page
from time import sleep

@pytest.fixture(scope="function", autouse=True)
def browser():
    '''
    开启浏览器
    定义全局浏览器驱动
    :return:
    '''
    url = "https://ai.zhilingsd.com/#/login"
    # 账号、密码、登陆、选择营销
    account = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/input')
    password = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[2]/div/div[2]/input')
    login = (By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/button/span')
    market = (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    Page(driver).find_element(*account).send_keys("zhouyanlong")
    Page(driver).find_element(*password).send_keys("Aa123456.")
    Page(driver).find_element(*login).click()
    Page(driver).find_element(*market).click()
    sleep(1)
    yield driver
    driver.quit()
    return driver


