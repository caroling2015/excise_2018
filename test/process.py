import common
from account import *
from orders import *
from conf import *
import json

if __name__ == '__main__':
    asset = []
    info = json.loads(Get_balance('BTM'))
    asset.append(info[u'result'])
    sell_data = {"side":"SELL","quantity":12300000,"trading_pair":"BTMBTC","limit":500000000,"type":"LIMIT"}
    sell_info = json.loads(Create_order(sell_data))
    info = json.loads(Get_balance('BTM'))
    asset.append(info[u'result'])
    print asset[-1]-asset[-2]