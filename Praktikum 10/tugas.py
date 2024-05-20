import socket
import os
import argparse
import socket
import struct
import fcntl
import nmap

BUFSIZE = 1024
SAMPLE_PORTS = '21-23'

def get_interface_status(ifname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address = socket.inet_ntoa(fcntl.ioctl(sock.fileno(),0x8915, struct.pack(b'256s', bytes(ifname[:15], 'utf-8')))[20:24])
    nm = nmap.PortScanner()
    nm.scan(ip_address, SAMPLE_PORTS)
    return nm[ip_address].state()

def test_socketpair():
    """ Test Unix socketpair"""
    parent, child = socket.socketpair()
    pid = os.fork()
    try:
        if pid:
            print ("@Parent, sending message...")
            child.close()
            parent.sendall(bytes("Hello from parent!", 'utf-8'))
            response = parent.recv(BUFSIZE)
            print ("Response from child:", response)
            parent.close()
        else:
            print ("@Child, waiting for message from parent")
            parent.close()
            message = child.recv(BUFSIZE)
            print ("Message from parent:", message)
            child.sendall(bytes("Hello from child!!", 'utf-8'))
            child.close()

    except Exception as err:
        print ("Error: %s" %err)

def main_menu():
    print("\nMENU PILIHAN")
    print("1. Mengetahui delay ke suatu alamat")
    print("2. Mengetahui list interface")
    print("0. Keluar")

def main():
    while True:
        main_menu()
        choice = input("Masukkan pilihan anda: ")
        if choice == '1':
            interface = input("Masukkan Interface: ")
            print ("Interface [%s] is: %s" %(interface, get_interface_status(interface)))
        elif choice == '2':
            test_socketpair()
            break
        elif choice == '0':
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()