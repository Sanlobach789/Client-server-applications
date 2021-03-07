import socket

import click

from gb_chat.client_socket import ClientSocket


@click.command()
@click.option("--address")
@click.option("--port")
def main(address, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((address, int(port)))
        client_socket = ClientSocket(s)


if __name__ == "__main__":
    main()
