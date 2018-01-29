# -*- encoding: utf-8 -*-

import xlrd
import xlwt
from datetime import date,datetime

def read_excel():
    # 打开文件
    data = xlrd.open_workbook(r'case.xlsx')
    table = data.sheets()[0]
    # table = data.sheet_by_index(0)
    # table = data.sheet_by_name(u'Sheet1')
    nrows = table.nrows
    ncols = table.ncols
    print range(nrows)
    # for i in range(nrows):
    #     # print table.row_values(i)
    # print '----------------------------'
    # for i in range(ncols):
    #     print table.col_values(i)

if __name__ == '__main__':
    read_excel()