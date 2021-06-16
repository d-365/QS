# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件

import pytest

from interface.testCaseManage.api_manage.App_addOrder import addOrder


@pytest.fixture(scope='session')
def order():
    run = addOrder()
    run.test_sql('11111111121')
    run.app_login('11111111121')
    return run
