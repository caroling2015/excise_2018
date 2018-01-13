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
        print "开始委托"
        order = json.loads(Create_order(json.dumps(each)))
        print order
        if order['status']['success'] == 1:
            print '委托成功，订单号：%d价值：%f'%(order['result']['order_id'],order['result']['frozen']/1e8)
            after_coin = json.loads(Get_balance(coin))
            after_denominator = json.loads(Get_balance(denominator))
            asset.append(after_coin['result'])
            asset.append(after_denominator['result'])
            price = order_sum(each['quantity'], each['limit']) + order_fee(denominator,each['quantity'], each['limit'])
            print price
            if each['side'] == 'BUY':
                denominator_balance = (int(asset[1]['balance']) - int(asset[3]['balance']))/1e8
                denominator_frozen = (int(asset[3]['frozen'])- int(asset[1]['frozen']))/1e8

                print denominator_balance,denominator_frozen
                if (price == denominator_balance) and (price ==denominator_frozen):
                    print "委买订单成功，委托数量已经冻结"
                else:
                    print "委买订单冻结账户失败"

            elif each['side'] == 'SELL':
                coin_balance = (int(asset[1]['balance']) - int(asset[3]['balance'])) / 1e8
                coin_frozen = (int(asset[3]['frozen']) - int(asset[1]['frozen'])) / 1e8

                print coin_balance,coin_frozen
                if (price == coin_balance) and (price == coin_frozen):
                    print "委卖订单成功，委托数量已经冻结"
                else:
                    print "委卖订单冻结账户失败"
        else:
            print "委托失败"



if __name__ == '__main__':
    Cancel_orders_by_pair('BTMBTC')
    for each in data:
        order_frozen(coin,data)


