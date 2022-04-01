# Belajar Looping dalam Python / Pemrograman: Looping merupakan proses perulangan suatu blok pernyataan sebanyak yang diinginkan. 
# 1. While
# 2. Looping for
# 3 Nested loop di Python

# Looping While: Mengulangi selama kondisi terpenuhi
a = 0 # 1, 2, 3, 4
while a <= 3:                      # , Sampai kondisi jadi False
    a += 1
    print('Nilai a Sekarang: ', a)

# Looping For: Mengambil nilai dari dalam sebuah variable (object)
nilai = [1,2,3,4,5]

for i in nilai:              # 1, 2, 3, 4, 5
    print('nilai i: ', i)

# Nested Loop: Perulangan dalam Perulangan
semua_mata_kuliah = ['Matematika', 'Fisika', 'Informatika', 'Kimia']
nama_siswa = ['Rizal', 'Ilham', 'Ronaldo', 'Messi']

for mata_kuliah in semua_mata_kuliah:
    print('Mata Kuliah: ', mata_kuliah)
    print('Mahasiswa yang mengambil mata kuliah', mata_kuliah), # Matematika, Fisika, Informatika, Kimia
    
    # Looping dalam Looping
    for nama in nama_siswa:
        print('> ', nama) # Rizal, Ilham, Ronaldo, Messi