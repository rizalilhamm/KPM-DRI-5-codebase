# Belajar Type Data
# Tipe data adalah suatu media atau memori pada komputer yang digunakan untuk menampung informasi.

# Python sendiri mempunyai tipe data yang cukup unik bila kita bandingkan dengan bahasa pemrograman yang lain.
"""
Boolean = True / False
String = Untuk nyimpen karaktek
Integer = Nyimpan angka
List = [1, 2, 3] (Bisa diubah)
Tuple = (1,2,3,45,) (Tidak bisa diubah)
Dictionary = key, value
"""

# BOOLEAN
# Sebuah akun tervalidasi atau tidak
validasi = False # Tidak tervalidasi
validasi2 = True # Tervalidasi

# STRING - Nyimpen karakter
nama = "Rizal Ilham"
kampus = 'Universitas Islam Negeri Ar-Raniry'
hasil = "Mahasiswa dengan nama " + nama + " Kuliah di kampus " + kampus
print(hasil)

# INTEGER - nyimpen angka
angka1 = 10
angka2 = 20

print("Hasil Penjumlahan 2 angka: ", angka1 + angka2)

# LIST
data_nama_siswa = ["Rizal", "Ilham", "Aulia", "Darul", "Daus"]
print(data_nama_siswa)
data_nama_siswa[0] = "Rizal(Update)"
print("Versi Update:", data_nama_siswa)


# DICTIONARY
d1 = {
    'nama': 'Ronaldo Wati',
    'tinggi': 150,
    'hobi': 'Main Bola'
}

print("Semua Data: ", d1)
print("Nama Saja: ", d1['nama'])
print("Tinggi: ", d1['tinggi'])
print("Hobi: ", d1['hobi'])