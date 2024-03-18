import socket

def get_remote_machine_info():
    remote_host = "www.pens.ac.id"
    ip_address = socket.gethostbyname(remote_host)
    try:
        print ("IP Address of %s: %s" %(remote_host, ip_address))
    except socket.error as err_msg:
        print("%s: %s" %remote_host, err_msg)

if __name__ == "__main__":
    get_remote_machine_info()