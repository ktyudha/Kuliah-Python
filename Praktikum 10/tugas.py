import socket
import os
BUFSIZE = 1024

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
            print("Ping to", interface)
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