kelas = []
i = 0

juml_data = int(input("Masukkan Jumlah Data : "))

while len(kelas) < juml_data: 
    i += 1

    nama = input("\nMasukka Nama : ")
    tugas = int(input("Masukkan Nilai Tugas : "))
    kuis = int(input("Masukka Nilai Kuis : "))
    uts = int(input("Masukkan Nilai UTS : "))
    uas = int(input("Masukkan Nilai UAS : "))
    akhir = int(input("Masukkan Nilai Akhir : "))

    data = {"nama" : nama, "tugas" : tugas, "kuis" : kuis, "uts" : uts, "uas" : uas, "akhir" : akhir}
    kelas.append(data)

print("\nNama\t Tugas\t Kuis\t UTS\t UAS\t AKHIR\t AVERAGE")

for obj in kelas:
    total_nilai = obj["tugas"] + obj["kuis"] + obj["uts"] + obj["akhir"] 
    average = total_nilai / 4

    print(f"{obj['nama']}\t {obj['tugas']}\t {obj['kuis']}\t {obj['uts']}\t {obj['uas']}\t {obj['akhir']}\t {average}")