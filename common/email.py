# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2020/07/29 19:24

import smtplib, time, os
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.config import ConfigJson

SMTP_CONFIG_PATH = os.path.join(os.getcwd(), "resources", "smtp.json")

class Mail(object):
    def __init__(self, receiver):        
        self.receiver = receiver
        self.mail = MIMEMultipart()



    def send(self):
        msg = MIMEMultipart()
        # stress_body = Consts.STRESS_LIST
        # result_body = Consts.RESULT_LIST
        # content = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        # mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')

        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        msg['Subject'] = Header("接口自动化测试报告"+"_"+tm, 'utf-8')

        msg['From'] = self.config.sender

        receivers = self.config.receiver
        toclause = receivers.split(',')

        msg['To'] = ",".join(toclause)


        msg.attach(mail_body2)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.server)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")

        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
