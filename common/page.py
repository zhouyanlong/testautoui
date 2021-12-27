from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
from time import sleep
from common.mylog import Log
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
        """
        :param loc: 传参能传1个元组，列表,或者传多个参数，把By和元素分开传如:((By.XPATH),('//*[@id="app"]'))，函数定义的*loc会自动组装成元组,然后调用find_element方法的时候再解包裹,要求传参数到此方法的时候也要先解包裹
        :return:
        """
        try:
        #print(*loctor,loctor)
            return self.driver.find_element(*loc)
        except Exception as e:
            Log.error("元素定位出现错误"+e)
    def find_element_test(self,loc):
        """
        :param loc: 传参能传元组，列表
        :return:
        """
        try:
        #print(*loctor,loctor)
            return self.driver.find_element(*loc)
        except Exception as e:
            Log.error("元素定位出现错误"+e)
    #专门处理excel中的元素和action
    def find_element_action(self,action,*loc):
        try:
            if action[0]=="click()":
                self.driver.find_element(*loc).click()
                #sleep(3)
            elif action[0]=="send_keys()":
                self.driver.find_element(*loc).send_keys(action[1])
            elif action[0]=="clear()":
                self.driver.find_element(*loc).clear()
        except Exception as e:
            Log.error("元素定位出现错误"+e)

    #等待元素存在
    def wait_until_presence(self,driver,loc,time=10,poll=1):
        return WebDriverWait(driver,time,poll,ignored_exceptions=None).until(EC.presence_of_element_located(loc))
    #等待元素可点击=可见+enable
    def wait_until_clickable(self,driver,loc,time=10,poll=0.5):
        return WebDriverWait(driver,time,poll,ignored_exceptions=None).until(EC.element_to_be_clickable(loc))
    #执行js
    def script(self,scr):
        return self.driver.execute_script(scr)
    #滚动鼠标到底部
    def rolling_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def get_handles(self):
        """
        获取当前所有句柄
        :return:所有句柄
        """
        Log.info('获取所有句柄')
        try:
            all_handles = self.driver.window_handles
        except Exception:
            Log.error('获取句柄失败')
            raise
        else:
            return all_handles

    def switch_alert(self, send_keys=None):
        """
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :send: 是否点击bool
        :return: alert内容
        """
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.alert_is_present())
            result = self.driver.switch_to.alert
            if result and send_keys is None:
                text = result.text
                Log.info("alert出现,内容：{}".format(text))
                result.accept()
                Log.info("alert已经关闭")
                return text
            elif result and send_keys is not None:
                text = result.text
                Log.info("alert出现,内容：{}".format(text))
                result.send_key(send_keys)
                result.accept()
                Log.info("alert已经关闭")
                return text
            else:
                Log.info("未弹出alert")
        except Exception:
            Log.error("alert切换失败！")
            raise

    def switch_window(self, handle='new', old_handles=None):
        """
        窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
        :param handle: (new, default,handle name )
        :param old_handles:切换新打开窗口时传入，传入的句柄为打开新窗口之前的所有句柄
        :return:
        """
        try:
            if handle == "new" and old_handles is not None:
                Log.info("切换到最新打开的窗口")
                WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(old_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif handle == "default":
                Log.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                # self.driver.switch_to_default_content()
            else:
                Log.info("切换到指定handles")
                self.driver.switch_to.window(handle)
        except Exception:
            Log.error("切换失败")
            raise

    def switch_iframe(self, loc):
        """
        切换iframe
        :param loc: 元素定位
        :return:
        """
        Log.info("iframe切换：{}".format(loc))
        try:
            WebDriverWait(self.driver, timeout=10).until(
                EC.frame_to_be_available_and_switch_to_it(loc))
            Log.info("切换成功")
        except Exception:
            Log.error("iframe切换失败！")
            raise

    def window_close(self):
        """
        关闭当前窗口
        :return:
        """
        self.driver.close()
        Log.info('关闭窗口')

    # #############元素操作部分#############

    def click(self, loc, msg=''):
        """
        点击操作
        :param loc:元素定位表达式
        :param msg:元素描述
        :return: None
        """

        try:
            Log.info('点击元素：{}'.format(msg))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc)).click()
        except Exception:
            Log.error('点击失败,元素不可点击或者元素点位失败')
            raise

    def submit(self, loc):
        """
        提交form表单操作，元素定位在form表单中任意元素即可
        记住只能在form表单中使用，一般在submit难定位时使用
        :param loc:元素定位表达式
        :return:
        """
        ele = self.find_element(*loc)
        try:
            Log.info('提交form表单')
            ele.submit()

        except Exception:
            Log.error('提交失败'.format())
            raise

    def get_text(self, loc, msg):
        """
        获取文本内容
        :param loc: 元素定位
        :param msg: 元素描述
        :return: 文本内容
        """
        ele = self.find_element(*loc)
        try:
            text = ele.text
            Log.info('{}元素文本：{}'.format(msg, text))
        except Exception:
            Log.error("获取文本失败")
            raise
        else:
            return text

    def uncheck_checkbox(self, loc, msg=''):
        """
        取消选择复选框
        :param loc:
        :param msg:
        :return:
        """
        if self.checkbox_status(loc):
            self.click(loc, msg=msg)
        else:
            Log.info('复选框没有选择')

    def check_checkbox(self, loc):
        """
        选择复选框
        :param loc:
        :param msg:
        :return:
        """
        if not self.checkbox_status(loc):
            self.click(loc)
        else:
            Log.info('复选框已是选择')

    def checkbox_status(self, loc):
        """
        复选框状态
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(*loc)
        try:
            status = ele.is_selected
            Log.info("复选框状态：{}".format(loc))
            return status
        except Exception:
            Log.error("获取复选框状态失败。")
            raise

    # #############js操作部分#############
    def click_by_js(self, loc, msg=''):
        """
        点击操作
        :param loc:元素定位表达式
        :param msg:元素描述
        :return: None
        """

        try:
            Log.info('点击元素：{}'.format(msg))
            ele = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(loc))
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception:
            Log.error('点击失败,元素不可点击或者元素点位失败')
            raise

    def scroll_into_view(self, loc):
        """
        滚动到元素可见位置
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(*loc)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            Log.info("滚动到元素：{}".format(loc))
        except Exception:
            Log.error("滚动操作失败。")
            raise

    # #############鼠标操作部分#############
    def double_click(self, loc):
        """
        鼠标双击
        :param loc: 元素定位
        :return:
        """
        ele = self.find_element(*loc)
        try:
            AC(self.driver).double_click(ele).perform()
            Log.info("双击元素：{}".format(loc))
        except Exception:
            Log.error("鼠标双击操作失败。")
            raise

    def right_click(self, loc):
        """
        右击
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element_test(*loc)
        try:
            AC(self.driver).context_click(ele).perform()
            Log.info("右击元素：{}".format(loc))
        except Exception:
            Log.error("右击操作失败。")
            raise

    def drag_and_drop(self, loc_rource, loc_tarteg):
        """
        拖动元素
        :param loc_rource:
        :param loc_tarteg:
        :param msg:
        :return:
        """
        ele = self.find_element(*loc_rource)
        ele1 = self.find_element(*loc_tarteg)
        try:
            AC(self.driver).drag_and_drop(ele, ele1).perform()
            Log.info("拖动元素：{}，{}".format(loc_rource, loc_tarteg))
        except Exception:
            Log.error("拖动操作失败。")
            raise

    def mouse_hover(self, loc):
        """
        鼠标悬停到一个元素位置
        :param loc:
        :param msg:
        :return:
        """
        ele = self.find_element(*loc)
        try:
            AC(self.driver).move_to_element(ele).perform()
            Log.info("鼠标悬停：{}".format(loc))
        except Exception:
            Log.error("鼠标操作失败。")
            raise

    # #############键盘操作部分#############
    def key_down(self, key, text):
        """
        用于模拟按下辅助按键(CONTROL, SHIFT, ALT)的动作，按住
        :param key: 键盘操作码
        :param text:
        :return:
        """
        # Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
        try:
            Log.info('按住{}输入{}'.format(key, text))
            AC(self.driver).key_down(key).send_keys(text).perform()
        except Exception:
            Log.error('输入失败')
            raise

    def key_up(self, loc, key, text, key1, text1):
        """
        用于模拟辅助按键(CONTROL, SHIFT, ALT)弹起或释放的操作，松开
        :param key:第一次按住键
        :param loc:定位器
        :param text:第一次输入文本
        :param key1:第二次按住的键
        :param text1:第二次输入文本
        :param msg:
        :return:
        """
        # Enters text "qwerty" with keyDown SHIFT key and after keyUp SHIFT key (QWERTYqwerty)
        ele = self.find_element(*loc)
        try:
            Log.info('输入内容：{}{}'.format(text, text1))
            ele.clear()
            AC(self.driver).key_down(key).send_keys_to_element(ele, text).key_up(key1).send_keys(text1).perform()
        except Exception:
            Log.error('输入失败')
            raise

    def send_keys(self, loc, text=''):
        """
        输入操作
        :param loc:元素定位表达式
        :param text: 输入内容
        :param msg:元素描述
        :return:
        """
        ele = self.find_element(*loc)
        try:
            Log.info('输入内容：{}'.format(text))
            ele.clear()
            ele.send_keys(text)
        except Exception:
            Log.error('输入失败')
            raise