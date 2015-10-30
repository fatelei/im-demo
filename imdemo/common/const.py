# -*- coding: utf8 -*-
"""
    imdemo.common.const
    ~~~~~~~~~~~~~~~~~~~

    Const.
"""

__all__ = [
    "NSQ_INBOX_TOPIC"
]

NSQ_INBOX_TOPIC = "inbox"  # Inbox topic name.

NSQ_LOOKUP_ADDRESS = "http://127.0.01:4161"
NSQD_ADDREESS = "127.0.0.1:4150"


class ErrorCode(object):

    """Error Code.
    """

    BAD_REQUEST = 1


class RedisKeys(object):

    USER_TOKEN_KEY = 'token:{token}->user_id'
