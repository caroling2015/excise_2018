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


def trade_fee(quantity,limit):
    quantity = quantity / 1e8
    limit = limit / 1e8
    trade_fee = quantity*limit*rate
    return trade_fee

def order_sum(quantity,limit):
    quantity = quantity / 1e8
    limit = limit / 1e8
    sum = quantity*limit
    return sum

def order_fee(denominator,quantity,limit):
    fee = trade_fee(quantity, limit)
    if denominator == 'ETH':
        if fee > ETH_min_fee:
            return fee
        else:
            return ETH_min_fee
    elif denominator == 'BTC':
        if fee > BTC_min_fee:
            return fee
        else:
            return BTC_min_fee
    elif denominator == 'ETP':
        if fee > ETP_min_fee:
            return fee
        else:
            return ETP_min_fee
    else:
        print "交易对分母未定义"
