# -*- coding: utf8 -*-
"""
    imdemo.common.mq.consumer
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Nsq consumer.
"""

import ujson

from imdemo.common.const import CLIENT_IDENTIFY
from imdemo.im.store.clients import clients


def handle_boardcast_message(message):
    """Handle boardcast message delivered nsq from frontend sockjs server.

    :param nsq.message.Message message
    :return: A boolean value.
    """
    tmp = ujson.loads(message.body)
    group_id = tmp.get("group_id", -1)
    user_id = tmp.get("user_id")
    key = CLIENT_IDENTIFY.format(group_id=group_id, user_id=user_id)

    if clients.has_client(key):
        client = clients.get_client(key)
        if client:
            client.send(tmp["payload"])

    return True
