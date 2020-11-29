# -*- coding: utf-8 -*-
# @Time    : 2020/10/24 9:04 AM
# @Author  : Hui
# @File    : run_case.py

'''
    执行器
'''
import time
import pytest
from config.config import *
import unittest
from methods_class.HTMLTestReportCN import HTMLTestRunner
from BeautifulReport import BeautifulReport


class Actuator(object):

    def __init__(self):

        self.nowTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    def py_run_html_report(self):
        """
        通过pytest 执行用例
        :return:
        """

        pytest.main(['-s', TESTCASE_PATH, '--html=report/{}_report.html'.format(self.nowTime)])

    def py_run_allure(self):
        xml_report_path = REPORT_PATH + "/xml"
        html_report_path = REPORT_PATH + "/html"
        pytest.main(['--reruns 2'])
        args = ['-s', '-q', '--alluredir', xml_report_path]
        pytest.main(args)
        cmd = 'allure generate {xml} -o {html}'.format(xml=xml_report_path, html=html_report_path)
        p = os.popen(cmd).read().strip()  # 运行终端命令

    def un_run_Report(self):
        """
        通过unittest 执行用
        :return:
        """
        # #test_dir"目录，"test*.py"匹配当前目录下所有test*.py结尾的用例
        suite_tests = \
            unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern="test*.py",
                                                top_level_dir=None)
        # BeautifulReport(suite_tests).report(filename='ApiReport' + '_' + nowTime,
        #                                     description='ApiTesting',
        #                                     log_path=REPORT_PATH)

        f = open(REPORT_PATH+"report_{}.html".format(self.nowTime), 'wb')  # 二进制写格式打开要生成的报告文件
        HTMLTestRunner(stream=f,title="Api Test",description="测试",tester ='hui').run(suite_tests)
        f.close()


if __name__ == '__main__':
    Actuator().py_run_allure()




    # xml_report_path = REPORT_PATH + "/xml"
    # html_report_path = REPORT_PATH + "/html"
    # pytest.main(['--reruns 2'])
    # args = ['-s', '-q', '--alluredir', xml_report_path]
    # pytest.main(args)
    # cmd = 'allure generate {xml} -o {html}'.format(xml=xml_report_path,html=html_report_path)
    # p = os.popen(cmd).read().strip()  # 运行终端命令