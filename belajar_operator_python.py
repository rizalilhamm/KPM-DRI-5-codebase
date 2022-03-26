"""
Belajar Operator pada Python

1. Operasi Aritmatika
2. Operasi Perbandingan
3. Operasi Penugasan
4. Operator Prioritas

1. Aritmatika 
    a. Penjumlahan
    b. Pengurangan
    c. Perkalian
    d. Pembagian

2. Perbandingan
    a. Sama dengan (==)
    b. Tidak sama dengan (!=)
    c. Lebih besar dari (>)
    d. Lebih kecil dari (<)
    e. Lebih besar dari atau sama dengan (>=)
    f. Lebih kecil dari atau sama dengan (<=)

3. Operator penugasan
    a. += 
    b. -=
    c. *=
    d. //=

4. Proiritas Operator(Opsional)
    a. Perkalian
    b. Pembagian
    c. Pemjumlahan
    d. Pengurangan
"""
angka1 = 10
angka2 = 20

# BELAJAR ARITMATIKA
# Aritmatika pemjumlahan
hasil_penjumlahan = angka1 + angka2
print("Hasil pemjumlahan: ", hasil_penjumlahan)

# Aritmatika pengurangan
hasil_pengurangan = angka2 - angka1
print("Hasil Pengurangan: ", hasil_pengurangan) # 10

# Perkalian
a = 3
b = 4
hasil_perkalian = a * b
print("Hasil Perkalian: ", hasil_perkalian) # 12

# Pembagian
c = 100
d = 5
hasil_pembagian = c / d
print("Hasil pembagian: ", hasil_pembagian) # 20

# BELAJAR OPERATOR PERBANDINGAN
print(1 == 1) # True
print(1 == 2) # False
print(2 > 1) # True
print(1 > 10) # False
print(10 < 100) # True
print(10 < 3) # False

print(10 >= 11) # False
print(10 >= 10) # True

print(10 <= 10) # True
print(10 <= 3) # False

print(100 != 90) # True
print(10 != 10) # False


# BELAJAR OPERATOR PENUGASAN
p = 10
print("Nilai p: ", p)
p += 1 # 11 (p += 1 == | p = p + 1
print("Penugasan tambah: ", p) # 11

p -= 1 # 10 | p = p - 1
print("Penugasan kurang", p) # 10

p *= 2 # 20 | p = p * 2
print("Penugasan kali: ", p) # 20

p //= 5 # p = p // 2
print("Penugasan Bagi: ", p) # 4