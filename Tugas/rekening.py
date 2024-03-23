class Rekening:
    def __init__(self, pin ):
        self.pin = pin
        self.saldo = 5000
        self.name = "Kurniawan Try Yudha"
        self.no_rek = "085848250548"

    def authentication(self):
        pin_atm = "331144"
        if pin_atm == self.pin:
            return True
            
    def lihat_saldo(self):
        print(f"Saldo\t: {self.saldo}")

    def menabung(self, jumlah):
        self.saldo += jumlah
        print(f"{self.name} menabung sejumlah {jumlah}. Saldo sekarang: {self.saldo}")

    def tarik_tunai(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"{self.nama_pemilik} menarik tunai sejumlah {jumlah}. Saldo sekarang: {self.saldo}")
        else:
            print("Saldo tidak mencukupi.")


pin = input("Masukkan Pin Rekening: ")

rekening = Rekening(pin)

if rekening.authentication():
    while True:
        print("\nMenu ATM\n1. Cek saldo\n2. Setor\n3. Tarik")
        pilihan = int(input("Masukkan pilihan (1/2/3): "))

        if pilihan == 1:
            rekening.lihat_saldo()
        elif pilihan == 2:
            setor = int(input("Masukkan jumlah yang ingin ditabung: "))
            rekening.menabung(setor)
        elif pilihan == 3:
            tarik = int(input("Masukkan jumlah yang ingin ditarik: "))
            rekening.tarik_tunai(tarik)
        else:
            print("Data input incorrect")
        entry_data =  input("\nTransaksi lain (Y/T)\t: ")
        if entry_data.lower() != 'y':
            break
else:
    print("!!! Pin Rekening input incorrect !!!")