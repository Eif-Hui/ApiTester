# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 4:04 下午
# @Author  : Hui
# @File    : fail_run.py

def fail_run(n=3):
    def decorator(func):
        def wrapper(*args,**kw):
            for i in range(n):
                try:
                    r= func(*args,**kw)
                    return r
                except NameError as err:
                    print('用例第一次失败原因:%s'%err)
            raise NameError
        return wrapper
    return decorator