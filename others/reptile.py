# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 11:32
# @Author  : dujun
# @File    : reptile.py
# @describe:
import re

import requests


def get_one_page(url):
    res = requests.get(url=url)
    if res.status_code == 200:
        return res.text
    else:
        print('请求失败')


def main():
    url = 'http://testdrkmanager.wanqiandaikuan.com/user/login'
    res_html = get_one_page(url=url)
    return res_html


def parse_one_page(html_code):
    pattern = re.compile('<noscript>(.*?)</noscript>', re.S)
    items = re.findall(pattern, html_code)
    print(items)


if __name__ == "__main__":
    html = main()
    parse_one_page(html_code=html)
