# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:57:59
@FilePath: \python-init\main.py
'''
from tools.ArgsGet import ArgsGet         # 参数获取
from tools.LoggingControl import logger   # 日志系统，日志会自动输入到log/文件夹中
from tools.SystemInfo import SystemInfo   # 系统启动信息（name, start time）

a = ArgsGet().get()
logger.info(SystemInfo.start_time)
logger.info(a)
