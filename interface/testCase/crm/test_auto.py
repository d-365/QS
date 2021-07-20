# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 11:55
# @Author  : dujun
# @File    : test_auto.py
# @describe: CRM系统各菜单接口自动化判断

import random
import time

import allure
import pytest
from faker import Faker
from loguru import logger

from interface.data.order_data import order_data
from interface.testCaseManage.crm.crm_general import crm_general
from interface.tools.assert_custom import custom_assert
from .conftest import setting


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
            crmManege.recharge(companyName, price)
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
            rechargeList = crmManege.refundList(companyName=companyName)
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
            f = Faker(locale='zh_CN')
            adName = f.user_name()
            electricalStatus = 1
            push_data = crm_general().push_order(companyName=companyName, adName=adName,
                                                 electricalStatus=electricalStatus, cpcPrice=cpcPrice)
            loanId = push_data[0]
        with allure.step('CRM+多融客消耗列表断言'):
            # CRM财务管理消耗记录断言
            time.sleep(1)
            consumeList = crmManege.consumeList(companyName=companyName, adName=adName)
            i = 0
            while i < len(consumeList):
                if cpcPrice == consumeList[i]['comsumeMoney'] and loanId == consumeList[i]['thinkLoanId'] and adName == \
                        consumeList[i]['adName']:
                    status = True
                    break
                else:
                    i += 1
            if status is True:
                pass
            else:
                raise Exception("CRM消耗记录未查询对应订单")
            # 多融客账户消耗记录断言
            time.sleep(1)
            record_list = crmAdmin.record(types=2)
            print(record_list)
            if cpcPrice == record_list[i]['threadMoney']:
                print('-' * 20 + "消耗记录(负数,退款金额大于账户余额,公司余额断言,CRM公司退款记录断言,多融客账户退款记录断言)" + '-' * 20)
            else:
                raise Exception("多融客账户消耗记录下未找到对应消耗记录")


@allure.feature('多融客--客户管理')
class Test_customerManage:

    @pytest.fixture(scope='function')
    def setup_pushOrder(self):
        companyName = 'dujun_gs_001'
        cpcPrice = 25
        f = Faker(locale='zh_CN')
        adName = f.word()
        electricalStatus = 1
        push_data = crm_general().push_order(companyName=companyName, adName=adName, electricalStatus=electricalStatus,
                                             cpcPrice=cpcPrice)
        return push_data

    @allure.story('多融客户全部线索_订单分配至我的线索,退还公海')
    def test_case1(self, crmAdmin, setup_pushOrder):
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
    def test_case2(self, crmAdmin, setup_pushOrder):
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
        f = Faker(locale='zh_CN')
        productName = f.word()
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
                       "suggestedPrice": 6, "requirement": {}, "noRequirement": {}, "customPlan": customPlan,
                       "productName": productName, 'productId': product_ID}
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


