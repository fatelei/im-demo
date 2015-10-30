# -*- coding: utf8 -*-
"""
    imdemo.sockjs.handlers.chat
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Chat Handler.
"""

__all__ = ["ChatRouter"]

import logging
import ujson

from sockjs.tornado import SockJSRouter

from imdemo.common.const import CLIENT_IDENTIFY

from .base import BaseSockJSConnection

logger = logging.getLogger(__name__)


class ChatHandler(BaseSockJSConnection):

    """Chat with each others using sockjs.

    clients store the client information, its key format is 'group:client_id',
    """

    def on_open(self, session):
        """You can do validate client info here.

        Validate client info via session:
        >>> cookie = session.get_cookie('cookie key')
        >>> is_validate_user(cookie)
        """
        # Validate firstly.
        self.add_client("a")
        logger.info("client online")

    def on_message(self, payload):
        """Register message event callback function.

        :param unicode payload: Payload sent by client
        """
        payload = payload.encode("utf8")
        tmp = ujson.loads(payload)
        receiver_id = tmp.get('to', None)

        # Im need a receiver, if there is no receiver,
        # the session should be closed.
        if not receiver_id:
            self.close()

        # Get group id, we can use it to boardcast.
        group_id = tmp.get("group_id", -1)
        key = CLIENT_IDENTIFY.format(group_id=group_id, user_id=receiver_id)
        if self.has_client(key):
            client = self.get_clients(key)
            if client:
                client.send(tmp["payload"])
                logger.info("send message to client")
        else:
            # Send message to nsq server.
            self.publish_to_nsq(payload)
            logger.info("send message to nsq")

    def on_close(self):
        """Remove client info from clients.
        """
        self.remove_client("a")
        logger.info("client offline")


ChatRouter = SockJSRouter(ChatHandler, '/chat')
