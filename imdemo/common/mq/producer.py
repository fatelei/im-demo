# -*- coding: utf8 -*-
"""
    imdemo.common.mq.producer
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Message Producer.
"""

import nsq

from imdemo.common.const import NsqConfig

# TODO Should be lasy.
nsq_producer = nsq.Writer([NsqConfig.NSQD_ADDREESS])
