import sys
import socket
import fcntl
import struct
import array
import os

ICMP_ECHO_REQUEST = 8
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 4
SIOCGIFCONF = 0x8912
STUCT_SIZE_32 = 32
STUCT_SIZE_64 = 40
PLATFORM_32_MAX_NUMBER = 2 ** 32
DEFAULT_INTERFACES = 8

def list_interfaces():
    interfaces = []
    max_interfaces = DEFAULT_INTERFACES
    is_64bits = os.sys.maxsize > PLATFORM_32_MAX_NUMBER
    struct_size = STUCT_SIZE_64 if is_64bits else STUCT_SIZE_32
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        num_bytes = max_interfaces * struct_size
        interface_names = array.array('B', b'\0' * num_bytes)
        sock_info = fcntl.ioctl(
            sock.fileno(), SIOCGIFCONF, struct.pack('iP', num_bytes, interface_names.buffer_info()[0]))
        outbytes = struct.unpack('iL', sock_info)[0]
        if outbytes == num_bytes:
            max_interfaces *= 2
        else:
            break
    
    name_bytes = bytes(interface_names)
    for i in range(0, outbytes, struct_size):
        interface_name = name_bytes[i:i + 16].split(b'\0', 1)[0].decode('ascii', 'ignore')
        interfaces.append(interface_name)
    
    return interfaces
    
if __name__ == '__main__':
    interfaces = list_interfaces()
    print("List interface:", list_interfaces())
    #print ("This machine has %s network interfaces: %s." %(len(interfaces), interfaces))