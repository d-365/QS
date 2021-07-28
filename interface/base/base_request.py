# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 15:03
# @Author  : dujun
# @File    : base_request.py
# @describe: requests方法封装
import json

import requests
from requests.adapters import HTTPAdapter


class base_requests:

    def __init__(self, timeout=20):
        self.session = requests.Session()
        # 接口失败重试次数
        self.session.mount('http://', HTTPAdapter(max_retries=3))
        self.session.mount('https://', HTTPAdapter(max_retries=3))
        self.timeout = timeout

    def request(self, method, url, headers='', data='', data_is_json=False):
        if data_is_json is True:
            data = json.dumps(data)

        if method.lower() == 'get':
            res = self.session.get(url=url, headers=headers, params=data,data=data)
            return res.json()
        elif method.lower() == 'post':
            res = self.session.post(url=url, headers=headers, data=data)
            return res.json()
        elif method.lower() == 'delete':
            res = self.session.delete(url=url, headers=headers)
            return res.json()
        elif method.lower() == 'options':
            res = self.session.options(url=url, headers=headers)
            return res.json()
        elif method.lower() == 'put':
            res = self.session.put(url=url, headers=headers)
            return res.json()
        elif method.lower() == 'test':
            print(url, headers)

    # 关闭会话
    def close(self):
        self.session.close()


if __name__ == '__main__':
    def case(e, *args):
        data = args
        print(data)
