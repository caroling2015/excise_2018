from common import *

def Create_order(data):
    url = 'http://'+ host + '/api/trader/order'
    return post(url,data)

def Cancel_orders(trading_pair,order_id):
    url = 'http://' + host + '/api/trader/order/%s/%s'%(trading_pair,order_id)
    return delete(url)


def List_active_orders(trading_pair):
    url = 'http://' + host + '/api/trader/orders/%s'%trading_pair
    return get(url)

def List_history_orders(trading_pair,order_id):
    url = 'http://' + host + '/api/trader/history/%s/%s'%(trading_pair,order_id)
    return get(url)

def List_history_trades(trading_pair,page=None):
    if page !=None:
        url = 'http://' + host + '/api/trader/historys/%s/%d'%(trading_pair,page)
    else:
        url = 'http://' + host + '/api/trader/historys/%s/0'%(trading_pair)
    return get(url)

def List_trading_pairs():
    url = 'http://' + host + '/api/trader/trading_pairs'
    return get(url)











