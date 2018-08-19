import for_run.utils as utils
import for_run.jim as jim
import random

with utils.create_tcp_client_socket(utils.HOST, utils.PORT) as s:
    s.send(jim.get_presence_message(str(random.randint(1, 10 ** 10)), "hello,world").encode("utf-8"))
    s.recv(1024)

    s.send(utils.str_to_bytes(jim.get_message("1181967759", "Pak")))
