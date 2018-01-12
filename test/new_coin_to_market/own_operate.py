# -*- encoding: utf-8 -*-
from orders import *
import json

def Cancel_orders_by_pair(pair):
    info = json.loads(List_active_orders(pair))
    if info['result']!=[]:
        for each in info['result']:
            print "---开始取消当前挂单：%s---" % each['id']
            Cancel_orders(pair, each['id'])
    else:
        print "交易对%s当前没有挂单" % pair

def ETH_order_fee(quantity,limit):
    min_rate = ETH_min_fee
    order_fee = quantity*limit*rate
    if order_fee > min_rate:
        return order_fee
    else:
        return min_rate

def BTC_order_fee(quantity,limit):
    min_rate = BTC_min_fee
    order_fee = quantity*limit*rate
    if order_fee > min_rate:
        return order_fee
    else:
        return min_rate

def ETP_order_fee(quantity,limit):
    min_rate = ETP_min_fee
    order_fee = quantity*limit*rate
    if order_fee > min_rate:
        return order_fee
    else:
        return min_rate

def order_fee(denominator,quantity,limit):
    quantity = quantity/1e8
    limit = limit/1e8
    if denominator == 'ETH':
        ETH_min_fee(quantity,limit)
    elif denominator == 'BTC':
        BTC_min_fee(quantity,limit)
    elif denominator == 'ETP':
        ETP_min_fee(quantity,limit)
    else:
        print "交易对分母未定义"
