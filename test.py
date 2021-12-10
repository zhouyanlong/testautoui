from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from commom.page import Page
from commom.shot import screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class Test():
    def __init__(self):
        url = "https://ai.zhilingsd.com/#/login"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[1]/div/div[2]/input').send_keys(
            "zhouyanlong")
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div[3]/form/div[2]/div/div[2]/input').send_keys(
            "Aa123456.")
        self.driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div[3]/div[3]/form/button/span').click()
        self.driver.find_element(By.XPATH,
                            '//*[@id="app"]/div[1]/div/div[2]/div/div[2]/div').click()
        #screenshot(self.driver, "登陆成功")
        #self.driver.get_screenshot_as_file(r'D:\pycharm\pythondemo\testui1125\screenpic\登陆成功.png')
        sleep(1)

    def test_xiansuoliebiao(self):


        #点击线索中心
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/div/span').click()
        #点击线索列表
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/ul/a[1]/li').click()
        sleep(1)
        #点击查询
        #self.driver.find_element(By.XPATH, '//*[@id="appMain"]/div/div/form/span/button[1]/span').click()
        print("1")
        #暂无数据
        #a=self.driver.find_element(By.XPATH,'//*[@id="appMain"]/div/div/div/div[2]/div[3]/div/span').text
        #print(a)
        #点击30天
        Page(self.driver).find_element("XPATH",'//*[@id="appMain"]/div/div/form/div[1]/div/div/div/div/div[1]/label[4]/span')
        sleep(1)
        #点击详情
        Page(self.driver).find_element("XPATH", '//*[@id="appMain"]/div/div/div/div[2]/div[5]/div[2]/table/tbody/tr[1]/td[20]/div/div/button/span').click()
        sleep(2)

        self.driver.quit()
    def test_ziduanguanli(self):
        #点击线索中心
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/div/span').click()
        #点击字段管理
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/ul/a[2]/li/span').click()
        #编辑线索id
        self.driver.find_element(By.XPATH,'//*[@id="appMain"]/div/div[1]/div/div[1]/div[3]/table/tbody/tr[1]/td[10]/div/button/span').click()
        #点击确定
        self.driver.find_element(By.XPATH,'//*[@id="appMain"]/div/div[2]/div/div[3]/span/button[2]/span').click()
        sleep(0.3)
        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'/div/p')))
        #self.driver.switch_to.alert()
        a=self.driver.find_element(By.CLASS_NAME,'el-message__content').text
        #a=self.driver.find_element(By.XPATH,'/div/p').text
        #a=self.driver.find_element(By.XPATH,'/div/p').text
        print(a)
        """#点击必填下拉框
        self.driver.find_element(By.XPATH,'//*[@id="appMain"]/div/div[1]/form/div[3]/div/div/div/input').click()
        #选择否
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[3]').click()
        sleep(1)
        #点击查询
        self.driver.find_element(By.XPATH,'//*[@id="appMain"]/div/div[1]/form/div[4]/div/button[1]/span').click()
        sleep(3)"""
        self.driver.quit()
    def find(self,*loctor):
        return self.driver.find_element(*loctor)
    def testtt(self):
        cluecenter=(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[1]/div/ul/div/li[2]/div/span')
        Test().find(*cluecenter)
        sleep(3)

if __name__ == '__main__':
    #Test().test_ziduanguanli()
    Test().test_ziduanguanli()
