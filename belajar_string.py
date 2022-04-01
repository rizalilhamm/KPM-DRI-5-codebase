# Belajar String dalam Python: Dalam pemrograman komputer, string secara umum merupakan urutan karakter


# Akses nilai string
nilai_char = 'Banda Aceh'
print('Nilai Index ke 5', nilai_char[5])

for i in range(0, len(nilai_char)):
    print('nilai index ke', i, 'Adalah: ', nilai_char[i])
print(nilai_char)

# Update nilai String
# nilai_char[0] = 'b'
# print(nilai_char)

nilai_char2 = ' Disebut Kotaraja'

# Operator Spesial menggabungkan 2 string
print(nilai_char + nilai_char2)

# Triple Quote string
panjang = """Banda Aceh adalah kota yang terletak di ujung barat Sumatra
            jalsdkfjasdlkfj
        """
print(panjang)

# Built-in Function String
print(panjang.upper()) # Text jadi huruf kapital semua

print(panjang.lower()) # Text jadi huruf kecil semua
