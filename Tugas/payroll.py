class Penggajian:
    def __init__(self, nama, gaji_pokok, jam_lembur, upah_lembur):
        self.nama = nama
        self.gaji_pokok = gaji_pokok
        self.jam_lembur = jam_lembur
        self.upah_lembur = upah_lembur

    def _hitung_gaji(self):
        gaji = (self.upah_lembur * self.jam_lembur) + self.gaji_pokok
        return gaji

    def cetak_gaji(self):
        print(f"Gaji {self.nama}: Rp {self._hitung_gaji():,.2f}")


while True:
    # Input dari pengguna
    nama = input("Masukkan nama karyawan: ")
    gaji_pokok = float(input("Masukkan gaji pokok karyawan: "))
    jam_lembur = float(input("Masukkan jumlah jam lembur: "))
    upah_lembur = float(input("Masukkan upah lembur per jam: "))

    # Membuat objek Penggajian
    karyawan = Penggajian(nama, gaji_pokok, jam_lembur, upah_lembur)

    # Mencetak gaji karyawan
    karyawan.cetak_gaji()
    entry_data =  input("\nHitung gaji lagi? (Y/T)\t: ")
    if entry_data.lower() != 'y':
        break

