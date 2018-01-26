# -*- encoding: utf-8 -*-

import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'D:\excise_2018\test\learn\charpter 1\case.xlsx')
    # 获取所有sheet
    content = workbook.sheet_names()  # [u'sheet1', u'sheet2']
    sheet1_name = content[0]
    sheet2_name = content[1]
    print sheet1_name,sheet2_name

    # # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    print sheet1.cell(1, 0).ctype
    for i in range(sheet1.nrows):
        type = sheet1.cell(i,2).ctype
        if type == 1:
            type_name = 'string'
        if type == 2:
            type_name = 'number'
        if type == 3:
            date_value = xlrd.xldate_as_tuple(sheet1.cell_value(2, 3), book.datemode)
            date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    print '第%d个是：%s'%(i,type_name)

if __name__ == '__main__':
    read_excel()