# -*- coding: utf8 -*-
"""
    imdemo.models.message
    ~~~~~~~~~~~~~~~~~~~~~

    Message orm.
"""

import time

from pony.orm import PrimaryKey, Required, db_session

from .session import db


class Message(db.Entity):

    """Message table.
    """
    _table_ = "message"

    id = PrimaryKey(int, unsigned=True, auto=True, size=32)
    thread_id = Required(str, index=True)
    sender_id = Required(str, index=True)
    receiver_id = Required(str, index=True)
    content = Required(str, 400)
    created_at = Required(int, unsigned=True, size=32)

    @classmethod
    @db_session
    def get_messages(cls, thread_id, offset=0, limit=20):
        """Get messages.

        :param str thread_id: Thread id
        :param int offset: Page number
        :param int limit: Page size
        :return: A list of messages.
        """
        sql = """
            SELECT * FROM message WHERE thread_id = $thread_id \
            ORDER BY id DESC LIMIT $offset, $limit
        """
        messages = cls.select_by_sql(sql)
        return messages

    @classmethod
    @db_session
    def create_message(cls, thread_id, sender_id, receiver_id, content):
        """Create a new message.

        :param str sender_id: Sender id
        :param str receiver_id: Receiver id
        :param str content: Content
        :return: Message
        """
        created_at = int(time.time())
        message = Message(thread_id=thread_id,
                          sender_id=sender_id,
                          receiver_id=receiver_id,
                          content=content,
                          created_at=created_at)
        return message

    @classmethod
    @db_session
    def delete_message(cls, message_id):
        """Delete a message.

        :param int message_id: Message id
        """
        Message[message_id].delete()

    @classmethod
    @db_session
    def get_message(cls, message_id):
        """Get a message.

        :param int message_id: Message id
        :return: A message.
        """
        return Message.get(id=message_id)
