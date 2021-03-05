# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:39:49
@FilePath: \python-init\tools\SystemInfo.py
'''

import time

class SystemInfo:
    system_name = "system"
    start_time = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))


if __name__ == "__main__" :
    print(SystemInfo.start_time )