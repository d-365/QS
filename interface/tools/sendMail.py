# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 17:34
# @Author  : dujun
# @File    : sendMail.py
# @describe: 发送电子邮件
from py3_email import Mail


# py_email发送邮件
def send_mail(file_name=''):
    receivers = ['1765043251@qq.com','dujun8368@dingtalk.com']
    host = 'smtp.qq.com'
    user = '859893448@qq.com'
    password = 'wsrbthmniifobdef'

    m = Mail(receivers=receivers, host=host, user=user, password=password)
    m.add_tittle('接口自动化执行报告')
    m.add_attachment(file_name=file_name)
    m.send()


if __name__ == '__main__':
    send_mail()
