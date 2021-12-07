from commom.page import Page
from selenium.webdriver.common.by import By
class Test1():

    def find_element(self,*loctor):
        print(*loctor)

    """def ttt(self,*re):
        print(*re)

    cluelist_btn=(123,"222","33",66)
    ttt(*cluelist_btn)"""

    # 关键字参数，传参会被加工成元组
    def print_hello(*args):
        print(args)
        print(*args) #print(*args)输出结果(1, ('zhou', '男'))       1 ('zhou', '男')解包裹后会把元组中的元素打印出来
    #a = (1,('zhou', '男'))
    #print_hello(a)#print(args)把元组a当成参数传入关键字参数中，会被加工成三个括号((1, ('zhou', '男')),)的嵌套元组
    #print_hello(*a)#print(args)解包裹参数，把元组a拆开后当成各个参数传入关键字参数中，结果会被加工成一个元组中的两个参数(1, ('zhou', '男'))
if __name__ == '__main__':
    #cluecenter = [By.XPATH,'//*[@id="appMain"]/div/div/form/div[1]/div/div/div/div/div[1]/label[1]/span']
    cluecenter = (By.XPATH, '//*[@id="appMain"]/div/div/form/div[1]/div/div/div/div/div[1]/label[1]/span')
    Test1().find_element(cluecenter)
    a=["send_keys()", "222"]
