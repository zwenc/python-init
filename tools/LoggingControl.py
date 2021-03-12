# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:39:49
@FilePath: \python-init\tools\LoggingControl.py
'''

import sys
sys.path.append(".")

import logging 
from tools.SystemInfo import SystemInfo
from tools.Decorator import Singleton
import os
import traceback
import multiprocessing as mp

@Singleton   # 单例模式
class Logger:
    def __init__(self, filename = SystemInfo.start_time + ".txt"):
        if os.path.exists("log/") is False:
            os.mkdir("log/")

        filename = "log/" + str(filename)

        self.logger=logging.getLogger(SystemInfo.system_name)
        self.logger.setLevel(logging.DEBUG)
        handler=logging.FileHandler(filename)
        handler.setLevel(logging.DEBUG)

        formatter=logging.Formatter('%(asctime)s - %(name)s - [%(filename)s file line:%(lineno)d] - %(levelname)s - %(message)s')
        console=logging.StreamHandler()
        console.setLevel(logging.DEBUG)

        handler.setFormatter(formatter)
        console.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.addHandler(console)
        
        self.delete_old_file()
        self.lock = mp.Lock()
    
    def info(self, *args):
        out = str()
        for info in args:
            out += str(info)

        try:
            self.lock.acquire()
            self.logger.info("\n" + out)
        finally:
            self.lock.release()
    
    def warning(self, *args):
        out = str()
        for info in args:
            out += str(info)

        try:
            self.lock.acquire()
            self.logger.warning("\n" + out)
        finally:
            self.lock.release()

    def error(self, *args):
        out = str()
        for info in args:
            out += str(info)
            
        try:
            self.lock.acquire()
            self.logger.error("\n" + out)
        finally:
            self.lock.release()

    def get_log(self):
        return self.logger

    def delete_old_file(self):
        import os 
        dir_list = os.listdir("log")
        if not dir_list:
            return
        else:
            dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join("log", x)))
            # print(dir_list)

        if len(dir_list) >= 10:
            os.remove("log/" + dir_list[0])
            self.logger.warning("\nlogging size is too big, remove " + dir_list[0] + " log file")

logger = Logger()

def except_hook(cls, exception, traceback_):
    outinfo = ""
    for i in traceback.format_exception(cls, exception, traceback_):
        outinfo += i
        
    logger.error(outinfo)
    sys.exit(1)
    
sys.excepthook = except_hook

if __name__ == "__main__":
    # a = Logger().get_log()
    logger.info("asdf", 1, "asfd", "   ", "qqweq")
    logger.warning("asdf", 1)
    logger.error("asdf", 1)