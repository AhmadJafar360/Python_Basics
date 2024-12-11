# String
nama = "Ahmad Ja'far Ali"
asal = "Lamongan"
instansi = "Universitas Negeri Surabaya"

# Mengakses Karakter String
karakter_pertama = nama[0] # Mengakses Karakter Pertama
karakter_terakhir = asal[-1] # Mengakses Karakter Terakhir
print(karakter_pertama, karakter_terakhir)

# Concatenation
nama_depan = "Ja'far"
nama_terakhir = "Ali"
nama_lengkap = nama_depan + "" + nama_terakhir # menggabungkan string

# Pengulangan String
pesan = "Selamat Siang"
pesan_ulang = pesan * 3 # Mengulang string 3 kali

kata = '''
Hallo semua,
Namaku Ahmad Ja'far Ali

Aku sekarang lagi belajar bahasa pemrograman python

Semoga aku bisa menguasai bahasa

'''
print(kata) 
print(kata[1]) # memanggil Huruf Pertama
print(pesan[1:-1]) # Menghilangkan kata pertama dan terakhir