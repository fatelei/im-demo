# -*- coding: utf8 -*-

"""
    imdemo.sockjs.app
    ~~~~~~~~~~~~~~~~~

    Sockjs Service
"""

import logging
import nsq
import tornado.web
import tornado.ioloop

from imdemo.common.mq.consumer import handle_boardcast_message
from imdemo.common.const import NSQ_INBOX_TOPIC, NSQ_LOOKUP_ADDRESS
from imdemo.im.handlers import urls

logging.basicConfig(level=logging.INFO)


def run():
    """Run standalone sockjs server.
    """
    reader = nsq.Reader(lookupd_http_addresses=[NSQ_LOOKUP_ADDRESS],
                        topic=NSQ_INBOX_TOPIC,
                        channel="chat",
                        lookupd_poll_interval=15)
    reader.set_message_handler(handle_boardcast_message)
    app = tornado.web.Application(urls)
    app.listen(9999)

    nsq.run()
    tornado.ioloop.IOLoop.instance().start()
