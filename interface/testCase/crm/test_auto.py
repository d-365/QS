# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 11:55
# @Author  : dujun
# @File    : test_auto.py
# @describe: CRM系统各菜单接口自动化判断

import random

import allure
import pytest

from interface.data.order_data import order_data
from interface.testCaseManage.crm.crm_general import crm_general


@allure.feature('财务管理')
class Test_finance:

    @allure.story('账户充值')
    def test_recharge(self, crmManege, crmAdmin):
        # 充值金额
        price = random.randint(1, 20)
        print('本次充值金额数据为：', price)
        # 充值公司
        companyName = 'dujun_gs_001'

        with allure.step('输入负数进行充值,提示：参数不正确'):
            message1 = '参数不正确'
            re1 = crmManege.recharge(companyName, -5)
            assert re1['msg'] == message1
        with allure.step('输入不存在公司进行充值,提示：系统异常'):
            message2 = '系统异常'
            re2 = crmManege.recharge('不存在公司', price)
            assert re2['msg'] == message2
        with allure.step('输入任意公司,可充值成功'):
            detail_before = crmAdmin.detail()
            money_before = detail_before['data']['money']
            re3 = crmManege.recharge(companyName, price)
            detail_after = crmAdmin.detail()
            money_after = detail_after['data']['money']
            # 公司余额断言
            assert money_after == (money_before + price)
            # CRM公司充值记录断言
            rechargeList = crmManege.rechargeList(companyName=companyName)
            for i in range(len(rechargeList)):
                if price == rechargeList[i]['threadMoney']:
                    break
                else:
                    raise Exception("对应公司财务管理,充值记录下未找到对应充值记录")
            # 多融客公司充值记录断言
            record_list = crmAdmin.record(types='0')
            for i in range(len(record_list)):
                if price == record_list[i]['threadMoney']:
                    break
                else:
                    raise Exception("多融客账户充值记录下未找到对应充值记录")
            print('-' * 20 + "账户充值(负数,不存在公司,公司余额断言,CRM公司充值记录断言,多融客公司充值记录断言)" + '-' * 20)

    @allure.story('账户退款')
    def test_refund(self, crmManege, crmAdmin):

        # 退款公司
        companyName = 'dujun_gs_001'
        price = 5

        with allure.step('禁用该公司下所有广告'):
            crmManege.recharge(companyName, price)
            advertList = crmManege.advertisingList(companyName=companyName)
            for i in range(0, len(advertList)):
                advertID = advertList[i]['id']
                crmManege.openStatus(ID=advertID, isOpen='0')

        with allure.step('输入负数进行退款,提示：参数不正确'):
            message1 = '参数不正确'
            re1 = crmManege.refund(companyName, -5)
            assert re1['msg'] == message1

        with allure.step('退款金额大于账户余额,提示：退款金额不能大于账户余额'):
            message2 = '退款金额不能大于账户余额'
            detail_before = crmAdmin.detail()
            money_before = detail_before['data']['money']
            re2 = crmManege.refund(companyName, (money_before + price))
            assert re2['msg'] == message2

        with allure.step('退款金额小于账户余额,可退款'):
            detail_before = crmAdmin.detail()
            money_before = detail_before['data']['money']

            crmManege.refund(companyName, money_before)

            detail_after = crmAdmin.detail()
            money_after = detail_after['data']['money']
            # 公司余额断言
            assert money_after == (money_before - money_before)
            # CRM公司退款记录断言
            rechargeList = crmManege.consumeList(companyName=companyName)
            for i in range(len(rechargeList)):
                if money_before == rechargeList[i]['threadMoney']:
                    break
                else:
                    raise Exception("对应公司财务管理,退款记录下未找到对应退款记录")
            # 多融客账户退款记录断言
            record_list = crmAdmin.record(types='1')
            for i in range(len(record_list)):
                if money_before == record_list[i]['threadMoney']:
                    break
                else:
                    raise Exception("多融客账户退款记录下未找到对应退款记录")
            print('-' * 20 + "账户退款(负数,退款金额大于账户余额,公司余额断言,CRM公司退款记录断言,多融客账户退款记录断言)" + '-' * 20)

    @allure.story('消耗记录')
    def test_consumeList(self, crmManege, crmAdmin, appAddOrder):

        with allure.step('发起线索,推送定制需电核广告'):
            companyName = 'dujun_gs_001'
            cpcPrice = 25
            adName = ''
            electricalStatus = 1
            push_data = crm_general().push_order(companyName=companyName,adName=adName, electricalStatus=electricalStatus, cpcPrice=cpcPrice)
            loanId = push_data[0]
        with allure.step('CRM+多融客消耗列表断言'):
            # CRM财务管理消耗记录断言
            consumeList = crmManege.consumeList(companyName=companyName, adName=adName)
            for i in range(len(consumeList)):
                if cpcPrice == consumeList[i]['threadMoney'] and loanId == consumeList[i]['loanId'] and adName == \
                        consumeList[i]['adName']:
                    break
                else:
                    raise Exception("对应公司财务管理,消耗记录下未找到对应消耗记录")
            # 多融客账户消耗记录断言
            record_list = crmAdmin.record(types='1')
            for i in range(len(record_list)):
                if cpcPrice == record_list[i]['threadMoney']:
                    break
                else:
                    raise Exception("多融客账户消耗记录下未找到对应消耗记录")
            print('-' * 20 + "消耗记录(负数,退款金额大于账户余额,公司余额断言,CRM公司退款记录断言,多融客账户退款记录断言)" + '-' * 20)


