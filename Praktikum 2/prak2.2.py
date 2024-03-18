from total_belanja import hitung_pembelian

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
        print("Total pembelian:", hitung_pembelian(belanja))



if __name__ == "__main__":
    main()
