import socket

def main():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    print("HOSTNAME: %s" % hostname)
    print("IP: %s" % ip_address)

if __name__ == "__main__":
    main()