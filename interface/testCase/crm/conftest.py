# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件

import sys
import pytest
from interface.data.CRM_Account import username
from interface.testCaseManage.crm.crm_admin import crm_admin
from interface.testCaseManage.crm.crm_manage import crm_manage

# path = r'interface/testCase/crm/conftest.py'
# sys.path.append(path)


@pytest.fixture(scope='session')
def crmManege(cmdOption):
    crm = crm_manage(env=cmdOption, loginName=username['管理员'])
    return crm


@pytest.fixture(scope='session')
def crmAdmin(cmdOption):
    backend = crm_admin(env=cmdOption, loginName=username['dujun_gs_001'])
    return backend
