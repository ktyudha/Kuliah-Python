import socket
import sys
import argparse

host = '127.0.0.1'
data_payload = 2048

def echo_client(port):
    """A Simple echo server"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    message = 'This is the message. It will be repeated.'

    try:
        message = "Test message. This will be echoed"
        print("Sending %s" % message)

        sent = sock.sendto(message.encode('utf8'),server_address)

        data, server = sock.recvfrom(data_payload)
        print("received %s"% data)
    
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action = 'store', dest ="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)