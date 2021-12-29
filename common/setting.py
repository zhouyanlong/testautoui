import sys,os
projectdir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(projectdir)
configdir=os.path.join(projectdir,"config/config.ini")
infologdir=os.path.join(projectdir,"log/info.txt")
errorlogdir=os.path.join(projectdir,"log/error.txt")
reportdir=os.path.join(projectdir,"report")
screenpicdir=os.path.join(projectdir,"screenpic")
testdatadir=os.path.join(projectdir,"testdata/case.xlsx")
testcasedir=os.path.join(projectdir,"testcase")
#autoit文件脚本路径
batchuploadfile="D:\software\AutoIt3\jiaoben\jiaoben.exe"

#输出到控制台的日志级别
LOG_STREAM_LEVEL="INFO"
#输出到文件的日志级别
LOG_FILE_LEVEL="DEBUG"
#隐式等待时间
IMPLICITLY_WAIT_TIME = 5