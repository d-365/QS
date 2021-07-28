# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 10:21
# @Author  : dujun
# @File    : user.py.py
# @describe: 好单后台--user

from loguru import logger
from interface.base.base_request import base_requests
from interface.base.caps import Caps
from interface.tools.dataBase import DataBase


class user_pro:

    def __init__(self, phone, environment=''):
        self.re = base_requests()
        self.caps = Caps(env=environment)
        self.database = DataBase()
        # 重置信贷多多后台用户登录验证码
        sql1 = "UPDATE admin.think_sms SET code =1234,`status`=0 WHERE phone={};".format(phone)
        # 好单后台登录
        login_data = {"phone": phone, "code": "1234"}
        self.header_data = {'Content-Type': 'application/json'}
        self.database.sql_execute(sql=sql1)
        login_url = self.caps['admin'] + '/api/sms/interface/dologin'
        self.re.request(method='post', headers=self.header_data, data_is_json=True, url=login_url, data=login_data)

    # 查询订单详情
    def orderList(self, phone):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/order/OrderList'
        payload = {
            'phone': phone, 'grabTime': None, 'page': '1', 'pageSize': '10'
        }

        res = self.re.request(method='post', data_is_json=True, url=url, data=payload, headers=self.header_data)
        print(res)

    # 获取用户列表信息
    def GetUserList(self, phone):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/userList/GetUserList'
        payload = {
            "phone": phone,
            "page": 1
        }
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.header_data, data=payload)
        uid = res['data']['data'][0]['id']
        return uid

    # 获取用户列表信息
    def releaseRiskUser(self, uid):
        url = self.caps['admin'] + 'api/v2.0.0/UserInformation/riskUser/releaseRiskUser'
        payload = {
            'xuser_id': uid,
            'reason': "interface"
        }
        res = self.re.request(method='post', url=url, data_is_json=True, headers=self.header_data, data=payload)
        logger.debug(res)


if __name__ == '__main__':
    run = user_pro(phone='17637898368')
