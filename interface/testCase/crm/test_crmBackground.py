# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 16:31
# @Author  : dujun
# @File    : test_crmBackground.py
# @describe: CRM管理后台
import time
import allure
from interface.data.order_data import order_data
from interface.tools.dataBase import DataBase


@allure.feature('CRM订单分配流程')
class Test_process:

    def teardown_function(self):
        mysql = DataBase()
        sql = ''
        mysql.sql_execute()

    @allure.story('关闭截单,均不符合(展位+不需电核广告)-->进入好单客源')
    def test_case1(self, crmManege, mysql, appAddOrder, appXdd2, crmAdmin):
        """
        登录CRM后台关闭截单按钮
        查询数据库，关闭所有开启展位
        禁用所有需电核广告
        发起线索———>进入好单客源查看对应订单
        """
        status_re = crmManege.getStatus()
        status = status_re['data']['status']
        if status:
            crmManege.cutStatus(0)
        else:
            pass
        sql1 = "SELECT * FROM jgq.think_xzw_config_log WHERE `status` = 2;"
        booth = mysql.sql_execute(sql1)
        if booth:
            print('存在已开启的展位')
            sql2 = "update jgq.think_xzw_config_log SET `status` = 3;"
            mysql.sql_execute(sql2)
        else:
            print("不存在开启的展位")
        with allure.step('禁用所有需电核广告'):
            advertList = crmManege.advertisingList(0)
            for i in range(0, len(advertList)):
                advertID = advertList[i]['id']
                crmAdmin.editAdIsOpen(advertID, isOpen='false')
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
        with allure.step('好单客源校验'):
            time.sleep(2)
            orderList = appXdd2.orderList(520400)  # 安顺市
            for i in range(0, len(orderList['data']['data'])):
                if loanId == orderList['data']['data'][i]['id']:
                    break
                else:
                    raise Exception("订单ID不在好单客源")
            print('-----------------------关闭截单,均不符合(展位+不需电核广告)-->进入好单客源----------------------------')

    @allure.story('关闭截单,符合展位-->进入好单客源')
    def test_case2(self, crmManege, mysql, appAddOrder, appXdd2, crmAdmin):
        """
        登录CRM后台关闭截单按钮
        查询数据库，关闭所有开启展位--打开对应展位
        发起线索———>展位查询对应线索
        """
        with allure.step('登录CRM后台关闭截单按钮'):
            status_re = crmManege.getStatus()
            status = status_re['data']['status']
            if status:
                crmManege.cutStatus(0)
            else:
                pass
        with allure.step('查询数据库，关闭所有开启展位,开启对应展位'):
            sql1 = "SELECT * FROM jgq.think_xzw_config_log WHERE `status` = 2;"
            booth = mysql.sql_execute(sql1)
            if booth:
                print('存在已开启的展位')
                sql2 = "update jgq.think_xzw_config_log SET `status` = 3;"
                mysql.sql_execute(sql2)
            else:
                print("不存在开启的展位")
            # 开启对应展位
            appXdd2.changeStatus(config_id='1688', status=2)
        with allure.step('禁用所有不需电核广告'):
            advertList = crmManege.advertisingList(0)
            for i in range(0, len(advertList)):
                advertID = advertList[i]['id']
                crmAdmin.editAdIsOpen(advertID, isOpen='false')
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
        with allure.step('展位校验'):
            time.sleep(1)
            boothOrderList = appXdd2.catchOrderList(1688)
            boothOrderID = boothOrderList[0]['id']
            assert loanId == boothOrderID
            print('-----------------------关闭截单,符合展位-->进入展位--------------------------')

    @allure.story('关闭截单,不符合展位，符合不需电核广告-->进入好单客源')
    def test_case3(self, crmManege, mysql, appAddOrder, appXdd2, crmAdmin):
        """
        关闭全部展位
        关闭所有不需电核的广告
        打开不需电核的广告，查询线索余量，不足进行充值
        查询对应广告下是否存在此订单
        """
        with allure.step('登录CRM后台关闭截单按钮'):
            status_re = crmManege.getStatus()
            status = status_re['data']['status']
            if status:
                crmManege.cutStatus(0)
            else:
                pass
        with allure.step('查询数据库，关闭所有展位'):
            sql1 = "SELECT * FROM jgq.think_xzw_config_log WHERE `status` = 2;"
            booth = mysql.sql_execute(sql1)
            if booth:
                print('存在已开启的展位')
                sql2 = "update jgq.think_xzw_config_log SET `status` = 3;"
                mysql.sql_execute(sql2)
            else:
                print("不存在开启的展位")
        with allure.step('禁用所有不需电核广告, 开启对应广告CRM+多融客'):
            advertList = crmManege.advertisingList(0)
            for i in range(0, len(advertList)):
                advertID = advertList[i]['id']
                crmAdmin.editAdIsOpen(advertID, isOpen='false')
            # 开启对应广告CRM+多融客
        with allure.step('查询线索余量，不足进行充值'):
            pass
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
        with allure.step('查询对应广告下是否存在此订单'):
            pass

    @allure.story('开启截单,CRM置为电核单--->进入好单客源')
    def test_case4(self, crmManege, mysql, appAddOrder, appXdd2, crmAdmin):
        """
        开启截单
        CRM置位电核单
        推送好单客源，断言
        """
        with allure.step('登录CRM后台开启截单按钮'):
            status_re = crmManege.getStatus()
            status = status_re['data']['status']
            if status:
                pass
            else:
                crmManege.cutStatus(1)
        with allure.step('CRM添加需电核的广告,条件不限制'):
            pass
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
        with allure.step('CRM对应线索置为电核单'):
            time.sleep(2)
            crmManege.setOrder(loanId)
        with allure.step('好单客源断言'):
            time.sleep(2)
            orderList = appXdd2.orderList(520400)  # 安顺市
            # 订单ID是否在好单客源
            for i in range(0,len(orderList['data']['data'])):
                if loanId == orderList['data']['data'][i]['id']:
                    if orderList['data']['data'][i]['callFlag'] is True:
                        break
                    else:
                        raise Exception("订单进入好单客源但不是电核单")
                else:
                    raise Exception("订单ID不在好单客源 或 不是电核单")
            # 订单是否是电核单
            print('----------------------开启截单 , CRM置为电核单--->进入好单客源---------------------------')
