# Belajar Komentar

# Ini adalah Komentar / Digunakan untuk menulis keterangan kode

def penjumlahan():
    # Ini adalah fungsi penjumlahan
    print(1+2)

# Akan mencetak 10 - 2 == 8
print(10 - 2)
# Fungsi kita panggil setelah print
penjumlahan()


# Belajar komentar yang lebih dari 1 baris
"""
Komentar baris pertam
Komentar baris ke-2
Komentar baris ke-3
"""

def perkalian():
    """ 
    Details:
        Fungsi ini digunakan untuk mengembalikan hasil perkalian
    Params:
        angka1: 
    
    return:
        hasil(int)
    """
    hasil = 10 * 10
    # return digunakan untuk mengembalikan nilai
    return hasil

print("Hasil Perkalian: ", perkalian())