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
    