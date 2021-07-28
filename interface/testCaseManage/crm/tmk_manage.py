# -*- coding: utf-8 -*-
# @Time    : 2021/7/21 16:53
# @Author  : dujun
# @File    : tmk_manage.py
# @describe: 电销开放平台
from interface.data.CRM_Account import account, tmkUser
from interface.data.order_data import crm_order_data
from interface.project.crm.tmk import tmk_pro


class tmk:
    def __init__(self, loginName, env=''):
        self.tmk = tmk_pro(environment=env)
        payload = account(user=loginName)
        re = self.tmk.login(datas=payload)
        self.token = re['data']['token']
        self.headers = {
            "Content-Type": "application/json",
            'token': self.token
        }

    # 电销开放平台-填单
    def apply(self, phone, cityName):
        payload = crm_order_data(phone=phone, cityName=cityName)
        res = self.tmk.apply(headers=self.headers, datas=payload)
        print('电销平台填单', res)
        return res


if __name__ == '__main__':
    run = tmk(loginName=tmkUser['分代理'])
    run.apply(phone='', cityName='')
