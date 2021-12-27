from common.page import Page
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
class Test1():

    def find_element(self,*loctor):
        print(*loctor)

    """def ttt(self,*re):
        print(*re)

    cluelist_btn=(123,"222","33",66)
    ttt(*cluelist_btn)"""
    def test1207(self,a):
        if a> 8:
            print(a)
        else:
            if a<5:
                print("5")
                if a==3:
                    print(a)
                else:
                    print()
            else:
                print("ddd")

    # 关键字参数，传参会被加工成元组
    def print_hello(*args):
        print(args)
        print(*args) #print(*args)输出结果(1, ('zhou', '男'))       1 ('zhou', '男')解包裹后会把元组中的元素打印出来
    #a = (1,('zhou', '男'))
    #print_hello(a)#print(args)把元组a当成参数传入关键字参数中，会被加工成三个括号((1, ('zhou', '男')),)的嵌套元组
    #print_hello(*a)#print(args)解包裹参数，把元组a拆开后当成各个参数传入关键字参数中，结果会被加工成一个元组中的两个参数(1, ('zhou', '男'))
    def test_roll(self):
        driver=webdriver.Chrome()
        driver.get("https://www.cnblogs.com/jasmine0627/p/13094288.html")
        sleep(3)
        #driver.execute_script("arguments[0].scrollIntoView();",(By.XPATH,'//*[@id="poweredby"]'))
        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.execute_script("window.scrollTo(0,1000)")
        sleep(3)
    def test1217(self):
        #遍历str list
        a='[[1,2],[3,4]]'
        for i in eval(a):
            print(i)
        #使用下标
        for i in range(len(eval(a))):
            print(eval(a)[i])
        #遍历str,dict
        b='{"name":"zzz","age":"23"}'
        print(eval(b).keys(),eval(b).values(),eval(b).items())
        for i in eval(b).keys():
            print(i)
        for i in eval(b).values():
            print(i)
        for i,j in eval(b).items():
            print(i,j)
        #tuple
        c='(10,20,30)'
        for i in eval(c):
            print(i)
        #使用下表
        for i in range(len(eval(c))):
            print(eval(c)[i])
if __name__ == '__main__':
    #Test1().test_roll()
    #Test1().print_hello({"ss":"dd"})
    #Test1().test1217()
    print(type(('123',)))
    print(isinstance(("123",), tuple))
    a = (1, ('zhou', '男'))
    print(Test1().print_hello(*a))
