import socket

def find_service_name():
    print("Port: %s => service name: %s" % (53, socket.getservbyport(53) ))

if __name__ == "__main__":
    find_service_name()