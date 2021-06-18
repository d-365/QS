# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 10:38
# @Author  : dujun
# @File    : CRM_Account.py
# @describe:  CRM员工账号


username = {
    '管理员': 'manage_interface',
    '客户经理主管': 'khjlzg_interface',
    '客户经理': 'khjl_interface',
    '电核主管': 'dhzg_interface',
    '电核专员': 'dhzy_interface',
    'dujun_gs': 'dujun_gs'
}


# CRM员工账号
def account(user):
    payload = {
        'account': user,
        'password': 'e10adc3949ba59abbe56e057f20f883e',  # 123456
        'validate': "test"  # 校验码
    }
    return payload
