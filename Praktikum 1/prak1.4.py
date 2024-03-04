import statistics

nilai = []
i = 0

while len(nilai) < 10: 
    i += 1
    print("Masukkan nilai ke ", i)
    x = int(input())
    nilai.append(x)
    
    
average = sum(nilai) / i
median = statistics.median(nilai)
modus = statistics.mode(nilai)

print("Rata-rata : ", average)
print("Median : ", median)
print("Modus : ", modus)