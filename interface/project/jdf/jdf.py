# -*- coding: utf-8 -*-
# @author: dujun
# @software: PyCharm
# @file: jdf.py
# @time: 2021/5/31 15:19
# @describe : 信业帮App 项目

from interface.base.caps import Caps
from interface.base.requests import Base_requests


class jdf_pro:

    def __init__(self, environment=''):
        self.re = Base_requests()
        self.caps = Caps(env=environment)

    # 信业帮App,发布线索
    def firstLoan(self, headers='', datas=''):
        url = self.caps['jdf'] + 'api/h5/oneApply/firstLoan'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res

    # loanReject
    def loanReject(self, headers='', datas=''):
        """
        first请求后调用,新增线索
        :param headers:
        :param datas:
        :return:
        """
        url = self.caps['jdf'] + 'api/h5/oneApply/loanReject'
        res = self.re.post_json(url=url, headers=headers, datas=datas)
        return res
