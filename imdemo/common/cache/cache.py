# -*- coding: utf8 -*-
"""
    imdemo.common.cache.cache
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Redis cache client.
"""

import redis

pool = redis.ConnectionPool(host="localhost",
                            port=6379,
                            db=0)
rclient = redis.Redis(connection_pool=pool)
