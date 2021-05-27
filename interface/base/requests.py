# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: requests.py
# @time: 2021/5/27 10:51
# @describe : requests方法封装

import requests
import json


class Base_requests:

    # post方法
    @staticmethod
    def post(url="", headers="", data=""):
        try:
            if headers == "":
                responses = requests.post(url=url, data=data)
                return responses
            else:
                responses = requests.post(url=url, headers=headers, data=data)
                return responses
        except:
            pass

    # post_json
    @staticmethod
    def post_json(url='', headers='', datas='', cookies=''):
        try:
            if headers == '':
                data_json = json.dumps(datas)
                header_data = {'Content-Type': 'application/json'}
                response = requests.post(url=url, headers=header_data, data=data_json, cookies=cookies)
                return response
            else:
                data_json = json.dumps(datas)
                response = requests.post(url=url, headers=headers, data=data_json, cookies=cookies)
                return response
        except:
            pass

    # get方法
    @staticmethod
    def get(url=None, headers=None, data=None):
        response = requests.get(url=url, headers=headers, data=data)
        return response.json()

    # post_cookie(登录接口使用，返回cookies信息)
    @staticmethod
    def post_login(url='', headers='', datas=''):
        data_json = json.dumps(datas)
        header_data = {'Content-Type': 'application/json'}
        response = requests.post(url=url, headers=header_data, data=data_json)
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie
