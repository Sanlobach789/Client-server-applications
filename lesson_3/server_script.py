# Программа сервера для получения приветствия от клиента и отправки ответа
from socket import *
import time
from sys import argv
from lesson_3.handler import MessageHandler


# addr, port = argv
# if not addr or not port:
#     raise ValueError('Введены не все параметры')

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8007))
# s.bind((str(addr), port))
s.listen(5)


while True:
    client, addr = s.accept()
    data = MessageHandler.load_msg(client.recv(1000000))
    print('Сообщение: ', data, ', было отправлено клиентом: ', addr)
    msg = {
        "action": "probe",
        "time": str(time.time()),
    }
    msg_json = MessageHandler.create_msg(msg)
    client.send(msg_json)
    client.close()