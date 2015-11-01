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

from imdemo import models
from imdemo.common.cache.cache import rclient
from imdemo.common.const import ErrorCode, RedisKeys

from .base import BaseSockJSConnection

logger = logging.getLogger(__name__)


class ChatHandler(BaseSockJSConnection):

    """Chat with each others using sockjs.

    clients store the client information, its key format is 'group:client_id',
    """

    def on_open(self, session):
        """You can do validate client info here.

        Validate client info via token from querystring:
        >>> token = self.get_argument("token")
        >>> validate(token)
        """
        token = self.get_argument("token")
        _id = self.get_argument("id")
        if not token or not _id:
            self.send_error(ErrorCode.BAD_REQUEST,
                            "Unauthorized connection.")
            self.close()
        else:
            key = RedisKeys.USER_TOKEN_KEY.format(token=token)
            user_id = rclient.get(key)

            if _id != user_id:
                self.send_error(ErrorCode.BAD_REQUEST,
                                "Unauthorized connection.")
                self.close()
            else:
                self.current_user_id = user_id
                self.add_client(user_id)
                logger.info("user {} online".format(user_id))

    def on_message(self, payload):
        """Register message event callback function.

        :param unicode payload: Payload sent by client
        """
        payload = payload.encode("utf8")
        tmp = ujson.loads(payload)
        receiver_id = tmp.get('to', None)
        content = tmp["payload"]

        # Im need a receiver, if there is no receiver,
        # the session should be closed.
        if not receiver_id:
            self.close()

        # Insert to database first, then send to user,
        # ensure the message is not lost.
        logger.info("record message {0}:{1} to database".format(
            self.current_user_id, receiver_id))
        thread_id = models.Thread.generate_thread_id(
            self.current_user_id, receiver_id)
        message = models.Message.create_message(
            thread_id, self.current_user_id, receiver_id, content)
        models.Thread.create_or_update_thread(
            thread_id, self.current_user_id, receiver_id, message.id)

        # If the receiver is at same process with sender,
        # send the message directly to receiver.
        if self.has_client(receiver_id):
            client = self.get_client(receiver_id)
            if client:
                # Send via sockjs.
                client.send(content)
                logger.info("send message from {} to {}".format(
                    self.current_user_id, receiver_id))
        else:
            # Send message to nsq server.
            self.publish_to_nsq(ujson.dumps({
                "sender_id": self.current_user_id,
                "receiver_id": receiver_id,
                "payload": content
            }))
            logger.info("send message to nsq")

    def on_close(self):
        """Remove client info from clients.
        """
        self.remove_client(self.current_user_id)
        logger.info("user {} offline".format(self.current_user_id))


ChatRouter = SockJSRouter(ChatHandler, '/chat')
