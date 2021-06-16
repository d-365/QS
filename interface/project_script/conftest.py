# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 17:57
# @Author  : dujun
# @File    : conftest.py
# @describe: 项目脚本配置文件
import pytest

from ..testCaseManage.api_manage.App_addOrder import addOrder
from ..tools.dataBase import DataBase


@pytest.fixture(scope='session')
def mysql():
    return DataBase()


@pytest.fixture(scope='session')
def addOrd_manege():
    return addOrder()


# 用户账号数据
@pytest.fixture(scope='session')
def Account_data():
    pass
