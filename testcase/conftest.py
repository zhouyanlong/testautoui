import pytest,allure,os
from common.mylog import Log
from testcase.login import Login

driver = None
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    这里item是测试用例，call是测试步骤，具体执行过程如下：
    先执行when='setup' 返回setup 的执行结果
    然后执行when='call' 返回call 的执行结果
    最后执行when='teardown'返回teardown 的执行结果
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        #如果存在文件failures则追加写入文件，否则直接写
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图,hasattr表示如果driver有get_screenshot_as_png这个属性
        if hasattr(driver, "get_screenshot_as_png"):
            Log.info("添加失败截图")
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)



"""setup、teardown的两种实现方式"""
# @pytest.fixture(scope="function",autouse=True)
# def start(request):
#     def end():
#         Log.info("用例执行完成")
#         driver.quit()
#     request.addfinalizer(end)
#     Log.info("用例开始执行")
#     global driver
#     driver=Login().login_market()
#     return driver

@pytest.fixture(scope="function",autouse=True)
def start():
    global driver
    Log.info("用例开始执行")
    driver = Login().login_market()
    yield driver
    Log.info("用例执行完成")
    driver.quit()

