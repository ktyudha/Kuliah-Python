class Rekening:
    def __init__(self, saldo_awal):
        self.saldo = saldo_awal

    def lihat_saldo(self):
        return self.saldo

    def menabung(self, jumlah):
        self.saldo += jumlah

    def tarik_tunai(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi")
        else:
            self.saldo -= jumlah
            print("Penarikan berhasil. Saldo sekarang:", self.saldo)

# Contoh penggunaan
rekening_1 = Rekening(500000)  # Menggunakan saldo awal 500000
print("Saldo awal:", rekening_1.lihat_saldo())
rekening_1.menabung(1000000)
print("Setelah menabung:", rekening_1.lihat_saldo())
rekening_1.tarik_tunai(300000)
print("Setelah tarik tunai:", rekening_1.lihat_saldo())
