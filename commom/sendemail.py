from commom.config import get_config
import smtplib
from email.header import Header
from commom.mylog import Log
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from commom.newreport import new_report
def send_mail(file):
    # f = open(file,'rb')
    # mail_body = f.read()
    # f.close()
    # --------- 读取config.ini配置文件 ---------------
    HOST = get_config("user","HOST_SERVER")
    SENDER = get_config("user","FROM")
    RECEIVER = get_config("user","TO")
    USER = get_config("user","user")
    PWD = get_config("user","password")
    SUBJECT = get_config("user","SUBJECT")

    #msg = MIMEText(mail_body, "html", "utf-8")
    msg = MIMEMultipart()
    msg['Subject'] = Header(SUBJECT, "utf-8")
    msg['from'] = SENDER
    msg['to'] = RECEIVER

    att = MIMEApplication(open(file, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=file)
    msg.attach(att)

    try:
        server = smtplib.SMTP()
        server.connect(HOST)
        server.login(USER, PWD)
        server.sendmail(SENDER, RECEIVER, msg.as_string())
        server.quit()
        Log.info("邮件发送成功！")
    except Exception as  e:
        Log.error("失败: " + str(e))

if __name__ == '__main__':
    send_mail(new_report())