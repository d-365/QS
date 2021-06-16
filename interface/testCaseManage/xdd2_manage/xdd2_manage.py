# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:21
# @Author  : dujun
# @File    : xdd2_manage.py
# @describe: xdd2-好单多多应用层

import hashlib

from interface.project.xddd2.xddd2 import xddd_pro
from interface.tools.dataBase import DataBase


class xdd2_manage:

    def __init__(self, phone):
        self.phone = phone
        self.xddd2 = xddd_pro()
        self.database = DataBase()
        self.token = ''
        sql = 'UPDATE jgq.think_xsms SET code =1234,`status`=0 WHERE phone=%s;' % phone
        self.database.sql_execute(sql)
        payload = {
            'phone': self.phone,
            'code': '1234',
            'device_token': 'like365'
        }
        res = self.xddd2.xddd2_login(params=payload)
        self.token = res['data']['token']

    def login_pw(self, password):
        md5 = hashlib.md5()
        encode = password.encode(encoding='utf-8')
        md5.update(encode)
        passwd_md5 = md5.hexdigest()
        print(passwd_md5)
        payload = {
            'device_token': 'like365',
            'p': passwd_md5,
            'phone': '11111111101',
            'timeStamp': '1623069638474'
        }
        res = self.xddd2.login_password(datas=payload)
        print(res)


if __name__ == "__main__":
    run = xdd2_manage('11111111101')
    run.login_pw('1')
