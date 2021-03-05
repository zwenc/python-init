# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:43:52
@FilePath: \python-init\tools\ArgsGet.py
'''
import sys
sys.path.append(".")

import argparse
from tools.Decorator import Singleton
from tools.SystemInfo import SystemInfo

@Singleton
class ArgsGet():

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=SystemInfo.system_name)
        self.parser.add_argument('--param1', type=str, default="张", help='姓')
        self.parser.add_argument('--param2', type=str, default="三", help='名')
        
    def get(self):
        return self.parser.parse_args()


if __name__ == "__main__":
    a = ArgsGet().get()

    print(a.param1)
    print(a.param2)
    print("asdf")

