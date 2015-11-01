# -*- coding: utf8 -*-

"""
    imdemo.sockjs.app
    ~~~~~~~~~~~~~~~~~

    Sockjs Service
"""

import logging
import os
import nsq
import tornado.web
import tornado.ioloop

from imdemo.common.mq.consumer import handle_boardcast_message
from imdemo.common.const import NsqTopic, NsqConfig
from imdemo.im.handlers import urls
from imdemo.models import db

logging.basicConfig(level=logging.INFO)


def run():
    """Run standalone sockjs server.
    """
    # Bind to mysql, and generate mapping.
    db.bind("mysql",
            host="localhost",
            port=3306,
            user="root",
            passwd="123456",
            db="threads")
    db.generate_mapping(check_tables=True,
                        create_tables=False)

    reader = nsq.Reader(lookupd_http_addresses=[NsqConfig.NSQ_LOOKUP_ADDRESS],
                        topic=NsqTopic.NSQ_INBOX_TOPIC,
                        channel="chat",
                        lookupd_poll_interval=15)
    reader.set_message_handler(handle_boardcast_message)
    app = tornado.web.Application(urls)
    port = os.environ.get("PORT", 9999)
    port = int(port)
    app.listen(port)

    nsq.run()
    tornado.ioloop.IOLoop.instance().start()
