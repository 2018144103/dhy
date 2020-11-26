import smtplib
from email.mime.text import MIMEText
msg_from='1900912756@qq.com'
passwd='oznfpebgnxrvbaea'
msg_to='57820048@qq.com'

subject="2018144154陈娜的第一次作业"
content="内网手机wifi：218.63.75.76 外网手机wifi:218.63.75.76  内网手机流量：172.69.34.156  外网手机流量：172.69.34.156"
msg=MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com",465)
    s.login(msg_from,passwd)
    s.sendmail(msg_from,msg_to,msg.as_string())
    print("发送成功")
except(s.SMTPException,e):
    print("发送失败")
finally:
    s.quit()