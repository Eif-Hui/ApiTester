# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 上午10:38
# @Author  : Hui
# @File    : run_case.py

from apps import app
from apps.core.views import coreApi
from apps.users.views import userApi
from apps.auth.views import authApi


#将蓝图注册到app中
app.register_blueprint(coreApi,url_prefix= '/methods_class')
app.register_blueprint(userApi)
app.register_blueprint(authApi)


if __name__ == '__main__':
	app.run(port=7080,debug=True)