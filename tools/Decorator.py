# -*- coding: utf-8 -*-
'''
@copyright: zwenc
@email: zwence@163.com
@Date: 2021-03-05 11:39:49
@FilePath: \python-init\tools\Decorator.py
'''


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

