import pytest,os,allure
"""@pytest.fixture(scope="class")
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
    print("333222111")"""
@pytest.fixture(autouse=True)
def tttaaa():
    print("全局fixture")