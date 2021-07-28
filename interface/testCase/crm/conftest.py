# -*- coding: utf-8 -*-
# @Time    : 2021/6/4 16:10
# @Author  : dujun
# @File    : conftest.py
# @describe: conftest配置文件
import time

import pytest
from faker import Faker

from interface.data.CRM_Account import username, tmkUser
from interface.project.crm.tmk import tmk_pro
from interface.testCaseManage.api_manage.App_addOrder import addOrder
from interface.testCaseManage.crm.crm_admin import crm_admin
from interface.testCaseManage.crm.crm_manage import crm_manage
from interface.testCaseManage.xdd2_manage.xdd2_manage import xdd2_manage
from interface.tools.dataBase import DataBase

# path = r'interface/testCase/crm/conftest.py'
# sys.path.append(path)

setting = {
    'api_phone': 18397858213  # 信业帮手机号
}


# 电销开放平台后台---总代理账号
@pytest.fixture(scope='function')
def tmk(cmdOption):
    tmk = tmk_pro(environment=cmdOption, loginName=tmkUser['总代理账号'])
    return tmk


# 电销开放平台后台---分代理账号
@pytest.fixture(scope='function')
def tmk_sub(cmdOption):
    tmk_sub = tmk_pro(environment=cmdOption, loginName=tmkUser['分代理账号'])
    return tmk_sub


# CRM后台
@pytest.fixture(scope='session')
def crmManege(cmdOption):
    crm = crm_manage(env=cmdOption, loginName=username['管理员'])
    return crm


# 多融客后台
@pytest.fixture(scope='module')
def crmAdmin(cmdOption):
    backend = crm_admin(env=cmdOption, loginName='interface_gs_manage')
    return backend


# 数据库
@pytest.fixture(scope='session')
def mysql():
    database = DataBase()
    return database


# 信业帮App
@pytest.fixture(scope='function')
def appAddOrder(cmdOption):
    app_order = addOrder(env=cmdOption, phone=setting['api_phone'])
    return app_order


# 好单多多App
@pytest.fixture(scope='function')
def appXdd2(cmdOption):
    xdd2_res = xdd2_manage(env=cmdOption, phone='13003672511')
    return xdd2_res


# faker造数据
@pytest.fixture(scope='session')
def faker(cmdOption):
    f = Faker(locale='zh_CN')
    return f


@pytest.fixture(scope='class')
def setup_process(crmManege, mysql):
    """
    1:关闭手动截单按钮，关闭自动截单按钮
    2:关闭所有展位信息（安顺市）
    3:清除自动化产生广告数据
    4;关闭所有非定制非电核广告
    """
    crmManege.cutStatus(types=1, status=0)
    crmManege.cutStatus(types=2, status=0)
    select_booth = "SELECT * FROM jgq.think_xzw_config_log WHERE `status` = 2;"
    booth = mysql.sql_execute(select_booth)
    if booth:
        print('存在已开启的展位')
        close_booth = "update jgq.think_xzw_config_log SET `status` = 3;"
        mysql.sql_execute(close_booth)
    else:
        print("不存在开启的展位")

    sql = "delete  from crm.crm_advertising WHERE company_name = 'dujun_gs_001' and advertising_name ='custom_yes' OR advertising_name ='custom_no' OR advertising_name ='common_no';"
    mysql.sql_execute(sql)
    dataTime = time.strftime('%Y-%m-%d', time.localtime())
    sql2 = "UPDATE jgq.think_xzw_city_ordernum_config SET nums = 100 WHERE city_name = '安顺市' and time = '%s' " % dataTime
    mysql.sql_execute(sql2)
    advertList = crmManege.advertisingList(electricalStatus='0')
    for i in range(len(advertList)):
        advertID = advertList[i]['id']
        crmManege.openStatus(ID=advertID, isOpen='0')
