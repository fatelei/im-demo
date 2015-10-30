# -*- coding: utf8 -*-
"""
    scripts.inbox
    ~~~~~~~~~~~~~

    Send message to inbox for persistent store.
"""

import nsq
import ujson

from imdemo.common.const import NSQ_INBOX_TOPIC, NSQ_LOOKUP_ADDRESS


def inbox(message):
    """
    :param nsq.message.Message message
    :return: A boolean value.
    """
    tmp = ujson.loads(message.body)
    group_id = tmp.get("group_id", -1)
    user_id = tmp.get("user_id")

    # Insert to database.


if __name__ == "__main__":
    reader = nsq.Reader(lookupd_http_addresses=[NSQ_LOOKUP_ADDRESS],
                        topic=NSQ_INBOX_TOPIC,
                        channel="chat",
                        lookupd_poll_interval=15)
    reader.set_message_handler(inbox)
    nsq.run()
