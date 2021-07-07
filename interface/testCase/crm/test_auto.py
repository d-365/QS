# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 11:55
# @Author  : dujun
# @File    : test_auto.py
# @describe: CRM系统各菜单接口自动化判断

import random
import time
import allure
from interface.data.order_data import order_data


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
            # 公司充值记录断言
            rechargeList = crmManege.rechargeList(companyName=companyName)
            for i in range(len(rechargeList)):
                if price == rechargeList[i]['threadMoney']:
                    break
                else:
                    raise Exception("对应公司财务管理,充值记录下未找到对应充值记录")

    @allure.story('账户退款')
    def test_refund(self, crmManege, crmAdmin):

        # 退款公司
        companyName = 'dujun_gs_001'
        price = 5

        with allure.step('禁用该公司下所有广告'):
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

            re3 = crmManege.refund(companyName, money_before)

            detail_after = crmAdmin.detail()
            money_after = detail_after['data']['money']
            # 公司余额断言
            assert money_after == (money_before - money_before)
            # 公司退款记录断言
            rechargeList = crmManege.consumeList(companyName=companyName)
            for i in range(len(rechargeList)):
                if money_before == rechargeList[i]['threadMoney']:
                    break
                else:
                    raise Exception("对应公司财务管理,退款记录下未找到对应退款记录")

    @allure.story('消耗记录')
    def test_consumeList(self, crmManege, crmAdmin,appAddOrder):

        with allure.step('开启人工截单按钮,'):
            crmManege.cutStatus1(status=1)
        with allure.step('新增广告[定制需电核]'):
            companyName = 'dujun_gs_001'
            cpcPrice = 25
            adName = 'custom_yes'
            electricalStatus = '1'
            # 广告数据
            addAdvertising_data = {}
            crmManege.addAdvertising(payload=addAdvertising_data)
            # 查询广告ID
            advert_list = crmManege.advertisingList(companyName=companyName,advertisingName=adName,electricalStatus=electricalStatus)
            advert_id = advert_list[0]['id']
            # 修改订单CPC出价
            crmAdmin.editAd(ID=advert_id, budgetConfig=99999, cpcPrice=cpcPrice)
        with allure.step('信业帮发起线索请求'):
            payload = order_data(city_name='安顺市')
            appAddOrder.app_addOrder(payload)
            loanId = appAddOrder.get_loanId()
        with allure.step("对应线索推送给符合条件广告"):
            print('线索ID：', loanId, '广告ID：', advert_id)
            time.sleep(2)
            crmManege.push(advertisingId=advert_id, thinkLoanId=loanId, companyName=companyName)
        with allure.step('消耗列表断言'):
            consumeList = crmManege.consumeList(companyName=companyName,adName=adName)
            for i in range(len(consumeList)):
                if cpcPrice == consumeList[i]['threadMoney'] and loanId == consumeList[i]['loanId'] and adName == consumeList[i]['adName']:
                    break
                else:
                    raise Exception("对应公司财务管理,消耗记录下未找到对应消耗记录")





