import ddt,unittest
@ddt.ddt
class Test3(unittest.TestCase):
    testdata=([{"name":"zhou","sex":"man"},{"name":"zhou1","sex":"man"}],[{"name":"zhou","sex":"man"},{"name":"zhou1","sex":"man"}])
    @ddt.data(*testdata)
    def test(self,param):
        print(param)
if __name__ == '__main__':
    unittest.main()