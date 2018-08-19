from chat import Chat
import select


class ChatServer(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.client = None
        self.address = None
        self.connect()
        self.clients = []

    def _setup(self, config):
        self.timeout = config["timeout"]
        self.listen = config["listen"]

    def send_message(self, msg):
        if self.client is not None:
            self.client.send(msg)

    def receive_message(self):
        raise NotImplementedError

    def connect(self):
        self.s.bind((self.host, self.port))
        self.s.listen(self.listen)
        self.s.settimeout(self.timeout)

    def serve_forever(self, handler):

        while True:
            try:
                client, addr = self.s.accept()

            except OSError as e:
                pass
            else:
                print('Получен запрос на соединение от {}'.format(addr))
                self.clients.append(client)
            finally:
                r = []
                w = []
                e = []
                try:
                    r, w, e = select.select(self.clients, self.clients, [], 0)
                except Exception:
                    pass

                clients_off = handler.handle(r, w, e)

                for c in clients_off:
                    print(f"Клиент отключился: {c}")
                    self.clients.remove(c)

