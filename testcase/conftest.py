import pytest
from common.mylog import Log
from testcase.login import Login
@pytest.fixture(scope="function",autouse=True)
def start(request):
    def end():
        Log.info("用例执行完成")
        driver.quit()
    request.addfinalizer(end)
    Log.info("用例开始执行")
    driver=Login().login_market()
    return driver


