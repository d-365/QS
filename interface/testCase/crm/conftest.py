# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件

import pytest
from interface.data.CRM_Account import username
from interface.testCaseManage.crm.crm_admin import crm_admin
from interface.testCaseManage.crm.crm_manage import crm_manage
from interface.testCaseManage.xdd2_manage.xdd2_manage import xdd2_manage
from interface.tools.dataBase import DataBase
from interface.testCaseManage.api_manage.App_addOrder import addOrder


# path = r'interface/testCase/crm/conftest.py'
# sys.path.append(path)

# CRM后台
@pytest.fixture(scope='session')
def crmManege(cmdOption):
    crm = crm_manage(env=cmdOption, loginName=username['管理员'])
    return crm


# 多融客后台
@pytest.fixture(scope='session')
def crmAdmin(cmdOption):
    backend = crm_admin(env=cmdOption, loginName=username['dujun_gs'])
    return backend


@pytest.fixture(scope='session')
def mysql():
    database = DataBase()
    return database


# 信业帮App
@pytest.fixture(scope='session')
def appAddOrder(cmdOption):
    app_order = addOrder(env=cmdOption,phone='11111111119')
    return app_order


# 好单多多App
@pytest.fixture(scope='session')
def appXdd2(cmdOption):
    xdd2_res = xdd2_manage(env=cmdOption,phone='13003672511')
    return xdd2_res
