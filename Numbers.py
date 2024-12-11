import math

# Aritmetic Operators / Operator Aritmatika
print (10 * 3)  # perkalian
print (10 + 3)  # pertambahan
print (10 - 3)  # pengurangan
print (10 / 3)  # Pembagian

# Operator precedence / Prioritas Operator
x = (10 + 3) * 2
print(x)

# Comparison Operators / Operator Perbandingan
x = 3 >= 2
print(x)
# ================= NOTE ================
# (>)  lebih besar
# (<)  lebih kecil
# (>=) lebih besar sama dengan
# (<=) lebih kecil sama dengan
# (==) sama dengan
# (!=) tidak sama dengan

# ==== Logical Operators / Operator Logika === #
# 1. Angka
jumlah = 11
print(jumlah > 10)
print(jumlah > 10 or jumlah < 4)

# 2. Boolean "True/False"
Income = True
Cash = False

if Income and not Cash:
  print("Aku gapapa sumpah")

# 3. Harga
Price = 1000000
Credit = True

if Credit : 
    down_payment = 0.1 * Price
else:
    down_payment = 0.2 * Price
print(f"Down payment: ${down_payment}")
# ================= NOTE ================
# and (both / keduanya)
# or (at least one / setidaknya satu)
# not (tidak memiliki nilai apapun)


# Function round() / Putaran Fungsi
ball = 188
pit = 250
distance = ball+pit
print(distance)

kecepatan = 70
waktu = distance/kecepatan
print(waktu)

# Math Functions / Fungsi Matematika
x = 2.9
print(round(x))
print(abs(-2.9))
print(math.ceil(2.9))