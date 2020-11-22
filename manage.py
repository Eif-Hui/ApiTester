# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 9:04 AM
# @Author  : Hui
# @File    : manage.py

'''
    pytest用例执行文件
'''


import time
from confs.conf import *

if __name__ == '__main__':
    '''
        执行器：pytest
    '''
    import pytest

    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    #pytest.main(['-s', TESTCASE_PATH, '--html=report/{}_report.html'.format(nowTime)])



    xml_report_path = REPORT_PATH + "/xml"
    html_report_path = REPORT_PATH + "/html"
    pytest.main(['--reruns 2'])
    args = ['-s', '-q', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate {xml} -o {html}'.format(xml=xml_report_path,html=html_report_path)
    p = os.popen(cmd).read().strip()  # 运行终端命令


    '''
        执行器：unittest
    '''
    # import unittest
    # from BeautifulReport import BeautifulReport
    # #test_dir"目录，"test*.py"匹配当前目录下所有test*.py结尾的用例
    # suite_tests = \
    #     unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern="test*.py",
    #                                         top_level_dir=None)
    # BeautifulReport(suite_tests).report(filename='ApiReport' + '_' + nowTime,
    #                                     description='ApiTesting',
    #                                     log_path=REPORT_PATH)