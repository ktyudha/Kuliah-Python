import matplotlib.pyplot as plt
import math
# Fungsi Erlang B untuk menghitung probabilitas blocking
def erlang_b(a, n):
    numerator = (a ** n) / math.factorial(n)
    denominator = sum([(a ** i) / math.factorial(i) for i in range(n + 1)])
    return numerator / denominator

# Fungsi untuk mencari jumlah trunk yang diperlukan
def find_trunks(a, pb):
    n = 1
    while True:
        if erlang_b(a, n) <= pb:
            return n
        n += 1

# Intensitas trafik (a) dan probabilitas blocking (Pb) yang diberikan
traffic_intensity = [0.1, 0.5, 1]
blocking_probabilities = [0.001, 0.005, 0.01]

# List untuk menyimpan jumlah trunk yang diperlukan
trunks_needed = []

# Menghitung jumlah trunk (n) untuk setiap kombinasi a dan Pb
for a in traffic_intensity:
    for pb in blocking_probabilities:
        n = find_trunks(a, pb)
        trunks_needed.append((a, pb, n))

# Membuat plot
plt.figure(figsize=(10, 6))
for pb in blocking_probabilities:
    trunks = [data[2] for data in trunks_needed if data[1] == pb]
    plt.plot(traffic_intensity, trunks, label=f'Blocking Prob. {pb * 100}%')
plt.xlabel('Traffic Intensity (Erlangs)')
plt.ylabel('Number of Trunks')
plt.title('Relationship between Traffic Intensity and Number of Trunks')
plt.legend()
plt.grid(True)
plt.show()
