import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'wsxcd@wsecar.com'
receivers = ['wangchunbo@wsecar.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("万顺叫车", 'utf-8')  # 发送者
message['To'] = Header("染血", 'utf-8')  # 接收者
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # 创建对象
    smtpObj = smtplib.SMTP()
    # 连接邮件服务器
    smtpObj.connect("smtp.wsecar.com", 25)
    # 登录，用户名，密码
    smtpObj.login("wsxcd@wsecar.com", "Wsjc201609")
    # 发送邮件
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")