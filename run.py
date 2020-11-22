# -*- coding: utf-8 -*-
# @Time    : 2020/11/21 10:06 下午
# @Author  : Hui
# @File    : run.py

import os
import time
from confs.conf import *
import unittest
from BeautifulReport import BeautifulReport

if __name__ == "__main__":
    # 定义测试报告的生成的时间，时间戳
    nowTime = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    # test_dir"目录，"test*.py"匹配当前目录下所有test*.py结尾的用例
    suite_tests = \
        unittest.defaultTestLoader.discover(TESTCASE_PATH, pattern="test*.py",
                                            top_level_dir=None)
    BeautifulReport(suite_tests).report(filename='ApiReport' + '_' + nowTime,
                                        description='测试LOGIN',
                                        log_path=REPORT_PATH)