@allure.feature('电销中心')
@pytest.mark.usefixtures('setup_process')
class Test_telemarketing:
    """
   1:关闭自动截单 + 人工截单
   2:关闭展位 + 非定制非电核广告
   """

    @allure.story('信业帮发起线索,电销列表校验')
    def test_case1(self, appAddOrder, crmManege):
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
            logger.debug('loanID----{}'.format(loanId))
        with allure.step('电销中心列表断言'):
            electrical_lists = crmManege.electrical(phone=setting['api_phone'])
            custom_assert().dict_json_include(expect_key='id', expect_value=loanId, dict_data=electrical_lists)
        with allure.step('保存订单,电销列表校验'):
            crmManege.electrical_save(loanID=loanId)
            electrical_lists_after = crmManege.electrical(phone=setting['api_phone'])
            i = 0
            while i < len(electrical_lists_after):
                assert loanId not in electrical_lists_after[i]
                i += 1

    @allure.story("发起线索,电销列表保存,推送")
    def test_case2(self, appAddOrder, crmManege):
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
            logger.debug('loanID----{}'.format(loanId))
        with allure.step('创建【定制—需电核】广告 custom_yes'):
            companyName = "dujun_gs_001"
            advertisingName = 'custom_yes'
            customPlan = 1
            electricalStatus = 1
            ad_data = {"companyName": companyName, "advertisingName": advertisingName,
                       "electricalStatus": electricalStatus, "putCity": "全国",
                       "status": 1,
                       "suggestedPrice": 6, "requirement": {}, "noRequirement": {}, "customPlan": customPlan}
            advert_id = crm_general().add_Advertising(ad_data=ad_data, cpcPrice=25)
        with allure.step('电销详情,保存订单'):
            crmManege.electrical_save(loanID=loanId)
        with allure.step('校验定制需电核广告列表'):
            eligible_lists = crmManege.eligible_list(loanID=loanId)
            custom_assert().dict_json_include(expect_key='id', expect_value=advert_id, dict_data=eligible_lists)
            custom_assert().dict_json_include(expect_key='companyName', expect_value=companyName,
                                              dict_data=eligible_lists)
        with allure.step('推送对应订单至定制需电核广告'):
            time.sleep(1)
            crmManege.eligible_push(advertisingId=advert_id, thinkLoanId=loanId, companyName=companyName)
            time.sleep(3)
            detail_lists = crmManege.already_detail(loanID=loanId)
            assert detail_lists['advertisingName'] == advertisingName
        with allure.step('多融客线索列表断言对应线索'):
            crm_general().assert_customList(loanId)
            logger.debug('-' * 20 + "发起线索,电销列表保存,推送" + '-' * 20)

    @allure.story("提交订单,进入定制非电核")
    def test_case3(self, crmManege, appAddOrder):
        with allure.step('开启人工+自动截单按钮'):
            crmManege.cutStatus(types=1, status=1)
            crmManege.cutStatus(types=2, status=1)
        with allure.step('创建定制不需电核广告'):
            companyName = "dujun_gs_001"
            advertisingName = 'custom_no'
            customPlan = 1
            electricalStatus = 0
            ad_data = {"companyName": companyName, "advertisingName": advertisingName,
                       "electricalStatus": electricalStatus, "putCity": "全国",
                       "status": 1,
                       "suggestedPrice": 6, "requirement": {}, "noRequirement": {}, "customPlan": customPlan}
            crm_general().add_Advertising(ad_data=ad_data, cpcPrice=25)
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
            logger.debug('loanID----{}'.format(loanId))
        with allure.step('电销详情，保存提交订单'):
            crmManege.electrical_save(loanID=loanId)
            crmManege.submitOrder(loanID=loanId)
        with allure.step('订单进入定制非电核广告断言'):
            detail_lists = crmManege.already_detail(loanID=loanId)
            assert detail_lists['advertisingName'] == advertisingName
            crm_general().assert_customList(loanId)
            logger.debug('-' * 20 + "发起线索,电销列表保存,推送进入定制非电核" + '-' * 20)

    @allure.story("提交订单,进入非定制非电核")
    def test_case4(self, crmManege, appAddOrder):
        with allure.step('开启人工,关闭自动截单按钮'):
            crmManege.cutStatus(types=1, status=0)
        with allure.step('创建非定制不需电核广告'):
            companyName = "dujun_gs_001"
            advertisingName = 'common_no'
            customPlan = 0
            electricalStatus = 0
            ad_data = {"companyName": companyName, "advertisingName": advertisingName,
                       "electricalStatus": electricalStatus, "putCity": "全国",
                       "status": 1,
                       "suggestedPrice": 6, "requirement": {}, "noRequirement": {}, "customPlan": customPlan}
            advert_id = crm_general().add_Advertising(ad_data=ad_data, cpcPrice=25)
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
            logger.debug('loanID----{}'.format(loanId))
        with allure.step('电销详情，保存提交订单'):
            crmManege.electrical_save(loanID=loanId)
            crmManege.submitOrder(loanID=loanId)
        with allure.step('订单进入非定制非电核广告断言'):
            detail_lists = crmManege.already_detail(loanID=loanId)
            assert detail_lists['advertisingName'] == advertisingName
            crm_general().assert_customList(loanId)
            logger.debug('-' * 20 + "发起线索,电销列表保存，进入非定制非电核" + '-' * 20)
