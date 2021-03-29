from socket import *
# from handler import MessageHandler

ADDRESS = ('localhost', 9999)


def client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            msg = input('input your message: ')
            if msg == 'exit':
                break
            sock.send(msg.encode("utf-8"))
            data = sock.recv(1024).decode("utf-8")
            print(data)


if __name__ == "__main__":
    client()
