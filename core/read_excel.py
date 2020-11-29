# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 8:53 AM
# @Author  : Hui
# @File    : read_excel.py

import xlrd
import jsonpath,json
from confs.conf import *


def read_excel(excel_path=BASE_PATH + "/confs/case.xlsx", sheet_name="Sheet1"):
    '''
    读取excel文件内容
    :param excel_path: xlsx文件的路径
    :param sheet_name: 表格名称
    :return: k-v的列表
    '''
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)
    # 获取所有sheet
    # print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_name(sheet_name)  # sheet索引从0开始

    # 获取第一行作为key
    first_row = sheet.row_values(0)  # 获取第一行内容

    # 获取表的行数
    rows_length = sheet.nrows
    # 定义两个空列表，存放每行的数据
    all_rows = []
    rows_dict = []
    for i in range(rows_length):  # 循环逐行打印
        print("--------",i)
        if i == 0:  # 跳过第一行
            continue
        all_rows.append(sheet.row_values(i))
    for row in all_rows:
        lis = dict(zip(first_row, row))
        rows_dict.append(lis)
    return rows_dict

def get_all_case_name(excel_path=BASE_PATH + "/confs/case.xlsx",sheet_name="Sheet1"):
    """
    获取整个Excel 文件全部的用例名称
    :param excel_path:
    :return:
    """
    # 打开文件
    workbook = xlrd.open_workbook(excel_path)
    # 获取所有sheet
    # print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_name(sheet_name)  # sheet索引从0开始

    # 获取第一行作为key
    first_row = sheet.row_values(0)  # 获取第一行内容

    # 获取表的行数
    rows_length = sheet.nrows
    # 定义两个空列表，存放每行的数据
    all_rows = []
    rows_dict = []
    for i in range(rows_length):  # 循环逐行打印
        if i == 0:  # 跳过第一行
            continue
        all_rows.append(sheet.row_values(i))
    for row in all_rows:
        lis = dict(zip(first_row, row))
        #run_case_list = jsonpath.jsonpath(lis,"$.[?(@.is_run = 'yes')]")
        if RUN_CASE.upper() == "ALL":
            rows_dict.append(lis)
        if RUN_CASE.upper() == "YES":
            if lis.get("is_run").upper() == "NO":
                continue
            rows_dict.append(lis)
    return rows_dict


def excel_to_list(data_file, sheet):
    """

    :param data_file: excel 用例文件
    :param sheet:  sheet名字
    :return:
    """
    data_list = []  # 新建个空列表，来乘装所有的数据
    wb = xlrd.open_workbook(data_file)  # 打开excel
    sh = wb.sheet_by_name(sheet)  # 获取工作簿
    header = sh.row_values(0)  # 获取标题行数据
    for i in range(1, sh.nrows):  # 跳过标题行，从第二行开始取数据
        d = dict(zip(header, sh.row_values(i)))  # 将标题和每行数据组装成字典
        data_list.append(d)
    return data_list  # 列表嵌套字典格式，每个元素是一个字典

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['descrption']:  # 如果字典数据中case_name与参数一致
            return case_data
            # 如果查询不到会返回None


if __name__ == '__main__':
    #read_excel()
    #print(get_all_case_name())



    data_list = excel_to_list(data_file=BASE_PATH + "/confs/case.xlsx",sheet="Sheet1")  # 读取excel，TestUserLogin工作簿的所有数据
    case_data = get_test_data(data_list, '学校查询')  # 查找用例'test_user_login_normal'的数据
    print(data_list)
