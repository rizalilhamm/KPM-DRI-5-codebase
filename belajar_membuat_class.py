# Class / Kelas :   Pada python bisa kita katakan sebagai sebuah blueprint (cetakan) dari objek (atau instance) yang ingin kita buat. 
#                   Kelas adalah cetakannya atau definisinya.
# 
# Object        :   Sedangkan objek (atau instance) adalah objek nyatanya, Instance dari Function di kelas


class Aritmatika:
    def __init__(self, a):
        self.a = a
        self.b = self.b

    def penjumlahan(self, a, b):
        return a + b

    def pengurangan(a, b):
        return a - b

    def perkalian(a, b):
        return a * b

    def pembagian(a, b):
        return a / b

object_aritmatika = Aritmatika()

pemjumlahan_hasil = object_aritmatika.penjumlahan(10, 10)
print(pemjumlahan_hasil)