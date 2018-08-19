from chat_server import ChatServer
from configs import Config, LoadFromParams
from handlers import SimpleHandler

if __name__ == "__main__":
    config = Config(LoadFromParams())

    server = ChatServer(config.get_dict_config())

    server.serve_forever(SimpleHandler())
