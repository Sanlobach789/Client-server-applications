import selectors
import socket
import errno

server = ('localhost', 9999)


def read_sock():
    pass


class Client:
    # with socket(AF_INET, SOCK_STREAM) as sock:
    #     sock.connect(ADDRESS)
    #     while True:
    #         msg = input('input your message: ')
    #         if msg == 'exit':
    #             break
    #         sock.send(msg.encode("utf-8"))
    #         data = sock.recv(1024).decode("utf-8")
    #         print(data)
    def __init__(self, alias):
        alias = alias


def main_loop(sel):
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


def main():
    alias = input('Введите ваш ник: ')
    msg = input('сообщение: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect(server)
        # client_sock.bind(("", 0))
        # client_sock.listen()
        client_sock.setblocking(False)

        with selectors.DefaultSelector() as sel:
            sel.register(
                client_sock,
                selectors.EVENT_READ | selectors.EVENT_WRITE,

            )

            main_loop(sel)


if __name__ == "__main__":
    main()
