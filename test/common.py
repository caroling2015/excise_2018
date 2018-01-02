# -*- encoding: utf-8 -*-
import urllib2
from conf import *

req_headers = {
    'signature': '%s' % signature,
    'apikey': '%s' % apikey,
    'Content-Type': 'application/json',
    'host': '%s' % host
}

# data = {"side":side,"quantity":quantity,"trading_pair":pair,"limit":limit,"type":"LIMIT"}

def get(url):
    req = urllib2.Request(url,headers = req_headers)
    info = urllib2.urlopen(req)
    return info.read()

def post(url,data):
    req = urllib2.Request(url,data,headers=req_headers)
    info = urllib2.urlopen(req)
    return info.read()

def delete(url):
    req = urllib2.Request(url,headers=req_headers)
    req.get_method = lambda : 'DELETE'
    info = urllib2.urlopen(req)
    return info.read()
