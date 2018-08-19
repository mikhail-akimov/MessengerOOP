import json
import datetime


def get_presence_message(user_name, status):
    return json.dumps({
        "action": "presence",
        "time": int(datetime.datetime.now().timestamp()),
        "type": "status",
        "user": {
            "account_name": user_name,
            "status": status
        }
    })


def get_message(user_name, status):
    return json.dumps({
        "action": "presence",
        "time": int(datetime.datetime.now().timestamp()),
        "to": user_name,
        "from": status,
        "message": "hello, world!"
    })
