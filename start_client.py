from chat_client import ChatClient
from configs import Config, LoadFromParams

if __name__ == "__main__":
    config = Config(LoadFromParams())

    client = ChatClient(config.get_dict_config())

    print(client.send_message(b"Hello"))
