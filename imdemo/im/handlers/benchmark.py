# -*- coding: utf8 -*-
"""
    imdemo.im.handlers.benchmark
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using for benchmark sockjs-tornado.
"""

__all__ = ["BenchmarkRouter"]

from sockjs.tornado import SockJSRouter

from .base import BaseSockJSConnection


class BenchmarkHandler(BaseSockJSConnection):

    def on_open(self, session):
        self.key = id(session)
        self.add_client(self.key)

    def on_message(self, message):
        self.send(message)

    def on_close(self):
        self.remove_client(self.key)


BenchmarkRouter = SockJSRouter(BenchmarkHandler, "/benchmark")
