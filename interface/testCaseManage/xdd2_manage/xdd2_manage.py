# -*- coding: utf-8 -*-
# @Time    : 2021/6/7 20:21
# @Author  : dujun
# @File    : xdd2_manage.py
# @describe: xdd2-好单多多应用层

import hashlib

from interface.project.xddd2.xddd2 import xddd_pro
from interface.tools.dataBase import DataBase


class xdd2_manage:

    def __init__(self, phone, env=''):
        self.phone = phone
        self.xddd2 = xddd_pro(environment=env)
        database = DataBase()
        sql = 'UPDATE jgq.think_xsms SET code =1234,`status`=0 WHERE phone=%s;' % phone
        database.sql_execute(sql)
        login_headers = {
            'auth': 'xdef33',
            'system': 'android',
            'version': '4.3.4',
            'brand': 'LLD-AL00',
            'phoneversion': '9',
            'User-Agent': 'okhttp/3.11.0',
            'uuid': 'ffffffff-c268-090c-ffff-ffffdd0a6de5'
        }
        login_payload = {
            'phone': self.phone,
            'code': '1234'
        }
        res = self.xddd2.xddd2_login(headers=login_headers, params=login_payload)
        print('好单用户登录',res)
        token = res['data']['token']
        self.headers_data = {
            'auth': 'xdef33',
            'system': 'android',
            'version': '4.3.4',
            'phone': '13003672511',
            'brand': 'LLD-AL00',
            'phoneversion': '9',
            'User-Agent': 'okhttp/3.11.0',
            'uuid': 'ffffffff-c268-090c-ffff-ffffdd0a6de5',
            'token': token

        }

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
        return res

    # 好单客源列表
    def orderList(self, city_code):
        """
        :param city_code: 城市代码
        """
        payload = {
            'page': 1,
            'status': 0,
            'city_code': city_code,
            'insurance': 0,
            'isallgrab': 0,
            'iscangrab': 0,
            'incomemethod': 0,
            'isallgold': 0,
            'isallgood': 0,
            'issocial': 0,
            'iscar': 0,
            'iswld': 0,
            'isfund': 0,
            'iscommontype': 0,
            'ishouse': 0,
            'isHome': 2

        }
        res = self.xddd2.orderList(headers=self.headers_data, params=payload)
        return res

    # 更新展位状态
    def changeStatus(self, config_id, status):
        """
        :param config_id: 展位ID  1688
        :param status:   ( 1 待开启 2已开启 3已关闭 4系统关闭 0已删除 )
        """
        payload = {
            'config_id': config_id,
            'status': status
        }
        res = self.xddd2.changeStatus(headers=self.headers_data, datas=payload)
        print('更新展位状态',res)
        return res

    # 查询展位订单
    def catchOrderList(self,config_id):
        payload = {
            'config_id': config_id
        }
        res = self.xddd2.catchOrderList(headers=self.headers_data, datas=payload)
        print(res)
        boothOrderList = res['data']['data']
        return boothOrderList


if __name__ == "__main__":
    run = xdd2_manage('13003672511')
    print(run.orderList(520400))

