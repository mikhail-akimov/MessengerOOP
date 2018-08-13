from chat import Chat
import socket


class ChatClient(Chat):

    def __init__(self, config):
        super().__init__(config)
        self.connect()

    def send_message(self, msg):
        raise NotImplementedError

    def receive_message(self):
        return self.s.recv(1024)

    def connect(self):
        self.s.connect((self.host, self.port))

    def start_chat(self):
        raise NotImplementedError
