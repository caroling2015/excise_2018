# -*- encoding: utf-8 -*-

from account import *
from orders import *
from own_operate import *
import json


def test_quaity_frozen():
    #测试委托交易后，未成交前，下单数量是否从balance中移到frozen,是则冻结成功
    asset = []

    #123
    info = json.loads(Get_balance('BTM'))
    asset.append(info['result'])
    print asset
    quantity = 12300000
    limit = 500000000
    sell_data = '{"side":"SELL","quantity":%d,"trading_pair":"BTMBTC","limit":%d,"type":"LIMIT"}'%(quantity,limit)
    Create_order(sell_data)
    info = json.loads(Get_balance('BTM'))
    asset.append(info['result'])
    print asset
    forzen_before = int(asset[-2]['frozen'])
    balance_before = int(asset[-2]['balance'])
    frozen_after = int(asset[-1]['frozen'])
    balance_after = int(asset[-1]['balance'])
    if frozen_after - forzen_before == quantity:
        if balance_before - balance_after == quantity:
            print "委托订单成功，委托数量已经冻结"
        else:
            print "冻结后余额：%d"%balance_after
            print "冻结前余额：%d"%balance_before
    else:
        print "下单前冻结数量：%d"%forzen_before
        print "下单后冻结数量：%d"%frozen_after
        print "实际下单数量：%d"%quantity

if __name__ == '__main__':
    for each in trading_pair:
        Cancel_orders_by_pair(each)


