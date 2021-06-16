# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: requests.py
# @time: 2021/5/27 10:51
# @describe : requests方法封装

import json

import requests


class Base_requests:

    @staticmethod
    def post(url, headers="", data="", cookies=''):
        responses = requests.post(url=url, headers=headers, data=data, cookies=cookies)
        return responses.json()

    @staticmethod
    def post_app(url, headers="", datas="", cookies=''):
        if headers == '':
            header = {
                'auth': '98ef33',
                'system': 'android',
                'version': '3.1.2'
            }
            responses = requests.post(url=url, headers=header, data=datas, cookies=cookies)
        else:
            responses = requests.post(url=url, headers=headers, data=datas, cookies=cookies)
        return responses.json()

    @staticmethod
    def post_json(url, headers='', datas='', cookies=''):
        data_json = json.dumps(datas)
        if headers == '':
            header_data = {'Content-Type': 'application/json'}
            response = requests.post(url=url, headers=header_data, data=data_json, cookies=cookies)
        else:
            response = requests.post(url=url, headers=headers, data=data_json, cookies=cookies)
        return response.json()

    # post_cookie(登录接口使用，返回cookies信息)
    @staticmethod
    def post_login(url, datas=''):
        data_json = json.dumps(datas)
        header_data = {'Content-Type': 'application/json'}
        response = requests.post(url=url, headers=header_data, data=data_json)
        print(response.json())
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie

    # Get
    @staticmethod
    def Get(url, headers='', params='', cookies=''):
        res = requests.get(url=url, headers=headers, params=params, cookies=cookies)
        return res.json()

    # get方法(带默认headers)
    @staticmethod
    def get(url, headers='', params=''):
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

    # get_cookie
    @staticmethod
    def get_cookie(url, headers='', params=''):
        response = requests.get(url=url, headers=headers, params=params)
        cookies = response.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        return cookie

    @staticmethod
    def put(url, headers='', ):
        response = requests.put(url=url, headers=headers)
        return response.json()
