# String List
Nama = ['Aku', 'Arep', 'Muleh', 'Neng', 'Omah']
Nama[0] = 'Saya' # Mengganti kata Aku menjadi Saya
print(Nama)
print(Nama[0]) # Memanggil Kata pertama (Dimulai dari angka 0)
print(Nama[2:4]) # Memanggil kata ke dua dan empat
print(Nama[3:]) # Menghilangkan kata pertama sampai ke tiga

# Number List
Nomor = [10, 5, 9, 7, 6, 8]
max = Nomor[0] # Memanggil Nomor pertama (Dimulai dari angka 0)
for Nomer in Nomor:
    if Nomer > max:
      max = Nomer
print(max)

# 2D List
matrix = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]
# matrix [0][1] = 20
# print(matrix[0][1])

for row in matrix:
   for item in row:
    print(item)

# List Methods
Numbers = [5, 3, 4, 2, 1]
Numbers2 = Numbers.copy()
Numbers.append(9)
# Numbers.insert(0, 10)
# Numbers.remove(1)
print(Numbers2)

# tulis sebuah program untuk menghapus duplikat dalam daftar (Solution)
Number = [5,4,6,7,1,3]
uniques = []
for Numbe in Number:
   if Numbe not in uniques:
      uniques.append(Numbe)
      print(uniques) 