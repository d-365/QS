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
            'admin': 'http://testadmin.wanqiandaikuan.com/',
            'api': 'http://testapi.wanqiandaikuan.com/',
            'jdf': 'http://testjdf.wanqiandaikuan.com/'

        }
        return caps

    # 线上环境
    elif env == 'online':
        caps = {
            'admin': 'https://admin.91jiekuan.com/',

        }
        return caps
