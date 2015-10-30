# -*- coding: utf8 -*-
"""
    imdemo.socks.handlers.urls
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Handlers' urls
"""

from .chat import ChatRouter


urls = [] + ChatRouter.urls
