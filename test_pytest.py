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
class Test3():


    # def setup(self):
    #     print("test starts")
    #ccdd从当前目录下conftest.py中获取
    def test_1(self):
        print("1正在测试中")
        assert 1==1
    #重试
    #@pytest.mark.flaky(reruns=3)
    def test_2(self):
        assert 2==1
    def test_3(self):
        print("3正在测试中")
        assert 2==2
    # def teardown(self):
    #     print("test ends")
if __name__ == '__main__':
    pytest.main(["-sv","test_pytest.py",'--reruns=1'])