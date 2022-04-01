# Dictionary: Dictionary adalah tipe data pada python yang berfungsi untuk menyimpan kumpulan data/nilai dengan pendekatan “key-value”

data_siswa = {
    'nama': 'Rizal Ilham',
    'jurusan': 'Teknologi Informasi',
    'kampus': 'Universitas Islam Negeri Ar-Raniry'
    # 'semester': 8
}

# Akses nilai Dict
nama = data_siswa['nama']
jurusan = data_siswa['jurusan']

print(nama)
print(jurusan)

# Tambahkan data
data_siswa['semester'] = 8
print(data_siswa)

# Update Data
data_siswa['semester'] = 7
print(data_siswa)
