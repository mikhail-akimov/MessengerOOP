from subprocess import Popen, CREATE_NEW_CONSOLE

for i in range(30):
    Popen('python client_read.py', creationflags=CREATE_NEW_CONSOLE)
