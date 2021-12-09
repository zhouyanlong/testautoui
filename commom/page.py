from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from commom.mylog import Log
#PO中的Page类，所有页面都继承的类
class Page():
    def __init__(self,driver):
        self.url = "https://ai.zhilingsd.com/#/login"
        self.driver=driver
    def open(self):
        #账号btn
        account=(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/input')
        password=(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[3]/form/div[2]/div/div[2]/input')
        login=(By.XPATH,'//*[@id="app"]/div[1]/div[3]/div[3]/form/button/span')
        #选择营销系统
        market=(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        Page(self.driver).find_element(*account).send_keys("zhouyanlong")
        Page(self.driver).find_element(*password).send_keys("Aa123456.")
        Page(self.driver).wait_until_presence(self.driver,login)
        Page(self.driver).find_element(*login).click()
        Page(self.driver).find_element(*market).click()
        sleep(1)
    """def find_element(self,method,ele):
        try:
            if method == "By.ID":
                return self.driver.find_element(By.ID,ele)
            if method == "By.XPATH":
                return self.driver.find_element(By.XPATH,ele)
            if method == "By.CSS_SELECTOR":
                return self.driver.find_element(By.CSS_SELECTOR,ele)
            if method == "By.NAME":
                return self.driver.find_element(By.NAME,ele)
            if method == "By.LINK_TEXT":
                return self.driver.find_element(By.LINK_TEXT,ele)
            if method == "By.TAG_NAME":
                return self.driver.find_element(By.TAG_NAME,ele)
            if method == "By.PARTIAL_LINK_TEXT":
                return self.driver.find_element(By.PARTIAL_LINK_TEXT,ele)
            if method == "By.CLASS_NAME":
                return self.driver.find_element(By.CLASS_NAME,ele)
        except Exception as e:
            Log.error("元素定位方式错误，请检查"+e)"""
    #封装元素定位方式,*是把两个参数分开传值
    def find_element(self,*loc):
        #print(*loctor,loctor)
        return self.driver.find_element(*loc)
    #专门处理excel中的元素和action
    def find_element_action(self,action,*loc):
        if action[0]=="click()":
            self.driver.find_element(*loc).click()
            #sleep(1)
        elif action[0]=="send_keys()":
            self.driver.find_element(*loc).send_keys(action[1])
            #sleep(1)



    #等待元素存在
    def wait_until_presence(self,driver,loc,time=10,poll=0.5):
        return WebDriverWait(driver,time,poll,ignored_exceptions=None).until(EC.presence_of_element_located(loc))
    #等待元素可点击=可见+enable
    def wait_until_clickable(self,driver,loc,time=10,poll=0.5):
        return WebDriverWait(driver,time,poll,ignored_exceptions=None).until(EC.element_to_be_clickable(loc))
    #执行js
    def script(self,scr):
        return self.driver.execute_script(scr)