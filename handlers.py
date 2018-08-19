import jim
import json


class Handler:

    def handle(self, r, w, e, clients):
        raise NotImplementedError

    def client_connected(self, client, addr):
        raise NotImplementedError


class SimpleHandler(Handler):

    def handle(self, r, w, e, clients):
        msg = jim.JimMsg()
        clients_off = []
        for some_client in r:
            try:
                data = some_client.recv(1024)
                dic = jim.convert_from_bytes(data)
                msg.create_from_dict(dic)
                print(msg)

                for c in w:
                    if clients[msg.name] == c:
                        c.send(msg.message.encode('utf-8'))

            except:
                clients_off.append(some_client)

        return clients_off

    def client_connected(self, client, addr):

        presence = json.loads(client.recv(1024).decode('utf-8'))

        name = presence['user']['account_name']

        client.send(json.dumps({'responce': 200}).encode('utf-8'))

        return name
