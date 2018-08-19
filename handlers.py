class Handler:

    def handle(self, r, w, e):
        raise NotImplementedError


class SimpleHandler(Handler):

    def handle(self, r, w, e):
        clients = []
        for some_client in r:
            try:
                client_msg = some_client.recv(1024)
                print(client_msg)
                for some_client_w in w:
                    some_client_w.send(client_msg)

            except:
                clients.append(some_client)

        return clients
