# -*- coding: utf8 -*-
"""
    imdemo.common.mq.consumer
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Nsq consumer.
"""

import logging
import ujson

from imdemo.im.store.clients import clients

logger = logging.getLogger(__name__)


def handle_boardcast_message(message):
    """Handle boardcast message delivered nsq from frontend sockjs server.

    :param nsq.message.Message message
    :return: A boolean value.
    """
    try:
        logger.info("process message in nsq consumer")
        tmp = ujson.loads(message.body)
        # group_id = tmp.get("group_id", -1)
        sender_id = tmp["sender_id"]
        receiver_id = tmp["receiver_id"]
        content = tmp["payload"]

        # Send via sockjs.
        if clients.has_client(receiver_id):
            client = clients.get_client(receiver_id)
            if client:
                client.send(content)
                logger.info("send via sockjs by nsq consumer {0}:{1}".format(
                    sender_id, receiver_id))

        return True
    except Exception as e:
        logger.error(e, exc_info=True)
        logger.error(message.body)
        return False
