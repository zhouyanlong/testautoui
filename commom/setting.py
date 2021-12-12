import sys,os
projectdir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(projectdir)
configdir=os.path.join(projectdir,"config/config.ini")
infologdir=os.path.join(projectdir,"log/info.txt")
errorlogdir=os.path.join(projectdir,"log/error.txt")
reportdir=os.path.join(projectdir,"report")
screenpicdir=os.path.join(projectdir,"screenpic")
testdatadir=os.path.join(projectdir,"testdata/case.xlsx")
batchuploadfile="D:\software\AutoIt3\jiaoben\jiaoben.exe"

