import configparser
from commom import setting
def get_config(option,selection,file=setting.configdir):
    con=configparser.ConfigParser()
    con.read(file,encoding="UTF-8")
    return con.get(option,selection)

if __name__ == '__main__':
    print(get_config("test","name"))