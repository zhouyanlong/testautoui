import os
from common import setting

def new_report(filepath=setting.reportdir):
    files=os.listdir(filepath)
    files.sort(key=lambda fn:os.path.getmtime(filepath))
    file_new=os.path.join(filepath,files[-1])
    return file_new
if __name__ == '__main__':

    print(new_report())
