import socket

def find_service_name(data):
    service = socket.getservbyport(data)
    return service

def get_service(dst_web):
    ip_address = socket.gethostbyname(dst_web)

    hostname = socket.gethostname()
    myIp_address = socket.gethostbyname(hostname)
    return {'ip_address': ip_address, 'hostname': hostname, 'myIp_address': myIp_address}

def main():
     while True:
        entry_data =  input("Entry data (Y/T)\t: ")
        if entry_data.lower() == "t":
            break
        else:
            pilihan =  int(input("Masukkan pilihan (1/2)\t: "))

            if pilihan == 1:
                port = int(input("Masukkan port protocol: "))
                print("Port: %s => service name: %s" % (port, find_service_name(port) ))

            else:
                dst_web = input("Masukkan alamat web\t: ")
                service_info = get_service(dst_web)
                print("Anda mengakses %s dengan alamat IP %s\n dari komputer %s dengan alamt IP %s"%(dst_web, service_info['ip_address'],
                service_info['hostname'], service_info['myIp_address']) )
                
if __name__ == "__main__":
    main() 