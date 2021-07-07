# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 17:55
# @Author  : dujun
# @File    : create_count.py
# @describe: 注册信业帮用户

from interface.project.api.api import api_pro
from interface.tools.dataBase import DataBase


class create_count:

    def __init__(self, phone):
        env = ''
        mysql = DataBase()
        sql = "insert INTO jgq.think_sms (phone,code) VALUES(%s,'1234')" % phone
        mysql.sql_execute(sql)
        xinYe_api = api_pro(environment=env)

        payload = {
            'phone': phone,
            'code': 1234,
            'device_token': 'AhGJMV5mG - XzV1hO8F_9PW - RlCTsvj6_kcr__rACf5ih',
            'isCover': 0
        }
        res = xinYe_api.user_login(data=payload)
        print(res)


if __name__ == "__main__":
    lists = []
    for i in range(0, 1):
        phones = 13003672505 + i
        lists.append(phones)
        run = create_count(str(phones))
