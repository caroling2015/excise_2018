# -*- encoding: utf-8 -*-
from common import *

def Get_balance(coin):
    url = 'http://' + host + '/api/trader/balance/%s'%coin
    return get(url)

def List_balances():
    url = 'http://' + host + '/api/trader/balances'
    return get(url)

def List_deposit(asset,page=None):
    if(page!=None):
        url = 'http://' + host + '/api/trader/deposits/%s/%d'%(asset,page)
    else:
        url = 'http://' + host + '/api/trader/deposits/%s/0'%(asset)
    return get(url)

def List_withdrawal(asset,page=None):
    if(page!=None):
        url = 'http://' + host + '/api/trader/withdrawals/%s/%d'%(asset,page)
    else:
        url = 'http://' + host + '/api/trader/withdrawals/%s/0'%(asset)
    return get(url)