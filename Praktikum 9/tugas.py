import os
import socket
import fcntl
import struct
import array
import argparse
import subprocess

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

def ping_website(address):
    try:
        output = subprocess.check_output(["ping", "-c", "1", address])
        delay = float(output.split(b"time=")[1].split(b" ")[0])
        return delay
    except subprocess.CalledProcessError:
        return None

def get_ip_address(host):
    try:
        ip_address = socket.gethostbyname(host)
        return ip_address
    except socket.gaierror:
        return None

def main_menu():
    print("\nMENU PILIHAN")
    print("1. Mengetahui delay ke suatu alamat")
    print("2. Mengetahui list interface")
    print("3. Mengetahui alamat IP")
    print("0. Keluar")

def main():
    while True:
        main_menu()
        choice = input("Masukkan pilihan anda: ")
        if choice == '1':
            address = input("Masukkan alamat web: ")
            print("Ping to", address)
            delay = ping_website(address)
            if delay is not None:
                print("Get pong in", delay, "ms")
            else:
                print("Ping failed.")
        elif choice == '2':
            print("List interface:", list_interfaces())
        elif choice == '3':
            host = input("Masukkan nama host: ")
            ip_address = get_ip_address(host)
            if ip_address:
                print("IP address of", host, "is", ip_address)
            else:
                print("Failed to resolve IP address for", host)
        elif choice == '0':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
