import socket
import sys
import argparse

host ='127.0.0.1'
data_paylpad  = 2048
backlog = 5

def echo_server(port):
    """A simple echo server"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print("Starting echo server on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen(backlog)

    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_paylpad)
        
        if data:
            print("Data: %s" %data)
            client.send(data)
            print("Sent: %s bytes back to %s" % (data, address))
        # client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store', type=int, dest='port', required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)