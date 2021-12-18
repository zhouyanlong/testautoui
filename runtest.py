from commom import setting
import unittest,time
from commom.sendemail import send_mail
from commom.newreport import new_report
from commom.HTMLTestRunner import HTMLTestRunner
def load_testcase(testcase=setting.testcasedir):
    return unittest.defaultTestLoader.discover(testcase, pattern='stop*.py')
def run_case(filedir=setting.reportdir):
    #设置报告名称
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename=filedir+'/'+now+"result.html"
    #实例化HTMLTestRunner并运行case
    with open(filename,"wb")as fp:
        runner = HTMLTestRunner(stream=fp, verbosity=2, title="UI自动化测试", description=None, tester="zhouyanlong")
        runner.run(load_testcase())
        send_mail(new_report())


if __name__ == '__main__':
    run_case()

