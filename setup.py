# -*- coding: utf8 -*-

from setuptools import setup

from imdemo import __version__

setup(
    name="imdemo",
    version=__version__,
    author="fatelei@gmail.com",
    description="Using sockjs & nsq & flask & mysql, implement a im demo.",
    packages=["imdemo"],
    install_requires=[
        "flask",
        "pony",
        "pymysql",
        "pynsq",
        "redis",
        "sockjs-tornado",
        "tornado",
        "ujson"
    ],
    entry_points={
        "console_scripts": [
            "im=imdemo.im.app:run",
            "im_apis=imdemo.apis.app:app"
        ]
    }
)
