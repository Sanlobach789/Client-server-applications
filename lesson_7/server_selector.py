import errno
import selectors
import socket


def accept(sel, clients, sock, _):
    conn, addr = sock.accept()
    print(f"РљР»РёРµРЅС‚ {conn.fileno()} {addr} РїРѕРґРєР»СЋС‡РёР»СЃСЏ")
    conn.setblocking(False)
    sel.register(
        conn,
        selectors.EVENT_READ | selectors.EVENT_WRITE,
        lambda conn, mask: process(sel, clients, conn, mask),
    )
    clients[conn] = b""


def disconnect(sel, clients, conn):
    print(f"РљР»РёРµРЅС‚ {conn.fileno()} {conn.getpeername()} РѕС‚РєР»СЋС‡РёР»СЃСЏ")
    sel.unregister(conn)
    conn.close()
    del clients[conn]


def recv_all(conn):
    data = b""
    try:
        while True:
            data += conn.recv(1000)
    except socket.error as exc:
        err = exc.args[0]
        if err in (errno.EAGAIN, errno.EWOULDBLOCK):
            return data

        raise


def process(sel, clients, conn, mask):
    if mask & selectors.EVENT_READ:
        data = recv_all(conn)
        if data:
            for other_conn in clients:
                if conn is other_conn:
                    continue

                clients[other_conn] += data
        else:
            disconnect(sel, clients, conn)

    if mask & selectors.EVENT_WRITE:
        out_data = clients[conn]
        if out_data:
            sent_size = conn.send(out_data)
            if sent_size == 0:
                disconnect(sel, clients, conn)
                return

            clients[conn] = out_data[sent_size:]


def main_loop(sel):
    while True:
        events = sel.select()
        for key, mask in events:
            callback = key.data
            callback(key.fileobj, mask)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind(("", 10000))
        server_sock.listen()
        server_sock.setblocking(False)

        clients = {}

        with selectors.DefaultSelector() as sel:
            sel.register(
                server_sock,
                selectors.EVENT_READ,
                lambda conn, mask: accept(sel, clients, conn, mask),
            )

            main_loop(sel)


if __name__ == "__main__":
    main()
