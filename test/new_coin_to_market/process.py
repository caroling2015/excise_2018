# -*- encoding: utf-8 -*-

from account import *
from orders import *
from own_operate import *
import json

def order_frozen(coin,data):
    #测试委托交易后，未成交前，下单数量是否从balance中移到frozen,是则冻结成功
    asset = []
    before_coin = json.loads(Get_balance(coin))
    asset.append(before_coin['result'])
    for each in data:
        denominator = str(each['trading_pair'][-3:])
        before_denominator = json.loads(Get_balance(denominator))
        asset.append(before_denominator['result'])
        order = json.loads(Create_order(json.dumps(each)))
        if order['status']['success'] == 1:
            print "开始委托"
            after_coin = json.loads(Get_balance(coin))
            after_denominator = json.loads(Get_balance(denominator))
            asset.append(after_coin['result'])
            asset.append(after_denominator['result'])
            print asset
            print each
            fee = float(order_fee(denominator,each['quantity'],each['limit']))
            print fee



            print (int(asset[-3]['balance']) - int(asset[-1]['balance']))
            print (int(asset[-1]['frozen'])- int(asset[-3]['frozen']))
            if each['quantity'] == int(asset[-3]['balance']) - int(asset[-1]['balance']) and \
                            each['quantity'] ==  int(asset[-1]['frozen'])- int(asset[-3]['frozen']):
                    print "委托订单成功，委托数量已经冻结"
            else:
                print "委买订单冻结账户失败"
        else:
            print "委托失败"



if __name__ == '__main__':
    Cancel_orders_by_pair('BTMBTC')
    for each in data:
        order_frozen(coin,data)


