# -*- coding: utf8 -*-
"""
    imdemo.models.session
    ~~~~~~~~~~~~~~~~~~~~~

    Pony database session.
"""

__all__ = ["db"]

from pony.orm import Database

db = Database()
