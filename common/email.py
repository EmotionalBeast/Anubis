# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 19:24

import smtplib, time, os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from common.config import ConfigJson
from common.log import LogHandler

SMTP_CONFIG_PATH = os.path.join(os.getcwd(), "resources", "smtp.json")

class Mail(object):
    def __init__(self, *receiver):        
        self.receiver = receiver
        self.mail = MIMEMultipart()
        self.dic = ConfigJson(SMTP_CONFIG_PATH).jsonDic
        self.server = self.dic['server']
        self.user = self.dic["user"]
        self.pw = self.dic["passWord"]
        self.sender = self.dic["sender"]
        self.log = LogHandler()
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.prepareMail()
    
    def prepareMail(self):
        content = self.getAttachContent()
        image = self.getAttachImage()
        self.mail['Subject'] = Header("接口自动化测试报告" + "_" + self.time, 'utf-8')
        self.mail['From'] = self.sender
        self.mail['To'] = ""
        self.mail.attach(content)
        self.mail.attach(image)
    
    def getAttachContent(self):
        return 0
    
    def getAttachImage(self):
        return 0

    def send(self):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.server)
            smtp.login(self.user, self.pw)
            smtp.sendmail(self.sender, self.receiver, self.mail.as_string())
        except Exception as e:
            print(e)
            print("发送失败!")
            self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print("发送成功!")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
