from commom import setting
import logging
from commom import setting
from logging import handlers
class Log():
    def get_log(self,level,msg,filename1=setting.infologdir,filename2=setting.errorlogdir):
        #获取日志收集器
        mylog=logging.getLogger()
        #设置级别
        mylog.setLevel("DEBUG")
        #输出到控制台
        sh=logging.StreamHandler()
        sh.setLevel("INFO")
        sh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        #输出到文件
        fh1=logging.handlers.TimedRotatingFileHandler(filename1, when='D', interval=30, backupCount=10,encoding="UTF8")
        fh1.setLevel("DEBUG")
        fh1.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        #添加到handle
        mylog.addHandler(sh)
        mylog.addHandler(fh1)
        if level=="DEBUG":
            mylog.debug(msg)
        if level=="INFO":
            mylog.info(msg)
        if level=="WARNING":
            mylog.warning(msg)
        if level=="ERROR":
            fh2 = logging.FileHandler(filename2,encoding="UTF8")
            fh2.setLevel("DEBUG")
            fh2.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            mylog.addHandler(fh2)
            mylog.error(msg)
            mylog.removeHandler(fh2)
            fh2.close()
        if level=="CRITICAL":
            mylog.critical(msg)
        #删除handle
        mylog.removeHandler(sh)
        mylog.removeHandler(fh1)
        fh1.close()

    @staticmethod
    def debug(msg):
        Log().get_log("DEBUG",msg)
    @staticmethod
    def info(msg):
        Log().get_log("INFO", msg)
    @staticmethod
    def warning(msg):
        Log().get_log("WARNING", msg)
    @staticmethod
    def error(msg):
        Log().get_log("ERROR", msg)
    @staticmethod
    def critical(msg):
        Log().get_log("CRITICAL", msg)
if __name__ == '__main__':
    Log.debug("1")
    Log.info("2")
    Log.warning("3")
    Log.error("4")
    Log.critical("阿萨德")
