# -*- coding: utf8 -*-
"""
    imdemo.apis.handlers.chat
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Chat http apis.
"""

__all__ = ["thread_app"]

from flask import Blueprint, request, jsonify

from imdemo import models

thread_app = Blueprint("thread",
                       __name__)


@thread_app.route("/inbox", methods=["GET"])
def show_threads_list():
    """Show all threads.

    :response:

    {
        "paging": {
            "prev": //,
            "next": //,
            "has_next": //
        },
        "data": [
            {
                "id": // Thread id, type is string,
                "message": {
                    "sender": // Sender info,
                    "receiver": // Receiver info,
                    "content": // Message content, type is string
                },
                "is_read": // Has read or not, type is int
            }
        ]
    }
    """
    offset = request.args.get("offset", 0)
    try:
        offset = int(offset)
    except:
        offset = 0

    limit = request.args.get("limit", 20)
    try:
        limit = int(limit)
    except:
        limit = 20

    user_id = "a"  # User id got from cookie or db or cache.
    threads = models.Thread.get_threads(
        user_id, offset=offset, limit=limit)

    data = []

    for thread in threads:
        msg = models.Message.get_message(thread.message_id)
        data.append({
            "id": thread.thread_id,
            "message": {
                "sender": msg.sender_id,
                "receiver": msg.receiver_id,
                "content": msg.content,
                "created_at": msg.created_at
            },
            "is_read": thread.is_read
        })

    return jsonify({
        "data": data
    })


@thread_app.route("/inbox/<thread_id>", methods=["GET", "PUT"])
def show_threads_by_thread_id(thread_id):
    """Show specific threads by thread_id.

    :param str thread_id: Thread id

    HTTP GET
    :response:

    {
        "paging": {
            "prev": //
            "next": //
            "has_next": //
        },
        "data": [
            {
                "id": // Message id, type is int,
                "sender": // Sender info,
                "receiver": // Receiver info,
                "content": // Message content, type is string
            }
        ]
    }

    HTTP PUT
    :response:

    {
        "success": True
    }
    """
    if request.method == "PUT":
        models.Thread.read_thread(thread_id)
        return jsonify({"success": True})
    else:
        messages = models.Message.get_messages(thread_id)
        data = []

        for message in messages:
            data.append({
                "id": message.id,
                "sender": message.sender_id,
                "receiver": message.receiver_id,
                "content": message.content
            })
        return jsonify({
            "data": data
        })