@allure.feature('多融客--客户管理')
class Test_customerManage:

    @pytest.fixture(scope='function')
    def setup_pushOrder(self):
        companyName = 'dujun_gs_001'
        cpcPrice = 25
        adName = 'custom_yes'
        electricalStatus = 1
        push_data = crm_general().push_order(companyName=companyName,adName=adName, electricalStatus=electricalStatus, cpcPrice=cpcPrice)
        return push_data

    @allure.story('多融客户全部线索_订单详情校验')
    def test_case1(self, crmAdmin, setup_pushOrder):
        with allure.step('发起线索--推送广告'):
            loanId = setup_pushOrder[0]
        with allure.step('用户发起订单数据与全部线索内订单数据断言'):
            order_datas = order_data(city_name='安顺市')
            customerDetail_list = crmAdmin.customerDetail(Id=loanId)

    @allure.story('多融客户全部线索_订单分配至我的线索,退还公海')
    def test_case2(self, crmAdmin, setup_pushOrder):
        with allure.step('发起线索--推送广告'):
            loanId = setup_pushOrder[0]
            adId = setup_pushOrder[1]
        with allure.step('订单分配至我的线索,断言'):
            crmAdmin.allotCustomer(ids=[loanId])
            myCustomerList = crmAdmin.myCustomerList(adId=adId)
            for i in range(len(myCustomerList)):
                if loanId == myCustomerList[i]['id']:
                    break
                else:
                    raise Exception(loanId, "不在我的线索中")
        with allure.step('订单放入公海'):
            crmAdmin.throwCustomer(loanId=loanId)
            # 我的线索进行断言(不存在我的线索)
            myCustomerList = crmAdmin.myCustomerList(adId=adId)
            i = 0
            while i < len(myCustomerList):
                if loanId == myCustomerList[i]['id']:
                    raise AssertionError(loanId, '此订单依然在我的线索中')
                else:
                    i += 1
            # 公海进行断言（在公海）
            commonCustomerList = crmAdmin.commonCustomerList(adId=adId)
            for i in range(len(commonCustomerList)):
                if loanId == commonCustomerList[i]['id']:
                    break
                else:
                    raise Exception(loanId, "不在公海中")

    @allure.story('多融客公海_我来跟进')
    def test_case3(self, crmAdmin, setup_pushOrder):
        with allure.step('发起线索--推送广告'):
            loanId = setup_pushOrder[0]
            adId = setup_pushOrder[1]
        with allure.step('我来跟进'):
            crmAdmin.followCustomer(loanId=loanId)
            # 断言订单在我的线索中
            myCustomerList = crmAdmin.myCustomerList(adId=adId)
            for i in range(len(myCustomerList)):
                if loanId == myCustomerList[i]['id']:
                    break
                else:
                    raise Exception(loanId, "不在我的线索中")
            # 断言线索不在公海中
            commonCustomerList = crmAdmin.commonCustomerList(adId=adId)
            i = 0
            while i < len(commonCustomerList):
                if loanId == commonCustomerList[i]['id']:
                    raise AssertionError(loanId, '此订单依然在公海中')
                else:
                    i += 1


