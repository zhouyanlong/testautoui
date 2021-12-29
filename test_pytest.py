"""import ddt,unittest
@ddt.ddt
class Test3(unittest.TestCase):
    testdata=([{"name":"zhou","sex":"man"},{"name":"zhou1","sex":"man"}],[{"name":"zhou","sex":"man"},{"name":"zhou1","sex":"man"}])
    @ddt.data(*testdata)
    def test(self,param):
        print(param)
if __name__ == '__main__':
    unittest.main()"""

import pytest
import allure,os
@allure.feature("打印xx功能")
class Test3():


    # def setup(self):
    #     print("test starts")
    #ccdd从当前目录下conftest.py中获取
    #@pytest.fixture()
    @allure.story("cs1")
    def test_1(self):
        print("1正在测试中")
        assert 1==1
    #重试
    #@pytest.mark.flaky(reruns=3)
    @allure.story("cs2")
    def test_2(self):
        assert 3==1

    @allure.story("cs3")
    def test_3(self):
        with allure.step("step1 print"):
            print("3正在测试中")

        with allure.step("step2 print"):
            print("3正在测试中ing")
        with allure.step("step3 assert"):
            assert 2==2
    # def teardown(self):
    #     print("test ends")
if __name__ == '__main__':
    #pytest.main(["-sv","test_pytest.py",'--reruns=1'])
    pytest.main(["test_pytest.py", '--alluredir', 'report','--clean-alluredir'])
    os.system('allure serve report')
#import pytest
# class TestTT():
#     @pytest.fixture()
#     def test(self):
#         print("fixture")
#     def test_1223(self,test):
#         print("1223")
# if __name__ == '__main__':
#     pytest.main(["-sv","test_pytest.py"])