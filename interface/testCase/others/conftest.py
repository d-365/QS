# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件

import pytest

from interface.testCaseManage.api_manage.App_addOrder import addOrder


@pytest.fixture(scope='function')
def order():
    run = addOrder(phone='11111111121')
    return run
