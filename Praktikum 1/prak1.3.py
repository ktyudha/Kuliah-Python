# jumMatriks = int(input("Masukkan jumlah Matriks : "))
# ordo = int(input("Masukkan jumlah ordo : "))

# matrix = []
# dataMatrix = []
# hasilMatrix = []

# for index in range(jumMatriks):
#     for index in range(ordo):
        

#         print(index)

def input_matriks(ukuran_baris, ukuran_kolom):
    matriks = []

    print(f"Masukkan elemen-elemen matriks {ukuran_baris}x{ukuran_kolom}:")
    for i in range(ukuran_baris):
        baris = []
        for j in range(ukuran_kolom):
            elemen = float(input(f"Masukkan elemen matriks [{i+1}][{j+1}]: "))
            baris.append(elemen)
        matriks.append(baris)

    return matriks

def tambah_matriks(matriks1, matriks2):
    # Pastikan matriks memiliki ukuran yang sama
    if len(matriks1) != len(matriks2) or len(matriks1[0]) != len(matriks2[0]):
        print("Ukuran matriks tidak cocok untuk penjumlahan.")
        return None

    # Inisialisasi matriks hasil dengan ukuran yang sama
    hasil = [[0 for _ in range(len(matriks1[0]))] for _ in range(len(matriks1))]

    # Lakukan penjumlahan elemen per elemen
    for i in range(len(matriks1)):
        for j in range(len(matriks1[0])):
            hasil[i][j] = matriks1[i][j] + matriks2[i][j]

    return hasil

# Input matriks pertama
baris1 = int(input("Masukkan jumlah baris matriks pertama: "))
kolom1 = int(input("Masukkan jumlah kolom matriks pertama: "))
matriks1 = input_matriks(baris1, kolom1)

# Input matriks kedua
baris2 = int(input("Masukkan jumlah baris matriks kedua: "))
kolom2 = int(input("Masukkan jumlah kolom matriks kedua: "))
matriks2 = input_matriks(baris2, kolom2)

# Tampilkan matriks input
print("\nMatriks pertama:")
for baris in matriks1:
    print(baris)

print("\nMatriks kedua:")
for baris in matriks2:
    print(baris)

# Hitung dan tampilkan hasil penjumlahan
hasil_penjumlahan = tambah_matriks(matriks1, matriks2)
if hasil_penjumlahan:
    print("\nHasil penjumlahan:")
    for baris in hasil_penjumlahan:
        print(baris)

