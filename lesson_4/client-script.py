# Программа клиента для отправки приветствия серверу и получения ответа
import time
from socket import *
from handler import MessageHandler

# from sys import argv

# addr, port = argv
# if not addr or not port:
#     raise ValueError('Введены не все параметры')

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8007))
# s.connect((str(addr), port))
msg = {
    "action": "presence",
    "time": str(time.time()),
    "type": "status",
    "user": {
        "account_name": "Client_Script",
        "status": "Yep, I am here!"
    }
}
msg_json = MessageHandler.create_msg(msg)
s.send(msg_json)

data = MessageHandler.load_msg(s.recv(1000000))
print('Сообщение от сервера: ', data)
s.close()