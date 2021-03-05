# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:39:49
@FilePath: \python-init\tools\ParseConfig.py
'''

import sys
sys.path.append(".")

import configparser
from tools.SystemInfo import SystemInfo
from tools.LoggingControl import Logger
import pickle
# from tools.Decorator import Singleton
# import MerbleInfo.DataInfo

loger = Logger().get_log()

def _print_ini_info(con):
    sections = con.sections()

    for i in sections:
        for key in con[i]:
            loger.info ("{sec} : {key} = {value}".format(sec = i, key = key, value=con[i][key]))

def parse_ini_file(filePath):
    con = configparser.ConfigParser()
    con.read(filePath, encoding='utf-8')

    _print_ini_info(con)

    return con

def save_class(cls_object):
    output_hal = open("backups/"+SystemInfo.start_time + ".pkl", 'wb')
    str = pickle.dumps(cls_object)
    output_hal.write(str)
    output_hal.close()
    
    output_hal = open("backups/latest.pkl", 'wb')
    str = pickle.dumps(cls_object)
    output_hal.write(str)
    output_hal.close()
    
def load_class(filename, cls_object):
    with open(filename,'rb') as file:
        cls_object  = pickle.loads(file.read())

if __name__ == "__main__" :

    a = parse_ini_file("Config/config.ini")
    print(a["image"]["is_center"])




