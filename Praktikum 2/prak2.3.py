# Modul (module) untuk menghitung bilangan genap dan ganjil
from operasi_hitung import hitung_genap_ganjil

def main():
    try:
        # Input dari program utama
        jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))
        data = []

        # Input bilangan secara acak
        for i in range(jumlah_bilangan):
            bilangan = int(input(f"Masukkan bilangan ke-{i + 1}: "))
            data.append(bilangan)

        # Memanggil modul untuk menghitung bilangan genap dan ganjil
        hasil_genap, hasil_ganjil = hitung_genap_ganjil(data)

        # Menampilkan hasil
        print(f"Jumlah bilangan genap: {len(hasil_genap)} yaitu {', '.join(map(str, hasil_genap))}")
        print(f"Jumlah bilangan ganjil: {len(hasil_ganjil)} yaitu {', '.join(map(str, hasil_ganjil))}")

    except ValueError:
        print("Masukkan harus berupa bilangan bulat.")

if __name__ == "__main__":
    main()
