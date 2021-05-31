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
                return response.json()
            else:
                data_json = json.dumps(datas)
                response = requests.post(url=url, headers=headers, data=data_json, cookies=cookies)
                return response.json()
        except:
            pass

    # get方法
    @staticmethod
    def get(url='', headers='', params=''):
        if headers == '':
            header = {
                'auth': '98ef33',
                'system': 'android',
                'version': '3.1.2'
            }
            response = requests.get(url=url, headers=header, params=params)
        else:
            response = requests.get(url=url, headers=headers, params=params)
        return response.json()

    # post_cookie(登录接口使用，返回cookies信息)
    @staticmethod
    def post_login(url='', datas=''):
        data_json = json.dumps(datas)
        header_data = {'Content-Type': 'application/json'}
        response = requests.post(url=url, headers=header_data, data=data_json)
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie

    # get_cookie
    @staticmethod
    def get_cookie(url='', headers='', params=''):
        response = requests.get(url=url, headers=headers, params=params)
        print(response.json())
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie
