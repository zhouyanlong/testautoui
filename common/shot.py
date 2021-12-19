from common import setting
import os
import time
from common.mylog import Log
#断言失败截图
def screenshot(driver, filename):
    finalfilename = setting.screenpicdir + "\\" +time.strftime("%Y%m%d_%H%M%S") +filename + ".png"
    Log.info(finalfilename)
    return driver.get_screenshot_as_file(finalfilename)
#删除图片
def delshot(filepath=setting.screenpicdir):
    try:
        piclist = os.listdir(filepath)
        for i in piclist:
            picname = filepath + "\\" + i
            if os.path.isfile(picname):
                os.remove(picname)
    except Exception as e:
        Log.error("删除文件失败,请检查文件是否正常:{}".format(e))



if __name__ == '__main__':
    delshot()



