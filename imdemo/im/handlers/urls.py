# -*- coding: utf8 -*-
"""
    imdemo.socks.handlers.urls
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Handlers' urls
"""

__all__ = ["urls"]

from .benchmark import BenchmarkRouter
from .chat import ChatRouter


urls = [] + ChatRouter.urls
urls += BenchmarkRouter.urls
