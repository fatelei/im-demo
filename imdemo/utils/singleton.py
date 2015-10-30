# -*- coding: utf8 -*-
"""
    imdemo.utils.singleton
    ~~~~~~~~~~~~~~~~~~~~~~

    Singleton mode.
"""


def singleton_class(obj):
    instances = {}

    def wrapper(*args, **kwargs):
        name = obj.__name__
        if name not in instances:
            instance = obj(*args, **kwargs)
            instances[name] = instance
        return instances[name]
    return wrapper
