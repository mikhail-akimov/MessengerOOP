from chat import Chat
import select


class ChatServer(Chat):

    def __init__(self, config):
        super().__init__(config)
        self._setup(config)
        self.client = None
        self.address = None
        self.connect()
        self.clients = dict()

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

    def _delete_clients(self, clients):
        print("Отключаю вырубившихся клиентов", clients)
        self.clients = {key:val for key,val in self.clients.items() if val not in clients}

    def serve_forever(self, handler):
        print("Сервер запущен")
        while True:
            try:
                client, addr = self.s.accept()

            except OSError as e:
                pass
            else:
                print('Получен запрос на соединение от {}'.format(addr))

                name = handler.client_connected(client, addr)

                self.clients.update({name: client})
                print(self.clients)
            finally:
                r = []
                w = []
                e = []
                try:
                    r, w, e = select.select(self.clients.values(), self.clients.values(), [], 0)
                except Exception:
                    pass

                if len(r) > 0 or len(w) > 0 or len(e) > 0:
                    clients_off = handler.handle(r, w, e, self.clients)

                    if len(clients_off) > 0:
                        self._delete_clients(clients_off)
