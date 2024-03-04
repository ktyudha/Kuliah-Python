def hitung_pembelian(barang):
    total_pembelian = 0
    
    # Header tabel
    print("{:<15} {:<7} {:<7}".format("\nNama", "Jumlah", "Harga"))
    print("-" * 30)
    
    for item in barang:
        nama_barang, harga_barang, jumlah_barang = item
        sub_total = harga_barang * jumlah_barang
        total_pembelian += sub_total
        print("{:<15} {:<7} {:<7}".format(nama_barang, jumlah_barang, sub_total))
    
    print("-" * 30)
    print("Total pembelian:", total_pembelian)

def main():
    # Input dari pengguna
    belanja = []

    while True:
        entry_data =  input("Entry data (Y/T)\t: ")
        if entry_data.lower() == 't':
            break
        else:
            nama_barang = input("Nama Barang\t: ")
            harga_barang = float(input("Harga\t\t: "))
            jumlah_barang = int(input("Jumlah\t\t: "))
            belanja.append((nama_barang, harga_barang, jumlah_barang))
            # Memanggil fungsi untuk menghitung pembelian
        hitung_pembelian(belanja)


if __name__ == "__main__":
    main()
