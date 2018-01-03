# -*- encoding: utf-8 -*-
from orders import *
import json

def Cancel_orders_by_pair(pair):
    info = json.loads(List_active_orders(pair))
    if info['result']!=[]:
        for each in info['result']:
            print "---开始取消挂单：%s---" % each['id']
            Cancel_orders(pair, each['id'])
    else:
        print "交易对%s当前没有挂单" % pair