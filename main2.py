from chat_server import ChatServer
from chat_client import ChatClient
from configs import Config, LoadFromArgparse, LoadFromConsole, LoadFromFile, LoadFromParams
from handlers import SimpleHandler

if __name__ == "__main__":

    config = Config(LoadFromParams())

    server = ChatServer(config.get_dict_config())

    server.serve_forever(SimpleHandler())

