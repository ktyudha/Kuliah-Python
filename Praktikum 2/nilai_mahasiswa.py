# nilai_mahasiswa.py

import matplotlib.pyplot as plt

def hitung_nilai_akhir(tugas, kuis, uts, uas):
    nilai_akhir = 0.3 * tugas + 0.2 * kuis + 0.2 * uts + 0.3 * uas
    return nilai_akhir

def konversi_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 80:
        return 'A'
    elif nilai_akhir >= 70:
        return 'B'
    elif nilai_akhir >= 60:
        return 'C'
    elif nilai_akhir >= 50:
        return 'D'
    else:
        return 'E'

def analisis_nilai_huruf(data_mahasiswa):
    jumlah_nilai_a = jumlah_nilai_b = jumlah_nilai_c = jumlah_nilai_d = jumlah_nilai_e = 0

    for i, (nama, tugas, kuis, uts, uas) in enumerate(data_mahasiswa, start=1):
        nilai_akhir = hitung_nilai_akhir(tugas, kuis, uts, uas)
        nilai_huruf = konversi_nilai_huruf(nilai_akhir)

        # Menghitung jumlah nilai huruf
        if nilai_huruf == 'A':
            jumlah_nilai_a += 1
        elif nilai_huruf == 'B':
            jumlah_nilai_b += 1
        elif nilai_huruf == 'C':
            jumlah_nilai_c += 1
        elif nilai_huruf == 'D':
            jumlah_nilai_d += 1
        elif nilai_huruf == 'E':
            jumlah_nilai_e += 1

    return jumlah_nilai_a, jumlah_nilai_b, jumlah_nilai_c, jumlah_nilai_d, jumlah_nilai_e

def plot_grafik_batang(kategori, jumlah_nilai):
    plt.bar(kategori, jumlah_nilai, color=['green', 'blue', 'yellow', 'orange', 'red'])
    plt.xlabel('Nilai Huruf')
    plt.ylabel('Jumlah Mahasiswa')
    plt.title('Grafik Jumlah Nilai Huruf Mahasiswa')
    plt.show()

def tampilkan_data_mahasiswa(data_mahasiswa):
    print("-" * 80)
    print("{:<5} {:<15} {:<7} {:<7} {:<7} {:<11} {:<13}".format(
        "No.", "Nama Mhs", "N.Tugas", "N.Kuis", "N.UTS", "N.UAS", "NilaiAkhir", "Nilai Huruf"
    ))
    print("-" * 80)

    for i, (nama, tugas, kuis, uts, uas) in enumerate(data_mahasiswa, start=1):
        nilai_akhir = hitung_nilai_akhir(tugas, kuis, uts, uas)
        nilai_huruf = konversi_nilai_huruf(nilai_akhir)

        print("{:<5} {:<15} {:<7} {:<7} {:<7} {:<11.2f} {:<13}".format(
            i, nama, tugas, kuis, uts, uas, nilai_akhir, nilai_huruf
        ))
