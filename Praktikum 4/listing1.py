import socket 

def convert_integer():
    data = 1
    #32bit
    print("Original: %s => Long\thost byte order: %s, Network byte order: %s" % (data, socket.ntohl(data), socket.htonl(data)))
    #16bit
    print("Original: %s => Long\thost byte order: %s, Network byte order: %s" % (data, socket.ntohs(data), socket.htons(data)))

if __name__ == "__main__":
    convert_integer()