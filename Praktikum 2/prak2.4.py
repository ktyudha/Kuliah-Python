# main_program.py

from nilai_mahasiswa import tampilkan_data_mahasiswa, analisis_nilai_huruf, plot_grafik_batang

def main():
    data_mahasiswa = []
    
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    
    for i in range(jumlah_mahasiswa):
        nama = input("Masukkan nama mahasiswa ke-{}: ".format(i + 1))
        tugas = float(input("Masukkan nilai tugas mahasiswa ke-{}: ".format(i + 1)))
        kuis = float(input("Masukkan nilai kuis mahasiswa ke-{}: ".format(i + 1)))
        uts = float(input("Masukkan nilai UTS mahasiswa ke-{}: ".format(i + 1)))
        uas = float(input("Masukkan nilai UAS mahasiswa ke-{}: ".format(i + 1)))
        
        data_mahasiswa.append((nama, tugas, kuis, uts, uas))

    tampilkan_data_mahasiswa(data_mahasiswa)

    jumlah_nilai_a, jumlah_nilai_b, jumlah_nilai_c, jumlah_nilai_d, jumlah_nilai_e = analisis_nilai_huruf(data_mahasiswa)

    print("\nJumlah A: {}".format(jumlah_nilai_a))
    print("Jumlah B: {}".format(jumlah_nilai_b))
    print("Jumlah C: {}".format(jumlah_nilai_c))
    print("Jumlah D: {}".format(jumlah_nilai_d))
    print("Jumlah E: {}".format(jumlah_nilai_e))

    kategori = ['A', 'B', 'C', 'D', 'E']
    jumlah_nilai = [jumlah_nilai_a, jumlah_nilai_b, jumlah_nilai_c, jumlah_nilai_d, jumlah_nilai_e]

    plot_grafik_batang(kategori, jumlah_nilai)

if __name__ == "__main__":
    main()
