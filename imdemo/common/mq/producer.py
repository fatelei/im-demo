# -*- coding: utf8 -*-
"""
    imdemo.common.mq.producer
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Message Producer.
"""

import nsq

from imdemo.common.const import NSQD_ADDREESS

# TODO Should be lasy.
nsq_producer = nsq.Writer([NSQD_ADDREESS])
