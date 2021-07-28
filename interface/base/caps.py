# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: caps.py
# @time: 2021/5/27 11:24
# @describe : 环境切换

def Caps(env=''):
    # 测试环境
    if env == '':
        caps = {
            # 信贷多多后台
            'admin': 'http://testadmin.wanqiandaikuan.com/',
            # 信业帮App
            'api': 'http://testapi.wanqiandaikuan.com/',
            # 信业帮App
            'jdf': 'http://testjdf.wanqiandaikuan.com/',
            # CRM
            'crm': 'http://testdrkmanager.wanqiandaikuan.com/',
            # 多融客admin
            'crm_admin': 'http://testdrkadmin.wanqiandaikuan.com/',
            # 好单多多App
            'xddd2': 'http://testxddd2.wanqiandaikuan.com/',
            # CRM--电销开放平台
            'tmk': 'http://testdrktm.wanqiandaikuan.com/'
        }
        return caps

    # 线上环境
    elif env == 'online':
        caps = {
            # 信贷多多后台
            'admin_old': 'https://admin.91jiekuan.com/',
            # CRM + 多融客 后台
            'crm': 'https://drkmanager.wanqiandaikuan.com/'
        }
        return caps
