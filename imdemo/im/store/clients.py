# -*- coding: utf8 -*-
"""
    imdemo.sockjs.store.clients
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Store the client info that connects to sockjs server.
"""

__all__ = ["clients"]

from imdemo.utils import singleton_class


@singleton_class
class Clients(object):

    def __init__(self):
        self.clients = {}

    def add_client(self, key, client):
        """Add client.

        :param str key
        :param object client: SockJS Session object
        """
        self.clients[key] = client

    def has_client(self, key):
        return key in self.clients

    def get_client(self, key):
        """Get client by key.

        :param str key
        :return: SockJS Session object or None.
        """
        return self.clients.get(key, None)

    def remove_client(self, key):
        """Remove client.

        :param str key
        """
        self.clients.pop(key)


clients = Clients()
