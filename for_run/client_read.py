import for_run.utils as utils
import for_run.jim as jim
import random

with utils.create_tcp_client_socket(utils.HOST, utils.PORT) as s:
    print("Enter in read socket")

    s.send(jim.get_presence_message(str(random.randint(1, 10 ** 10)), "hello,world").encode("utf-8"))
    s.recv(1024)
    while True:
        msg = s.recv(1024)

        print(utils.bytes_to_str(msg))
