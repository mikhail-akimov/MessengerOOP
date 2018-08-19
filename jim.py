import json
import time


def get_unix_timestamp():
    return int(time.time())


class Jim:
    def __init__(self, **kwargs):
        pass

    def __str__(self):
        pass


class JimMessage:
    message = {}

    def __init__(self):
        self.message.update({"time": get_unix_timestamp()})

    def __str__(self):
        return json.dumps(self.message)

    def _set_action(self, action):
        self.message.update({"action": action})

    def _set_user(self, account_name, status):
        self.message.update(
            {
                "user": {
                    "account_name": account_name,
                    "status": status
                }
            }
        )

    def _set_room(self, room):
        self.message.update(
            {
                "room": room
            }
        )


class JimPresence(JimMessage):

    def __init__(self, account_name, status):
        super().__init__()
        super()._set_action("presence")
        super()._set_user(account_name, status)


class JimProbe(JimMessage):

    def __init__(self):
        super().__init__()
        super()._set_action("probe")


class JimMsg(JimMessage):

    def __init__(self):
        super().__init__()
        super()._set_action("msg")


class JimAuthenticate(JimMessage):

    def __init__(self, account_name, status):
        super().__init__()
        super()._set_action("authenticate")
        super()._set_user(account_name, status)


class JimJoin(JimMessage):

    def __init__(self, room):
        super().__init__()
        super()._set_action("join")
        super()._set_room(room)


class JimLeave(JimMessage):

    def __init__(self, room):
        super().__init__()
        super()._set_action("leave")
        super()._set_room(room)


class JimQuit(JimMessage):

    def __init__(self):
        super().__init__()
        super()._set_action("quit")
