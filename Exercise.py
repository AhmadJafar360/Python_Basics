Berat = int(input("Berat: "))
Unit = input("(K)g atau (L)bs: ")
if Unit.upper() == "K" :
    Dikonversi = Berat / 0.45
    print("berat badan: " + str(Dikonversi) + "(L)bs")
else:
    Dikonversi = Berat * 0.45
    print("Berat badan: " + str(Dikonversi) + "(K)g")

# int(integer)
# str(string)