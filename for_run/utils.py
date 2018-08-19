import socket

HOST = 'localhost'
PORT = 7777
ENCODING = 'utf-8'


def create_tcp_client_socket(address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((address, port))

    return s


def str_to_bytes(msg):
    return msg.encode(ENCODING)


def bytes_to_str(msg):
    return msg.decode(ENCODING)