@allure.feature('CRM产品列表')
class Test_product:

    @pytest.fixture(scope='function')
    def add_product(self, crmManege):
        companyName = 'dujun_gs_001'
        productName = '测试产品'
        description = '产品描述'
        product_data = {"productName": productName, "companyName": companyName, "loanLinesMin": 5, "loanLinesMax": 5,
                        "loanDeadlineMin": 5, "loanDeadlineMax": 5, "rateUnit": 2, "rateMin": 5, "rateMax": 5,
                        "oneTimeCost": 5, "loanTimeMin": 5, "loanTimeMax": 5, "description": description}
        crmManege.add(product_data)

        return product_data

    @allure.story("添加产品")
    def test_case1(self, crmManege, add_product):
        with allure.step('新增产品'):
            pass
        with allure.step('产品列表断言'):
            product_list = crmManege.product_list(companyName=add_product['companyName'],
                                                  productName=add_product['productName'])
            assert product_list[0]['loanLinesMin'] == add_product['loanLinesMin']
            assert product_list[0]['loanLinesMax'] == add_product['loanLinesMax']
            assert product_list[0]['loanDeadlineMin'] == add_product['loanDeadlineMin']
            assert product_list[0]['loanDeadlineMax'] == add_product['loanDeadlineMax']
            assert product_list[0]['rateUnit'] == add_product['rateUnit']
            assert product_list[0]['rateMin'] == add_product['rateMin']
            # assert product_list[0]['rateMax'] == product_data['rateMax']
            assert product_list[0]['oneTimeCost'] == add_product['oneTimeCost']
            assert product_list[0]['loanTimeMin'] == add_product['loanTimeMin']
            assert product_list[0]['loanTimeMax'] == add_product['loanTimeMax']
            assert product_list[0]['description'] == add_product['description']

    @allure.story("删除产品_未绑定广告")
    def test_case2(self, crmManege, add_product):
        with allure.step('删除产品_未绑定广告'):
            product_list = crmManege.product_list(companyName=add_product['companyName'],
                                                  productName=add_product['productName'])
            product_ID = product_list[0]['id']
            crmManege.delete_product(product_ID)
        with allure.step('断言产品列表,产品已不在产品列表'):
            product_list_after = crmManege.product_list(companyName=add_product['companyName'],
                                                        productName=add_product['productName'])
            assert len(product_list_after) == 0
            print('-' * 20 + "产品未绑定广告进行删除,删除成功" + '-' * 20)

    @allure.story("删除产品_已绑定广告")
    def test_case3(self, crmManege, add_product):
        with allure.step('删除产品_已绑定广告'):
            product_list = crmManege.product_list(companyName=add_product['companyName'],
                                                  productName=add_product['productName'])
            product_ID = product_list[0]['id']
        with allure.step('添加广告,选择已添加产品'):
            companyName = "dujun_gs_001"
            advertisingName = 'custom_no'
            customPlan = 1
            electricalStatus = 0
            productName = add_product['productName']
            ad_data = {"companyName": companyName, "advertisingName": advertisingName,
                       "electricalStatus": electricalStatus, "putCity": "全国",
                       "status": 1,
                       "suggestedPrice": 6, "requirement": {}, "noRequirement": {}, "customPlan": customPlan,"productName":productName}
            crmManege.addAdvertising(payload=ad_data)
            crmManege.delete_product(product_ID)
        with allure.step('断言产品在产品列表'):
            product_list_after = crmManege.product_list(companyName=add_product['companyName'],
                                                        productName=add_product['productName'])
            i = 0
            status = False
            while i < len(product_list_after):
                if product_ID == product_list_after[i]['id']:
                    status = True
                    break
                else:
                    i += 1
            if status is True:
                print('-' * 20 + "产品绑定广告进行删除,无法删除" + '-' * 20)
            else:
                raise Exception('-' * 20 + "产品绑定广告进行删除,删除成功" + '-' * 20)


@allure.feature('广告管理')
class Test_advertising:

    @pytest.fixture(scope='class')
    # 创建广告
    def add_advert(self):
        companyName = "dujun_gs_001"
        advertisingName = random.randint(0, 99999)
        electricalStatus = 1
        customPlan = 1
        ad_data = {"companyName": companyName, "advertisingName": advertisingName, "electricalStatus": electricalStatus,
                   "putCity": "全国", "status": 1, "suggestedPrice": 6, "customPlan": customPlan, "requirement": {},
                   "noRequirement": {}, "remark": "interface"}
        adID = crm_general().add_Advertising(ad_data=ad_data, cpcPrice=25)
        return adID, ad_data

    @allure.story('添加广告')
    def test_case1(self):
        pass

    @allure.story('删除广告')
    def test_case2(self, add_advert, crmManege):
        crmManege.delete_advertising(adID=add_advert[0])
        with allure.step('广告列表断言'):
            advertList = crmManege.advertisingList(companyName=add_advert[1]['companyName'],
                                                   advertisingName=add_advert[1]['advertisingName'])
            assert len(advertList) == 0
            print('-' * 20 + '删除广告成功' + '-' * 20)
