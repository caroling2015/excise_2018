# -*- encoding: utf-8 -*-

import unittest
import json
import xlrd
import os
import HTMLTestRunner
class Test(unittest.TestCase):
    '测试类'
    # token_1 = token_emba('12012341006', '123456') #类变量
    # def begin_req(self,apidata):
    #     u'获取部门列表'
    #     # print apidata
    #     if apidata[1] == ['']:
    #         data = eval(apidata[0])()
    #     elif apidata[1] != ['']:
    #         data = eval(apidata[0])(apidata[1])  # 输入要测试的数据,data=(mode,url,body),
    #     back = json.loads(req(data, self.token_1)['res_body'])  # 获取实际返回值,需要传入token的话,请req(data,token)
    #     YQ = 200  # 输入预期的值
    #     SJ = back['code']  # 设置实际返回,如果需要传入TOKEN等header,请务必填写!
    #     self.assertEqual(SJ, YQ, error_code(SJ, YQ))

def demo(apidata):
    def tool(self):
        Test.begin_req(self,apidata)
    setattr(tool, '__doc__', u'测试%s' % str(apidata[0]))
    return tool

def testall(apidata):
    for i in range(len(apidata)):
     setattr(Test,'test_'+str(i+1),demo(apidata[i]))



if __name__ == "__main__":
    fname = './case_2.xls'
    Apidata = []  #设置接口函数名
    SZ = xlrd.open_workbook(fname)
    print SZ.read()
    sz = SZ.sheet_by_index(0)
    for i in range(1,sz.nrows):
        par = str(sz.cell_value(i,1)).split(',')
        Apidata.append([sz.cell_value(i,0),par])

    testall(Apidata)
    suit = unittest.makeSuite(Test)
    filename = u'/'.join(os.getcwd().split('/')[:-2]) + u'/Report/业务逻辑接口测试报告-test.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner(fp, title=u'测试服新接口测试', description=u'用例执行报告', fname=filename.split('/')[-1])
    runner.run(suit)