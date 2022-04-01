# Pengkondisian dalam Python
# Pengkondisian adalah penentuan blok code yang akan dijalankan, perbagi kedalam 2 kondisi yaitu
# TRUE jika kondisi terpenuhi dan FALSE jika suatu kondisi tidak terpenuhi
# 1. If Else
# 2. If Elif Else

# Link Video: https://github.com/rizalilhamm/KPM-DRI-5-codebase

"""
If
Jika nilai benar
    Jalankan kode yang disini

Else
Jika yang atas tidak terpenuhi
    Jalankan kode yang disini
"""

nama = 'Rizal Ilham'

# Penggunaan IF ELSE
if nama == 'Rizal Ilham':               # True
    print('Benar Nama Rizal Ilham')

if nama != 'Ronaldo':                   # True
    print('Benar nama bukan Ronaldo!')

nilai = 10

# Penggunaan IF ELIF ELSE
if nilai > 10:                          # False
    print('Nilai diatas 10')
elif nilai < 10:                        # False, True
    print('Nilai dibawah 10')
else:                                   # Alternatif Terakhir
    print('Nilai adalah 10')