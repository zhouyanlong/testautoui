import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.page import Page
from time import sleep
from testcase.login import Login
@pytest.fixture(scope="function")
def broswer(request):
    def end():
        print("全部用例执行完后 teardown quit dirver1")
        driver.quit()
    request.addfinalizer(end)
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


