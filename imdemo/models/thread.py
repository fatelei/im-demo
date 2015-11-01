# -*- coding: utf8 -*-
"""
    imdemo.models.thread
    ~~~~~~~~~~~~~~~~~~~~

    Thread orm.
"""

import time

from pony.orm import (
    PrimaryKey,
    Required,
    Optional,
    composite_key,
    db_session
)

from .session import db


class Thread(db.Entity):

    """Thread table.
    """

    _table_ = "thread"

    id = PrimaryKey(int, unsigned=True, size=32, auto=True)
    thread_id = Required(str, index=True)
    sender_id = Required(str, index=True)
    receiver_id = Required(str, index=True)
    message_id = Required(int, unsigned=True, size=32, index=True)
    is_read = Optional(int, size=8, default=0)
    created_at = Required(int, size=32, unsigned=True)
    updated_at = Required(int, size=32, unsigned=True)

    composite_key(sender_id, receiver_id)

    @classmethod
    @db_session
    def get_threads(cls, user_id, offset=0, limit=20):
        """Get the number of unread messages.

        :param str user_id: User id
        """
        sql = """
            SELECT * FROM thread WHERE sender_id = $user_id UNION \
            SELECT * FROM thread WHERE receiver_id = $user_id \
            ORDER BY id DESC LIMIT $offset, $limit
        """
        threads = cls.select_by_sql(sql)
        return threads

    @classmethod
    @db_session
    def read_thread(cls, thread_id):
        """Set thread's is_read is 1.

        :param int thread_id: Thread id
        """
        thread = Thread[thread_id]
        thread.is_read = 1

    @classmethod
    def generate_thread_id(cls, sender_id, receiver_id):
        """Generate thread id.

        :param str sender_id: Sender id
        :param str receiver_id: Receiver id
        :return: Thread id
        """
        tmp = [sender_id, receiver_id]
        return "_".join(sorted(tmp))

    @classmethod
    @db_session
    def create_or_update_thread(cls,
                                thread_id,
                                sender_id,
                                receiver_id,
                                message_id):
        """Create a new thread or update a existsed thread.

        :param str sender_id: Sender's id
        :param str receiver_id: Receiver's id
        :param int message_id: Message id
        :return: Thread query result.
        """
        thread = Thread.get(thread_id=thread_id)
        updated_at = created_at = int(time.time())

        if not thread:
            thread = Thread(sender_id=sender_id,
                            receiver_id=receiver_id,
                            message_id=message_id,
                            created_at=created_at,
                            updated_at=updated_at,
                            thread_id=thread_id)
        else:
            thread.message_id = message_id
            thread.updated_at = updated_at
            thread.is_read = 0
        return thread
