from commom import setting
import time
def screenshot(driver, filename):
    finalfilename = setting.screenpicdir + "\\" +time.strftime("%Y%m%d_%H%M%S") +filename + ".png"
    print(finalfilename)
    return driver.get_screenshot_as_file(finalfilename)


