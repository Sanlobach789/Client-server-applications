import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 5050))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, address = sock.recvfrom(1024)
    print(address[0], address[1])
    if address not in client:
        client.append(address)  # Если такого клиента нету , то добавить
    for clients in client:
        if clients == address:
            continue  # Не отправлять данные клиенту, который их прислал
        sock.sendto(data, clients)
