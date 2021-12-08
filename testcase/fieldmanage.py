from commom.mylog import Log
from commom.myunit import MyUnit
from commom.readexcel import ReadExcel
from testcase.basepage.fieldmanagepage import FieldManagePage
import ddt
testdata=ReadExcel().read_data("字段管理")
@ddt.ddt
class FieldManage(MyUnit):
    @ddt.data(*testdata)
    def test_ziduanguanli(self,testdata):
        Log.info(testdata)
        #点击线索中心
        FieldManagePage(self.driver).cluecenter_page()
        #点击字段管理
        FieldManagePage(self.driver).fieldmanage_page()



if __name__ == '__main__':
    FieldManage().main()
