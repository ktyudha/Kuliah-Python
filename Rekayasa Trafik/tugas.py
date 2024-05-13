import matplotlib.pyplot as plt

# Definisikan fungsi untuk menghitung jumlah trunk berdasarkan intensitas trafik (a) dan probabilitas blocking (Pb)
def hitung_trunk(a, Pb):
    return a / (1 - Pb)

# Definisikan nilai intensitas trafik (a) dari 1 hingga 10
a_values = list(range(1, 11))

# Definisikan probabilitas blocking (Pb) yang berbeda
prob_blocking_values = [0.001, 0.005, 0.01]

# Plot grafik untuk setiap probabilitas blocking (Pb)
for Pb in prob_blocking_values:
    trunk_values = [hitung_trunk(a, Pb) for a in a_values]
    plt.plot(a_values, trunk_values, marker='o', label=f'Pb={Pb}')

# Tambahkan judul dan label sumbu pada grafik
plt.title('Hubungan Intensitas Trafik dan Jumlah Trunk dengan Probabilitas Blocking yang Berbeda')
plt.xlabel('Intensitas Trafik (a)')
plt.ylabel('Jumlah Trunk (n)')

# Tampilkan legenda
plt.legend()

# Tampilkan grafik
plt.grid(True)
plt.show()
